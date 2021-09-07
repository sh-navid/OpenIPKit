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

im = back.imread(sys.path[0]+'/media/back.png')
gry1 = None
gry2 = None
gry3 = None
bw = None


def run():
    global gry1, gry2, gry3, bw
    gry1 = proc.toGray(im, proc.GRAY_MODE_A)
    gry2 = proc.toGray(im, proc.GRAY_MODE_B)
    gry3 = proc.toGray(im, proc.GRAY_MODE_C)

    gry1 = proc.toBGR(gry1)
    gry2 = proc.toBGR(gry2)
    gry3 = proc.toBGR(gry3)

    bw = proc.treshSimple(gry3, 240)


nss.execMonitor(run, True)
back.imshow('proc', np.hstack((im/255, gry1/255, gry2/255, gry3/255, bw/255)))
