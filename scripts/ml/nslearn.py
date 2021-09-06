import sys
import math
import numpy as np
import scripts.nssys as nss
import scripts.nsproc as proc
import scripts.nsmath as nmth
import scripts.nsarray as arr
import scripts.nscolor as nsc
import scripts.backend as back

def simpleCategoryLearn(imList,size,catNo):
    '''
    imList: [im1, im2, ..., imN]
    size: 8, 16, 32, 64
    '''
    samples=[]
    
    return {'size':size,'catNo':catNo,'samples':samples}

def simpleCategoryDetect(im,model):
    
    pass