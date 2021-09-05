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

h, w = im.shape[:2]
cx, ch, of = w/2, h/2, h/18
rc = nsc.randomColor

draw.triangle(im, (cx-cx/1.6, ch+of), ch/2, color=rc(), rotation=-90)
draw.triangle(im, (cx, ch-of), ch/2, color=rc(), rotation=-45, thickness=15)
draw.triangle(im, (cx+cx/1.6, ch-of), ch/2, color=rc(), thickness=30)

back.imshow('Test', im)