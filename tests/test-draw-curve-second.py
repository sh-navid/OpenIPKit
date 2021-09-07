#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import openipkit.ml.nslearn as learn
import openipkit.backend as back
import openipkit.nscolor as nsc
import openipkit.nsdraw as draw
import openipkit.nsproc as proc
import openipkit.nsmath as nmth
import openipkit.nssys as nss
import sys
sys.path.append('.')

#########################################################
# Source code
#########################################################
im = back.imread(sys.path[0]+'/media/im.png')


def run():
    h, w = im.shape[:2]
    ox, oh, cx = w/4, h/4, w/2
    rc = nsc.randomColor

    pt1, pt2, pt3 = (ox, h-h/8), (cx, oh), (w-ox, h-h/8)
    draw.curve(im, [pt1, pt2, pt3])


nss.execMonitor(run, True)
back.imshow('Test', im)
