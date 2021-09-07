#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import sys
[sys.path.append(pth) for pth in '.']
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
    global im
    im = draw.grid(im)
    im = draw.grid(im, color1=(127,0,255),color2=(200,200,200),thickness=20)
    print(signature(draw.grid))

nss.execMonitor(run,True)
back.imshow('Test', im)