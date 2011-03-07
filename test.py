#!/usr/bin/python

import tank
l = tank.Landscape()

print l

h = l.heightAt(0)
t = tank.Trajectory(5, 15, initial_y=h+1)
copy = l
copy.drawTrajectory(t)
for x in range(0, 20):
    copy = l
    y = t.getHeight(x)
    if l.heightAt(x) >= y:
        print "you hit land! {0}, {1}".format(x, y)
        break
    else:
        print "{0}, {1}".format(x, y)
