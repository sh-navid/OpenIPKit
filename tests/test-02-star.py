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
    cx, ch = w/2, h/2
    rc = nsc.randomColor

    draw.star(im, (cx-cx/1.6, ch), ch/2, color=rc(), rotation=-90)
    draw.star(im, (cx, ch), ch/2, color=rc(),
                 rotation=-90, thickness=10, points=9)
    draw.star(im, (cx+cx/1.6, ch), ch/2, color=rc(), points=15, thickness=30)


nss.execMonitor(run,True)
back.imshow('Test', im)
