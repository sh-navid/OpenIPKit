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


def NSC(im):
    nsc = im.copy()
    nsc = conv(nsc, CONV_TYPE_BGR2NSC)
    (c, g, i) = proc.split(nsc)
    return c, g, i


def fixHSVRange(h, s, v):
    '''
    H,S,V: (0-360,0-100%,0-100%) to (0-180,0-255 ,0-255) 
    '''
    return (180 * h / 360, 255 * s / 100, 255 * v / 100)


CONV_TYPE_BGR2NSC = 0 # NSC is my name + COLOR -> NS+Color
CONV_TYPE_NSC2BGR = 3


def conv(im, convType):
    if convType == CONV_TYPE_BGR2NSC:
        one=im/255
        b,g,r=proc.split(one)


        # NSC -> NS-COLOR -> Color, Grayness, Ilumination
        one=proc.merge(r, g, b)
        return one*255  # h,s,v
    elif convType == CONV_TYPE_NSC2BGR:
        
        return im
    return None


def changeHue(im, hue=130, hsvMode=HSV_MODE_GRAPHICAL_SOFTWARE_RANGE):
    if hsvMode == HSV_MODE_GRAPHICAL_SOFTWARE_RANGE:
        hue = 180 * hue / 360
    h, s, v = NSC(im)
    h[:] = hue
    hsv = proc.merge(h, s, v)
    bgr = conv(hsv, CONV_TYPE_NSC2BGR)
    return bgr


def changeSaturation(im, sat=130, hsvMode=HSV_MODE_GRAPHICAL_SOFTWARE_RANGE):
    if hsvMode == HSV_MODE_GRAPHICAL_SOFTWARE_RANGE:
        sat = 255 * sat / 100
    h, s, v = NSC(im)
    s[:] = sat
    hsv = proc.merge(h, s, v)
    bgr = conv(hsv, CONV_TYPE_NSC2BGR)
    return bgr


def changeBrightness(im, val=130, hsvMode=HSV_MODE_GRAPHICAL_SOFTWARE_RANGE):
    if hsvMode == HSV_MODE_GRAPHICAL_SOFTWARE_RANGE:
        val = 255 * val / 100
    h, s, v = NSC(im)
    v[:] = val
    hsv = proc.merge(h, s, v)
    bgr = conv(hsv, CONV_TYPE_NSC2BGR)
    return bgr
