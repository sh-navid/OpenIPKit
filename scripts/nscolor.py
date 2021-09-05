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
import scripts.nsproc as proc
import scripts.nsmath as nmth
import scripts.nsarray as arr

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



def shiftChannel(im, channel=0,shift=30):
    channels = np.array(proc.split(im))
    channels[:][channel] = shift
    return proc.merge(channels)