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
    cx, ch, of = w/2, h/2, h/18
    rc = nsc.randomColor

    draw.triangle(im, (cx-cx/1.6, ch+of), ch/2, color=rc(), rotation=-90)
    draw.triangle(im, (cx, ch-of), ch/2, color=rc(), rotation=-45, thickness=15)
    draw.triangle(im, (cx+cx/1.6, ch-of), ch/2, color=rc(), thickness=30)

nss.execMonitor(run,True)
back.imshow('Test', im)