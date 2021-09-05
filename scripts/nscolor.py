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


def NSC(im):
    '''
    I had trouble finding the border between nail and skin colors for a few days. 
    That's why I decided to create my own color format called NSC. 
    The first two letters are my name. I am working on this color algorithm. 
    I am slowly optimizing its code.

    I think I should completely separate the colors from the rest of the color format.
    I want to make a mask from nails.
    So in the end it does not matter if I can convert this format again with BGR,
    but if possible, is better. 
    So I made a flag for reversibility but I may delete it later. 
    I'm thinking about Grayness and Illumination. Maybe they will change or remove later.
    '''
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

        M=np.max(b,g,r)
        m=np.min(b,g,r)
        ME=np.mean(b,g,r)
        MD=np.median(b,g,r)
       


        # NSC -> NS-COLOR -> Color, Grayness, Ilumination
        one=proc.merge(r, g, b)
        return one*255
    elif convType == CONV_TYPE_NSC2BGR:
        
        return im
    return None


def changeColor(im, color=130):
    '''
    Not working yet; and i'm not sure about backward compatibility yet
    I want to push colors to c, i am not sure about g and i parameters yet
    '''
    c, g, i = NSC(im)
    c[:] = color
    hsv = proc.merge(c, g, i)
    bgr = conv(hsv, CONV_TYPE_NSC2BGR)
    return bgr


def changeGrayness(im, grayness=130):
    c, g, i = NSC(im)
    g[:] = grayness
    nsc = proc.merge(c, g, i)
    bgr = conv(nsc, CONV_TYPE_NSC2BGR)
    return bgr


def changeIlumination(im, ilumination=130):
    c, g, i = NSC(im)
    i[:] = ilumination
    nsc = proc.merge(c, g, i)
    bgr = conv(nsc, CONV_TYPE_NSC2BGR)
    return bgr
