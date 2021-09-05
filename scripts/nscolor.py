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

HSV_MODE_IPKit_RANGE = 0
HSV_MODE_OPENCV_RANGE = 1
HSV_MODE_GRAPHICAL_SOFTWARE_RANGE = 2

#########################################################
# Functions
#########################################################


def randomColor(min=0, max=255):
    return tuple([random.randint(min, max) for _ in [0, 1, 2]])


def randomLightColors():
    return randomColor(127, 255)


def randomDarkColors():
    return randomColor(0, 127)


def getHSV(im):
    '''
    DEPRECATED
    '''
    hsv = im.copy()
    hsv = conv(hsv, CONV_TYPE_BGR2HSV)
    (h, s, v) = proc.split(hsv)
    return h, s, v


def fixHSVRange(h, s, v):
    '''
    H,S,V: (0-360,0-100%,0-100%) to (0-180,0-255 ,0-255) 
    '''
    return (180 * h / 360, 255 * s / 100, 255 * v / 100)


CONV_TYPE_BGR2HSV = 0
CONV_TYPE_BGR2GRAY = 1
CONV_TYPE_GRAY2BGR = 2
CONV_TYPE_HSV2BGR = 3


def conv(im, convType):
    pass


def changeHue(im, hue=130, hsvMode=HSV_MODE_GRAPHICAL_SOFTWARE_RANGE):
    if hsvMode == HSV_MODE_GRAPHICAL_SOFTWARE_RANGE:
        hue = 180 * hue / 360
    h, s, v = getHSV(im)
    h[:] = hue
    hsv = proc.merge([h, s, v])
    bgr = conv(hsv, CONV_TYPE_HSV2BGR)
    return bgr


def changeSaturation(im, sat=130, hsvMode=HSV_MODE_GRAPHICAL_SOFTWARE_RANGE):
    if hsvMode == HSV_MODE_GRAPHICAL_SOFTWARE_RANGE:
        sat = 255 * sat / 100
    h, s, v = getHSV(im)
    s[:] = sat
    hsv = proc.merge([h, s, v])
    bgr = conv(hsv, CONV_TYPE_HSV2BGR)
    return bgr


def changeBrightness(im, val=130, hsvMode=HSV_MODE_GRAPHICAL_SOFTWARE_RANGE):
    if hsvMode == HSV_MODE_GRAPHICAL_SOFTWARE_RANGE:
        val = 255 * val / 100
    h, s, v = getHSV(im)
    v[:] = val
    hsv = proc.merge([h, s, v])
    bgr = conv(hsv, CONV_TYPE_HSV2BGR)
    return bgr
