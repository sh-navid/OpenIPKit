#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################

#########################################################
# Functions
#########################################################
def toInt1dArray(arr):
    return [int(x) for x in arr]

def toInt2dArray(arr):
    return [[int(y) for y in x] for x in arr]

def toInt3dArray(arr):
    return [[[int(z) for z in y] for y in x] for x in arr]

# Fixme: how to write a function for Nd Array?? use EVAL later