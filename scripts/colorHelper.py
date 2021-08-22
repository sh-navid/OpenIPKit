#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import random
import cv2

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
    hsv = im.copy()
    hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
    (h, s, v) = cv2.split(hsv)
    return h,s,v

# Fixme: pass mask ro RIO to changeHue, changeSaturation and changeBrightness

def changeHue(im, hue=130):
    h,s,v=getHSV(im)
    h[:] = hue
    hsv = cv2.merge([h, s, v])
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return bgr

def changeSaturation(im, sat=130):
    h,s,v=getHSV(im)
    s[:] = sat
    hsv = cv2.merge([h, s, v])
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return bgr

def changeBrightness(im, val=130):
    h,s,v=getHSV(im)
    v[:] = val
    hsv = cv2.merge([h, s, v])
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return bgr
