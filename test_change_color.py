#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import cv2
import scripts.drawHelper as drw
import scripts.osHelper as osh
from scripts.colorHelper import *
import numpy as np

#########################################################
# Source code
#########################################################

im = cv2.imread(osh.getPath(__file__)+r'/media/back.png')

h1=changeHue(im,hue=20)
h2=changeHue(im,hue=60)
h3=changeHue(im,hue=140)

cv2.imshow('Test', np.hstack((im,h1,h2,h3)))
cv2.waitKey(0)
cv2.destroyAllWindows()

