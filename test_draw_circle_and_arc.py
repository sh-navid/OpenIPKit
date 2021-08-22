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

im = cv2.imread(osh.getPath(__file__)+r'/media/im.png')

h, w = im.shape[:2]
ox, oh, cx, cy, o = w/4, h/4, w/2, h/2, (w/2)/1.6
rc = randomColor

drw.drawCircle(im, (cx-o, cy), h/14, color=rc(), thickness=2, arc=180, rotation=0)
drw.drawCircle(im, (cx-o, cy), h/7, color=rc(), thickness=10, arc=90, rotation=-90)
drw.drawCircle(im, (cx-o, cy), h/4, color=rc(), thickness=25, arc=270, rotation=-180)

drw.drawCircle(im, (cx, cy), h/14, color=rc(), thickness=2)
drw.drawCircle(im, (cx, cy), h/7, color=rc(), thickness=10)
drw.drawCircle(im, (cx, cy), h/4, color=rc(), thickness=25)

drw.drawCircle(im, (cx+o, cy), h/14, color=rc(), endLastLine=False, thickness=2, arc=180, rotation=0)
drw.drawCircle(im, (cx+o, cy), h/7, color=rc(), endLastLine=False, thickness=10, arc=90, rotation=-90)
drw.drawCircle(im, (cx+o, cy), h/4, color=rc(), endLastLine=False, thickness=25, arc=270, rotation=-180)


cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
