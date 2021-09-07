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
import scripts.nssys as nss
import scripts.nsproc as proc
import scripts.nsdraw as draw
import scripts.nscolor as nsc
import scripts.backend as back
import scripts.ml.nslearn as learn

#########################################################
# Source code
#########################################################
def run():
    k = proc.kernel((11, 11), proc.KERNEL_TYPE_CIRCULAR_FADE)
    print(k)

nss.execMonitor(run,True)
