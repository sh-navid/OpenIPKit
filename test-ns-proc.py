import cv2
import sys
import numpy as np
from inspect import signature
import scripts.nsproc as proc
import scripts.nsdraw as draw
import scripts.nscolor as nsc
import scripts.nspaint as paint

im = cv2.imread(sys.path[0]+'/media/back.png')

gry1 = proc.toGray(im, proc.GRAY_MODE_A)
gry2 = proc.toGray(im, proc.GRAY_MODE_B)
gry3 = proc.toGray(im, proc.GRAY_MODE_C)

gry1 = proc.toBGR(gry1)
gry2 = proc.toBGR(gry2)
gry3 = proc.toBGR(gry3)

bw = proc.treshSimple(gry3, 240)

#cv2.imshow('proc', np.hstack((im/255, gry1/255, gry2/255, gry3/255, bw/255)))
# cv2.waitKey(0)

##############################################################################
# im = cv2.imread(sys.path[0]+'/media/im.png')
# im = draw.chessGrid(im)
# im = draw.chessGrid(im, color1=(127,0,255),color2=(200,200,200),thickness=20)
# print(signature(draw.chessGrid))
# cv2.imshow('draw', im)
# cv2.waitKey(0)

##############################################################################
im = cv2.imread(sys.path[0]+'/media/im.png')
im = draw.line(im,(10,10),(200,200),color=(127,0,255),thickness=21,aa=True)
im = draw.line(im,(100,10),(200,200),color=(127,255,50),thickness=11,aa=True)
cv2.imshow('draw', im)
cv2.waitKey(0)

##############################################################################
im = cv2.imread(sys.path[0]+'/media/im.png')

h, w = im.shape[:2]
ox, oh, cx, cy, o = w/4, h/4, w/2, h/2, (w/2)/1.6
rc = nsc.randomColor

paint.circle(im, (cx-o, cy), h/14, color=rc(), thickness=2, arc=180, rotation=0)
paint.circle(im, (cx-o, cy), h/7, color=rc(), thickness=10, arc=90, rotation=-90)
paint.circle(im, (cx-o, cy), h/4, color=rc(), thickness=25, arc=270, rotation=-180)
paint.circle(im, (cx, cy), h/14, color=rc(), thickness=2)
paint.circle(im, (cx, cy), h/7, color=rc(), thickness=10)
paint.circle(im, (cx, cy), h/4, color=rc(), thickness=25)
paint.circle(im, (cx+o, cy), h/14, color=rc(), endLastLine=False, thickness=2, arc=180, rotation=0)
paint.circle(im, (cx+o, cy), h/7, color=rc(), endLastLine=False, thickness=10, arc=90, rotation=-90)
paint.circle(im, (cx+o, cy), h/4, color=rc(), endLastLine=False, thickness=25, arc=270, rotation=-180)

cv2.imshow('draw', im)
cv2.waitKey(0)
