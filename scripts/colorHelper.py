#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import random

#########################################################
# Functions
#########################################################


def randomColor(min=0, max=255):
    return tuple([random.randint(min, max) for _ in [0, 1, 2]])


def randomLightColors():
    return randomColor(127, 255)


def randomDarkColors():
    return randomColor(0, 127)
