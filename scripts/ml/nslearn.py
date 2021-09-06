import sys
import math
import numpy as np
import scripts.nssys as nss
import scripts.nsproc as proc
import scripts.nsmath as nmth
import scripts.nsarray as arr
import scripts.nscolor as nsc
import scripts.backend as back

'''
I want to make a very siple machine learning algorithm from scratch
'''

BLOCK_SIZE = 4


def simpleCategoryLearn(imList, size, catNo):
    '''
    imList: [im1, im2, ..., imN]
    size: 8, 16, 32, 64
    '''
    off = size//BLOCK_SIZE
    samples = []
    for im in imList:
        im = back.resize(im, (size, size))
        sample = []
        for r in off:
            for c in off:
                y, x = r*BLOCK_SIZE, c*BLOCK_SIZE
                block = im[y:y+BLOCK_SIZE, x:x+BLOCK_SIZE]
                sample.append(np.median(block))
                pass
        samples.append(sample)
    return {'size': size, 'catNo': catNo, 'samples': samples}


def simpleCategoryDetect(im, model, checkMirror=False, checkUpsideDown=False, checkRotated=False):
    '''
    model: {'size':size,'catNo':catNo,'samples':samples}
    '''
    size = model['size']
    catNo = model['catNo']
    samples = model['samples']
    off = size//BLOCK_SIZE
    bestProbability = 0
    '''...'''
    return bestProbability
