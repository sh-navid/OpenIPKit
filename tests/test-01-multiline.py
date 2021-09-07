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
sys.path.append('.')
import openipkit.nssys as nss
import openipkit.nsproc as proc
import openipkit.nsdraw as draw
import openipkit.nscolor as nsc
import openipkit.backend as back
import openipkit.ml.nslearn as learn

#########################################################
# Source code
#########################################################
im = back.imread(sys.path[0]+'/media/im.png')

def run():
    h, w = im.shape[:2]
    cx, ch = w/2, h/2
    rc = nsc.randomColor

    draw.line(im, (60, 303), (151, 40), color=rc(),thickness=3)

    draw.multiline(im, [(240, 307), (330, 40)], color=rc(),
                arrowType=draw.MULTILINE_ARROW_END,thickness=5)

    x = 0
    pts = [(418+x, 303), (461+x, 195),  (539+x, 140), (520+x, 40)]
    draw.multiline(im, pts, color=rc(), arrowType=draw.MULTILINE_ARROW_NONE,thickness=9)

    x = 205
    pts = [(418+x, 303), (461+x, 195),  (539+x, 140), (520+x, 40)]
    draw.multiline(im, pts, color=rc(), arrowType=draw.MULTILINE_ARROW_END,thickness=13)

    x = 410
    pts = [(418+x, 303), (461+x, 195),  (539+x, 140), (520+x, 40)]
    draw.multiline(im, pts, color=rc(), arrowType=draw.MULTILINE_MULTIPLE_ARROW,thickness=21)


nss.execMonitor(run,True)
back.imshow('Test', im)