#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import math

#########################################################
# Functions
#########################################################


def dist(pt1, pt2):
    '''Return the distance between 2 points'''
    # return math.sqrt(abs(pt1[0]-pt2[0])**2 + abs(pt1[1]-pt2[1])**2)
    dx, dy = dXY(pt1, pt2)
    return math.hypot(dx, dy)


def dXY(pt1, pt2):
    dx = pt2[0]-pt1[0]
    dy = pt2[1]-pt1[1]
    return (dx, dy)


def absDXY(pt1, pt2):
    dx, dy = dXY(pt1, pt2)
    return (abs(dx), abs(dy))


def lineEq(pt1, pt2):
    '''
    line eq is y=mx+b
    return m, b
    '''
    dx, dy = dXY(pt1, pt2)
    m = dy if dx == 0 else dy/dx
    # y=mx+b => b=y-mx
    b = pt2[1]-(m*pt2[0])
    return m, b


def calcLineX(m, b, y):
    # y=mx+b => mx=y-b => x=(y-b)/m
    return 0 if m == 0 else (y-b)/m


def calcLineY(m, b, x):
    return m*x+b
