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
H, W = im.shape[:2]
rc = nsc.randomColor
im = draw.line(im, (10, 10), (W-10, H-10), color=rc(), thickness=2, aa=True) #TRUE
im = draw.line(im, (W-50, H-50), (50, 50), color=rc(), thickness=3, aa=True) #TRUE

im = draw.line(im, (W//2, 10), (W-10, H-10),color=rc(), thickness=4, aa=True)
im = draw.line(im, (W-50, 10), (W-10, H-10),color=rc(), thickness=6, aa=True)
im = draw.line(im, (W-20, 10), (W-10, H-10),color=rc(), thickness=8, aa=True)
im = draw.line(im, (W-10, 10), (W-10, H-10),color=rc(), thickness=10, aa=True)
im = draw.line(im, (W-10, 10), (10, H-10),color=rc(), thickness=12, aa=True)
im = draw.line(im, (10, 10), (10, H-10),color=rc(), thickness=16, aa=True)
im = draw.line(im, (10, 10), (W-10, 10),color=rc(), thickness=18, aa=True)
cv2.imshow('draw', im)
cv2.waitKey(0)

##############################################################################
im = cv2.imread(sys.path[0]+'/media/im.png')

h, w = im.shape[:2]
ox, oh, cx, cy, o = w/4, h/4, w/2, h/2, (w/2)/1.6
rc = nsc.randomColor

#paint.circle(im, (cx-o, cy), h/14, color=rc(), thickness=2, arc=180, rotation=0)
#paint.circle(im, (cx-o, cy), h/7, color=rc(), thickness=10, arc=90, rotation=-90)
#paint.circle(im, (cx-o, cy), h/4, color=rc(), thickness=25, arc=270, rotation=-180)
#paint.circle(im, (cx, cy), h/14, color=rc(), thickness=2)
#paint.circle(im, (cx, cy), h/7, color=rc(), thickness=10)
#paint.circle(im, (cx, cy), h/4, color=rc(), thickness=25)
#paint.circle(im, (cx+o, cy), h/14, color=rc(), endLastLine=False, thickness=2, arc=180, rotation=0)
#paint.circle(im, (cx+o, cy), h/7, color=rc(), endLastLine=False, thickness=10, arc=90, rotation=-90)
#paint.circle(im, (cx+o, cy), h/4, color=rc(), endLastLine=False, thickness=25, arc=270, rotation=-180)

#paint.star(im, (cx, cy), oh, points=5)
#
#cv2.imshow('draw', im)
# cv2.waitKey(0)
