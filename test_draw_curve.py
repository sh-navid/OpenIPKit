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
import scripts.mathHelper as mth
from scripts.colorHelper import *
from inspect import signature

#########################################################
# Source code
#########################################################

im = cv2.imread(osh.getPath(__file__)+r'/media/im.png')

h, w = im.shape[:2]
ox, oh, cx, cy, o = w/4, h/4, w/2, h/2, (w/2)/1.6
rc = randomColor

pt1, pt2, pt3 = (ox, cy), (cx, oh), (w-ox, cy)
drw.drawMultiLine(im, [pt1, pt2, pt3], thickness=1)

slices = 10
_12 = mth.dist(pt1, pt2)//slices
_23 = mth.dist(pt2, pt3)//slices

m1, b1 = mth.lineEq(pt1, pt2)
m2, b2 = mth.lineEq(pt2, pt3)
for i in range(0, slices):
    x = int(pt1[0]+(i*_12))
    y = int(mth.calcLineY(m1, b1, x))
    cv2.circle(im, (x, y), 5, color=(120, 30, 240),
               thickness=3, lineType=cv2.LINE_AA)

cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
