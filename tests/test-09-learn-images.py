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
#Train Models
for tSet in range(1, 5):
    imList = [back.imread(train+f'/{tSet}/{tId}.png') for tId in range(1, 13)]
    model = learn.simpleLearn(imList, 32, 16)#32-8
    models.append(model)

#Test Models
for tId in range(1, 5):
    im = back.imread(test+f'/{tId}.png')
    print()
    for mId in range(1, 5):
        dist = learn.simpleDetect(im, models[mId-1])
        print(f'Testcase of number {tId} --- can be number {mId}: {dist}')
