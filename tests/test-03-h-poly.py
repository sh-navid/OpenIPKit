#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import sys
import numpy as np
from inspect import signature
import scripts.nsproc as proc
import scripts.nsdraw as draw
import scripts.nscolor as nsc
import scripts.backend as back
import scripts.nssys as nss

#########################################################
# Source code
#########################################################

im = back.imread(sys.path[0]+'/media/im.png')

def run():
    h, w = im.shape[:2]
    cx, ch = w/2, h/2
    rc = nsc.randomColor

    draw.hPoly(im, (cx-cx/1.6, ch), ch/2, color=rc(), rotation=-90)
    draw.hPoly(im, (cx, ch), ch/2, color=rc(),rotation=-90, thickness=10, points=9)
    draw.hPoly(im, (cx+cx/1.6, ch), ch/2,color=rc(), points=15, thickness=30)

nss.execMonitor(run,True)
back.imshow('Test', im)