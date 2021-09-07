#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import sys
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
    ox, oh, cx = w/4, h/4, w/2
    rc = nsc.randomColor

    pt1, pt2, pt3 = (ox, h-h/8), (cx, oh), (w-ox, h-h/8)
    draw.curve(im, [pt1, pt2, pt3], thickness=4)


nss.execMonitor(run, True)
back.imshow('Test', im)
