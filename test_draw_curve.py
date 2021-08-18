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
from inspect import signature

#########################################################
# Source code
#########################################################

im = cv2.imread(osh.getPath(__file__)+r'/media/im.png')

h, w = im.shape[:2]
ox, oh, cx, cy, o = w/4, h/4, w/2, h/2, (w/2)/1.6
rc = randomColor

pt1,pt2,pt3=(ox,cy),(cx,oh),(w-ox,cy)
drw.drawMultiLine(im,[pt1,pt2,pt3],thickness=1)

cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
