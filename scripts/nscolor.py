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

def getHSV(im):
    '''
    DEPRECATED
    '''
    hsv = im.copy()
    hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
    (h, s, v) = cv2.split(hsv)
    return h, s, v


def fixHSVRange(h, s, v):
    '''
    DEPRECATED
    '''
    # Normal H,S,V: (0-360,0-100%,0-100%)
    # OpenCV H,S,V: (0-180,0-255 ,0-255)
    return (180 * h / 360, 255 * s / 100, 255 * v / 100)


HSV_MODE_OPENCV_RANGE = 0
HSV_MODE_GRAPHICAL_SOFTWARE_RANGE = 1


def changeHue(im, hue=130, hsvMode=HSV_MODE_GRAPHICAL_SOFTWARE_RANGE):
    '''
    DEPRECATED
    '''
    if hsvMode == HSV_MODE_GRAPHICAL_SOFTWARE_RANGE:
        hue = 180 * hue / 360
    h, s, v = getHSV(im)
    h[:] = hue
    hsv = cv2.merge([h, s, v])
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return bgr


def changeSaturation(im, sat=130, hsvMode=HSV_MODE_GRAPHICAL_SOFTWARE_RANGE):
    '''
    DEPRECATED
    '''
    if hsvMode == HSV_MODE_GRAPHICAL_SOFTWARE_RANGE:
        sat = 255 * sat / 100
    h, s, v = getHSV(im)
    s[:] = sat
    hsv = cv2.merge([h, s, v])
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return bgr


def changeBrightness(im, val=130, hsvMode=HSV_MODE_GRAPHICAL_SOFTWARE_RANGE):
    '''
    DEPRECATED
    '''
    if hsvMode == HSV_MODE_GRAPHICAL_SOFTWARE_RANGE:
        val = 255 * val / 100
    h, s, v = getHSV(im)
    v[:] = val
    hsv = cv2.merge([h, s, v])
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return bgr
