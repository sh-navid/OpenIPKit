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
cx, ch = w/2, h/2
rc = randomColor

drw.drawStar(im, (cx-cx/1.6, ch), ch/2, color=rc(), rotation=-90)
drw.drawStar(im, (cx, ch), ch/2, color=rc(), rotation=-90, thickness=10, points=9)
drw.drawStar(im, (cx+cx/1.6, ch), ch/2, color=rc(), points=15, thickness=30)


cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
