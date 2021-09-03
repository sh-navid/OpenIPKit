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

#########################################################
# Source code
#########################################################

dir = osh.getPath(__file__)
im = cv2.imread(dir+r'/media/im.png')

h, w = im.shape[:2]
cx, ch, of = w/2, h/2, h/18
rc = randomColor

drw.drawTriangle(im, (cx-cx/1.6, ch+of), ch/2, color=rc(), rotation=-90)
drw.drawTriangle(im, (cx, ch-of), ch/2, color=rc(), rotation=-45, thickness=15)
drw.drawTriangle(im, (cx+cx/1.6, ch-of), ch/2, color=rc(), thickness=30)

cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
