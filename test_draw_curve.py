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

pt1, pt2, pt3 = (ox, h-h/8), (cx, oh), (w-ox, h-h/8)
drw.drawMultiLine(im, [pt1, pt2, pt3], thickness=1)

slices = 8
d12 = mth.dist(pt1, pt2)/slices
d23 = mth.dist(pt2, pt3)/slices

m1, b1 = mth.lineEq(pt1, pt2)
m2, b2 = mth.lineEq(pt2, pt3)
for i in range(0, slices):
    x1 = int(pt1[0]+(i*d12))
    y1 = int(mth.calcLineY(m1, b1, x1))
    cv2.circle(im, (x1, y1), 2, color=(160, 20, 255),
               thickness=2, lineType=cv2.LINE_AA)

    x2 = int(pt2[0]+(i*d23))
    y2 = int(mth.calcLineY(m2, b2, x2))
    cv2.circle(im, (x2, y2), 2, color=(160, 20, 255),
               thickness=2, lineType=cv2.LINE_AA)

    drw.drawMultiLine(im, [(x1, y1), (x2, y2)], thickness=1 ,color=(200,30,100))

cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
