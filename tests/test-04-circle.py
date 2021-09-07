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
    ox, oh, cx, cy, o = w/4, h/4, w/2, h/2, (w/2)/1.6
    rc = nsc.randomColor

    draw.circle(im, (cx-o, cy), h/14, color=rc(), thickness=2, arc=180, rotation=0)
    draw.circle(im, (cx-o, cy), h/7, color=rc(), thickness=10, arc=90, rotation=-90)
    draw.circle(im, (cx-o, cy), h/4, color=rc(), thickness=25, arc=270, rotation=-180)
    draw.circle(im, (cx, cy), h/14, color=rc(), thickness=2)
    draw.circle(im, (cx, cy), h/7, color=rc(), thickness=10)
    draw.circle(im, (cx, cy), h/4, color=rc(), thickness=25)
    draw.circle(im, (cx+o, cy), h/14, color=rc(), endLastLine=False, thickness=2, arc=180, rotation=0)
    draw.circle(im, (cx+o, cy), h/7, color=rc(), endLastLine=False, thickness=10, arc=90, rotation=-90)
    draw.circle(im, (cx+o, cy), h/4, color=rc(), endLastLine=False, thickness=25, arc=270, rotation=-180)

nss.execMonitor(run,True)
back.imshow('Test', im)