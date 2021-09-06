#########################################################
# Author: sh-navid
#########################################################
'''
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
import scripts.ml.nslearn as learn

#########################################################
# Source code
#########################################################
test=sys.path[0]+'/media/samples1/test'
train=sys.path[0]+'/media/samples1/train'


for i in range(1,5):
    trainList=[]
    for num in range(1,13):
        trainList.append(back.imread(train+f'/{i}/{num}.png'))
    learn.simpleCategoryLearn(trainList,8,4)

