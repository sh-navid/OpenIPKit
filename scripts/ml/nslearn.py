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


def simpleCategoryLearn(imList, sampleSize=8, blockSquareSize=4):
    '''
    imList: [im1, im2, ..., imN]
    size: 8, 16, 32, 64
    '''
    off = sampleSize//blockSquareSize
    samples = []
    for im in imList:
        im = back.resize(im, (sampleSize, sampleSize))
        sample = []
        for r in range(0, off):
            for c in range(0, off):
                y, x = r*blockSquareSize, c*blockSquareSize
                block = im[y:y+blockSquareSize, x:x+blockSquareSize]
                sample.append(np.mean(block))
                pass
        samples.append(sample)
        print(sample)
    return {'sampleSize': sampleSize, 'blockSquareSize': blockSquareSize, 'samples': samples}


def simpleCategoryDetect(im, model, checkMirror=False, checkUpsideDown=False, checkRotated=False):
    '''
    model: {'sampleSize': sampleSize,'blockSquareSize':blockSquareSize, 'samples': samples}
    '''
    sampleSize = model['sampleSize']
    blockSquareSize = model['blockSquareSize']
    samples = model['samples']
    off = sampleSize//blockSquareSize
    bestProbability = 0
    '''...'''
    return bestProbability
