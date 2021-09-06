#########################################################
# Author: sh-navid
#########################################################
'''
I want to make a very simple machine learning algorithm
from scratch
'''
#########################################################
# Add preprocessors
#########################################################
import sys
import math
import numpy as np
import scripts.nssys as nss
import scripts.nsproc as proc
import scripts.nsmath as nmth
import scripts.nsarray as arr
import scripts.nscolor as nsc
import scripts.backend as back

#########################################################
# Source code
#########################################################
def generateSimpleSample(im,sampleSize,blockSquareSize):
    sample = []
    off = sampleSize//blockSquareSize
    for r in range(0, off):
        for c in range(0, off):
            y, x = r*blockSquareSize, c*blockSquareSize
            block = im[y:y+blockSquareSize, x:x+blockSquareSize]
            sample.append(np.mean(block))
    return sample


def simpleCategoryLearn(imList, sampleSize=8, blockSquareSize=4):
    '''
    imList: [im1, im2, ..., imN]
    size: 8, 16, 32, 64
    '''
    
    samples = []
    for im in imList:
        im = back.resize(im, (sampleSize, sampleSize))
        sample=generateSimpleSample(im,sampleSize,blockSquareSize)
        samples.append(sample)
        #print(sample)
    return {'sampleSize': sampleSize, 'blockSquareSize': blockSquareSize, 'samples': samples}


def simpleCategoryDetect(im, model, checkMirror=False, checkUpsideDown=False, checkRotated=False):
    '''
    model: {'sampleSize': sampleSize,'blockSquareSize':blockSquareSize, 'samples': samples}
    return distance between sample and models
    if returns 0 it means identical match
    '''
    sampleSize = model['sampleSize']
    blockSquareSize = model['blockSquareSize']
    samples = model['samples']
    im = back.resize(im, (sampleSize, sampleSize))
    current=generateSimpleSample(im,sampleSize,blockSquareSize)

    allDists=[]
    for sample in samples:
        dist=0
        for i in range(0,len(sample)):
            dist+=abs(current[i]-sample[i])
        allDists.append(dist)

    return np.median(allDists)
