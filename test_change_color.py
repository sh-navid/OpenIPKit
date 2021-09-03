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
import scripts.drawHelper as drw
from scripts.colorHelper import *
import numpy as np

#########################################################
# Source code
#########################################################

im = cv2.imread(sys.path[0]+'/media/back.png')

h1 = changeHue(im, hue=0)
h2 = changeHue(im, hue=90)
h3 = changeHue(im, hue=160)
h4 = changeHue(im, hue=240)
h5 = changeHue(im, hue=310)

cv2.imshow('Hue', np.hstack((im, h1, h2, h3, h4, h5)))


s1 = changeSaturation(im, sat=5)
s2 = changeSaturation(im, sat=25)
s3 = changeSaturation(im, sat=50)
s4 = changeSaturation(im, sat=75)
s5 = changeSaturation(im, sat=95)


cv2.imshow('Saturation', np.hstack((im, s1, s2, s3, s4, s5)))

b1 = changeBrightness(im, val=15)
b2 = changeBrightness(im, val=35)
b3 = changeBrightness(im, val=55)
b4 = changeBrightness(im, val=75)
b5 = changeBrightness(im, val=100)


cv2.imshow('Brightness', np.hstack((im, b1, b2, b3, b4, b5)))
cv2.waitKey(0)
cv2.destroyAllWindows()
