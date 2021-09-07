#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import random
import math
import numpy as np
import openipkit.nsproc as proc
import openipkit.nsmath as nmth
import openipkit.nsarray as arr

#########################################################
# CONSTANTS
#########################################################

#########################################################
# Functions
#########################################################


def randomColor(min=0, max=255):
    return tuple([random.randint(min, max) for _ in [0, 1, 2]])


def randomLightColors():
    return randomColor(127, 255)


def randomDarkColors():
    return randomColor(0, 127)


def changeChannel(im, channel=0,newValue=30):
    channels = np.array(proc.split(im))
    channels[:][channel] = newValue
    return proc.merge(channels)