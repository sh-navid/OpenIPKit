#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import cv2
import sys
import numpy as np
from inspect import signature
import scripts.nsproc as proc
import scripts.nsdraw as draw
import scripts.nscolor as nsc

#########################################################
# Source code
#########################################################
im = cv2.imread(sys.path[0]+'/media/im.png')

im = draw.chessGrid(im)
im = draw.chessGrid(im, color1=(127,0,255),color2=(200,200,200),thickness=20)
print(signature(draw.chessGrid))

cv2.imshow('draw', im)
cv2.waitKey(0)