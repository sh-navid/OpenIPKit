#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import sys
import math
import numpy as np
import scripts.nssys as nss
import scripts.nsproc as proc
import scripts.nsmath as nmth
import scripts.nsarray as arr
import scripts.nscolor as nsc
import scripts.backend as back

#########################################################
# Source code
#########################################################
im = back.imread(sys.path[0]+'/media/back.png')
h1, h2, h3, h4, h5 = None, None, None, None, None
s1, s2, s3, s4, s5 = None, None, None, None, None
b1, b2, b3, b4, b5 = None, None, None, None, None


def run():
    global h1, h2, h3, h4, h5
    global s1, s2, s3, s4, s5
    global b1, b2, b3, b4, b5

    h1 = nsc.changeColor(im, color=0)
    h2 = nsc.changeColor(im, color=90)
    h3 = nsc.changeColor(im, color=160)
    h4 = nsc.changeColor(im, color=240)
    h5 = nsc.changeColor(im, color=310)

    s1 = nsc.changeGrayness(im, grayness=5)
    s2 = nsc.changeGrayness(im, grayness=25)
    s3 = nsc.changeGrayness(im, grayness=50)
    s4 = nsc.changeGrayness(im, grayness=75)
    s5 = nsc.changeGrayness(im, grayness=95)

    b1 = nsc.changeIlumination(im, ilumination=15)
    b2 = nsc.changeIlumination(im, ilumination=35)
    b3 = nsc.changeIlumination(im, ilumination=55)
    b4 = nsc.changeIlumination(im, ilumination=75)
    b5 = nsc.changeIlumination(im, ilumination=100)


nss.execMonitor(run, True)
back.imshow('Hue', np.hstack((im, h1, h2, h3, h4, h5)))
back.imshow('Saturation', np.hstack((im, s1, s2, s3, s4, s5)))
back.imshow('Brightness', np.hstack((im, b1, b2, b3, b4, b5)))
