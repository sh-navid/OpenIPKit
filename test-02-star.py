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
cx, ch = w/2, h/2
rc = nsc.randomColor

draw.star(im, (cx-cx/1.6, ch), ch/2, color=rc(), rotation=-90)
draw.star(im, (cx, ch), ch/2, color=rc(),
             rotation=-90, thickness=10, points=9)
draw.star(im, (cx+cx/1.6, ch), ch/2, color=rc(), points=15, thickness=30)


cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
