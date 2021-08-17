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

dir = osh.getPath(__file__)
org = cv2.imread(dir+r'/media/im.png')

h, w = org.shape[:2]
f, ox, oh, cx, cy = 2.5, w/12, h/4, w/2, h/2
rc = randomColor

im = org.copy()

drw.drawPoly(im, [(w/f, h/f), (w-w/f, h/2), (w/2, h-h/f)], color=rc())

drw.drawHomogeneousPoly(im, (ox*3, h-oh), oh/2,
                        color=rc(), points=5, rotation=45)
drw.drawHomogeneousPoly(im, (w-ox*3, h-oh), oh/2,
                        color=rc(), points=8, thickness=2)

drw.drawTriangle(im, (ox, h/2), oh/f, color=rc(), thickness=20)
drw.drawTriangle(im, (w-ox, h/2), oh/f, color=rc(), rotation=45)

cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
##################################################################
im = org.copy()
ox = w/4

print(signature(drw.drawMultiLine))



cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
##################################################################
im = org.copy()
ox = w/4

# print(signature(drw.drawMultiLine))

drw.drawCircle(im, (cx-cx/1.6, cy), h/8, color=rc(),
               thickness=1, arc=180, rotation=0)
drw.drawCircle(im, (cx-cx/1.6, cy), h/5, color=rc(),
               thickness=10, arc=90, rotation=-90)
drw.drawCircle(im, (cx-cx/1.6, cy), h/3, color=rc(),
               thickness=45, arc=270, rotation=-180)

drw.drawCircle(im, (cx, cy), h/8, color=rc(), thickness=1)
drw.drawCircle(im, (cx, cy), h/5, color=rc(), thickness=10)
drw.drawCircle(im, (cx, cy), h/3, color=rc(), thickness=45)

drw.drawCircle(im, (cx+cx/1.6, cy), h/8, color=rc(),
               endLastLine=False, thickness=1, arc=180, rotation=0)
drw.drawCircle(im, (cx+cx/1.6, cy), h/5, color=rc(),
               endLastLine=False, thickness=10, arc=90, rotation=-90)
drw.drawCircle(im, (cx+cx/1.6, cy), h/3, color=rc(),
               endLastLine=False, thickness=45, arc=270, rotation=-180)

# drawMarker(im,(w//2,h//2))

cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
