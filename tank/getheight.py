#!/usr/bin/env python

import math 

g = -9.81 ## meters/(sec^2)

def getHeight(x, v, t):
    return (x * math.tan(t) - ( (g * (x**2)) / (2 * (v * math.cos(t))**2))) 

def getDistance(v, t):
    #return ( (v * math.cos(t)) / g ) * ( (v * math.sin(t)) + math.sqrt( (v * (math.sin(t)))**2 + (2 * g * 0 )))
    return ( (v**2 * (math.sin(2 * t))) / g )

v = 44
for a in range(0, 91, 5):
    d = getDistance(v, a)
    print "ANGLE IS {0}, DISTANCE IS {1}".format(a, d)
    for t in range(1, d, 2):
        print "{0}, {1}".format(t, getHeight(t, v, math.radians(a)))

#print getDistance(50, 90)

#for i in range(0, 181, 5):
#    print 'sin: {0}, cos: {1} (theta {2})'.format(math.sin(i), math.cos(i), i)

