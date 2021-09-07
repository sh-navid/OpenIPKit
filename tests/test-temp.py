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
def run():
    k = proc.kernel((11, 11), proc.KERNEL_TYPE_CIRCULAR_FADE)
    print(k)

nss.execMonitor(run,True)
