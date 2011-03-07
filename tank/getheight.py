#!/usr/bin/env python

import math 

g = 9.81 ## meters/(sec^2)

def getHeight(x, v, angle):
    t = math.radians(angle)
    return (x * math.tan(t) - ( (g * (x**2)) / (2 * (v * math.cos(t))**2)))

def getPos(velocity, angle, time):
    angle   = math.radians(angle)
    v_horiz = velocity * math.cos(angle)
    v_vert  = velocity * math.sin(angle)
    x_pos   = v_horiz * time
    y_pos   = ( v_vert * time ) - ( .5 * g * (time**2) )
    return (x_pos / 100 , y_pos / 100 )
    
    return "x is {0} and y is {1}".format(x_pos, y_pos)
    

angle = 60
v = 30
for t in range(0, 20):
    (x, y) = getPos(v, angle, t)
    print "At time {0}, x is {1} and y is {2}".format(t,x,y)

h = getHeight(200, 100, 60)
print h