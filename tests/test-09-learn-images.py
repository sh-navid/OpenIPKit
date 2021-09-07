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
test = sys.path[0]+'/media/samples1/test'
train = sys.path[0]+'/media/samples1/train'

models = []
for trainSetIdx in range(1, 5):
    trainList = []
    for tainSampleNum in range(1, 13):
        trainList.append(back.imread(
            train+f'/{trainSetIdx}/{tainSampleNum}.png'))
    model = learn.simpleLearn(trainList, 32, 16)#32-8
    models.append(model)

for testIdx in range(1, 5):
    im = back.imread(test+f'/{testIdx}.png')
    print()
    for modelIdx in range(1, 5):
        distBetweenModelAndTestSample = learn.simpleDetect(im, models[modelIdx-1])
        print(f'Testcase of number {testIdx} --- can be number {modelIdx}: {distBetweenModelAndTestSample}')
