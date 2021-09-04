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
    x1, y1 = pt1[:2]
    x2, y2 = pt2[:2]
    div = (x2-x1)
    if div == 0:
        m = 0
    else:
        m = (y2-y1)/div
    # y=mx+b => b=y-mx
    b = y1-m*x1
    return m, b


def calcLineX(m, b, y):
    # y=mx+b => mx=y-b => x=(y-b)/m
    if m==0:
        return 0
    return (y-b)/m


def calcLineY(m, b, x):
    return m*x+b
