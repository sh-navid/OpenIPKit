#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import cv2
import sys
import numpy as np
from inspect import signature
import scripts.nsproc as proc
import scripts.nsdraw as draw
import scripts.nscolor as nsc

#########################################################
# Source code
#########################################################
im = cv2.imread(sys.path[0]+'/media/im.png')

h, w = im.shape[:2]
cx, ch, of = w/2, h/2, h/18
rc = nsc.randomColor

draw.triangle(im, (cx-cx/1.6, ch+of), ch/2, color=rc(), rotation=-90)
draw.triangle(im, (cx, ch-of), ch/2, color=rc(), rotation=-45, thickness=15)
draw.triangle(im, (cx+cx/1.6, ch-of), ch/2, color=rc(), thickness=30)

cv2.imshow('Test', im)
cv2.waitKey(0)