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
    return (abs(pt1[0]-pt2[0]), abs(pt1[1]-pt2[1]))


def lineEq(pt1,pt2):
    x1,y1=pt1[:2]
    x2,y2=pt1[:2]
    m=(y2-y1)/(x2-x1)
    
