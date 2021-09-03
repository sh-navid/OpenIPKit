import cv2
import sys
import numpy as np
import scripts.nsproc as proc
import scripts.nsdraw as draw
from inspect import signature

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
im = cv2.imread(sys.path[0]+'/media/im.png')
im = draw.chessGrid(im)
#im = draw.chessGrid(im, color1=(127,0,255),color2=(200,200,200),thickness=80)
#print(signature(draw.chessGrid))

cv2.imshow('draw', im)
cv2.waitKey(0)
