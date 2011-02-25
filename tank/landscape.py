import random

class Landscape(object):

    def __init__(self, width=65, height=30, bumpiness=2):
        self.width      = width
        self.height     = height
        self.bumpiness  = bumpiness

        self.maxHeight  = self.height - 5
        self.columns    = list()

        self.generate()

    def __repr__(self):
        s = ""
        for h in range(0, self.height + 1):
            for c in range(0, self.width +1):
                col = self.columns[c]
                s += col.draw(self.height - h)
            s += "\n"
        return s


    def generate(self):
        prevHeight = random.randint(0, self.maxHeight)
        self.columns.append(Column(prevHeight))

        for n in range(0, self.width):
            difference = random.randint((self.bumpiness * -1), self.bumpiness)
            thisHeight = prevHeight + difference
            if thisHeight < 0:
                thisHeight = 0
            if thisHeight > self.maxHeight:
                thisHeight = self.maxHeight

            self.columns.append(Column(thisHeight))
            prevHeight = thisHeight
            
    
class Column(object):

    def __init__(self, height):
        self.height = height
        self.landChar = "#"
        self.airChar  = " "

    def draw(self, num):
        if num <= self.height:
            return self.landChar
        else:
            return self.airChar
