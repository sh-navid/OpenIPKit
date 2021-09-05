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
a1, a2, a3 = None, None, None
b1, b2, b3 = None, None, None
c1, c2, c3 = None, None, None


def run():
    global a1, a2, a3
    global b1, b2, b3
    global c1, c2, c3

    a1 = nsc.shiftChannel(im, channel=0, shift=0)
    a2 = nsc.shiftChannel(im, channel=0, shift=100)
    a3 = nsc.shiftChannel(im, channel=0, shift=200)

    b1 = nsc.shiftChannel(im, channel=1, shift=0)
    b2 = nsc.shiftChannel(im, channel=1, shift=100)
    b3 = nsc.shiftChannel(im, channel=1, shift=200)

    c1 = nsc.shiftChannel(im, channel=2, shift=0)
    c2 = nsc.shiftChannel(im, channel=2, shift=100)
    c3 = nsc.shiftChannel(im, channel=2, shift=200)


nss.execMonitor(run, True)
back.imshow('A', np.hstack((im, a1, a2, a3))/255)
back.imshow('B', np.hstack((im, b1, b2, b3))/255)
back.imshow('C', np.hstack((im, c1, c2, c3))/255)
