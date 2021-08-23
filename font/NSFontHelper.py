#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import cv2
import numpy as np
import sys

#########################################################
# Source code
#########################################################

im = cv2.imread(sys.path[0]+'/NSFreeFont.png',cv2.IMREAD_GRAYSCALE)
im=cv2.threshold(im,225,255,cv2.THRESH_BINARY)[1]
im=~im

cv2.imwrite(sys.path[0]+'/NSFreeFontProcessed.png',im)