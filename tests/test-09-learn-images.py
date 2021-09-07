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
test = sys.path[0]+'/media/samples1/test'
train = sys.path[0]+'/media/samples1/train'

models = []
for trainSetIdx in range(1, 5):
    trainList = []
    for tainSampleNum in range(1, 13):
        trainList.append(back.imread(
            train+f'/{trainSetIdx}/{tainSampleNum}.png'))
    model = learn.simpleCategoryLearn(trainList, 32, 16)#32-8
    models.append(model)

for testIdx in range(1, 5):
    im = back.imread(test+f'/{testIdx}.png')
    print()
    for modelIdx in range(1, 5):
        distBetweenModelAndTestSample = learn.simpleCategoryDetect(im, models[modelIdx-1])
        print(f'Testcase of number {testIdx} --- can be number {modelIdx}: {distBetweenModelAndTestSample}')
