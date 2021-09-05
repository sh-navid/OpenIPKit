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

    draw.line(im, (60, 303), (151, 40), color=rc())

    draw.multiline(im, [(240, 307), (330, 40)], color=rc(),
                arrowType=draw.MULTILINE_ARROW_END)

    x = 0
    pts = [(418+x, 303), (461+x, 195),  (539+x, 140), (520+x, 40)]
    draw.multiline(im, pts, color=rc(), arrowType=draw.MULTILINE_ARROW_NONE)

    x = 205
    pts = [(418+x, 303), (461+x, 195),  (539+x, 140), (520+x, 40)]
    draw.multiline(im, pts, color=rc(), arrowType=draw.MULTILINE_ARROW_END)

    x = 410
    pts = [(418+x, 303), (461+x, 195),  (539+x, 140), (520+x, 40)]
    draw.multiline(im, pts, color=rc(), arrowType=draw.MULTILINE_MULTIPLE_ARROW)


nss.execMonitor(run,True)
back.imshow('Test', im)