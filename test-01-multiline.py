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
import scripts.nspaint as paint

#########################################################
# Source code
#########################################################

im = cv2.imread(sys.path[0]+'/media/im.png')

h, w = im.shape[:2]
cx, ch = w/2, h/2
rc = nsc.randomColor

draw.line(im, (60, 303), (151, 40), color=rc())

draw.line(im, (240, 307), (330, 40), color=rc())

x = 0
pts = [(418+x, 303), (461+x, 195),  (539+x, 140), (520+x, 40)]
paint.multiline(im, pts, color=rc(), arrowType=paint.MULTILINE_ARROW_NONE)

x = 205
pts = [(418+x, 303), (461+x, 195),  (539+x, 140), (520+x, 40)]
paint.multiline(im, pts, color=rc(), arrowType=paint.MULTILINE_ARROW_END)

x = 410
pts = [(418+x, 303), (461+x, 195),  (539+x, 140), (520+x, 40)]
paint.multiline(im, pts, color=rc(), arrowType=paint.MULTILINE_MULTIPLE_ARROW)


cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
