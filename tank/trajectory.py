import math

g = 9.8 ## meters / sec^2

class Trajectory(object):
    
    def __init__(self, velocity, angle, initial_x=0, initial_y=0):
        
        self.v     = velocity
        self.theta = math.radians(angle) 
        
        self.initial_y = initial_y
        self.initial_x = initial_x
        
                
    def getHeight(self, x):
        return (x * math.tan(self.theta) - ( (g * (x**2)) / (2 * (self.v * math.cos(self.theta))**2))) + self.initial_y

    def getPos(self, time):
        angle   = math.radians(self.theta)
        v_horiz = self.v * math.cos(self.theta)
        v_vert  = self.v * math.sin(self.theta)
        x_pos   = v_horiz * time
        y_pos   = ( v_vert * time ) - ( .5 * g * (time**2) )
        return (x_pos / 100, y_pos + self.initial_y)