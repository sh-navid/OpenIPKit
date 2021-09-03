import cv2
import sys
import numpy as np
import scripts.nsproc as proc

im = cv2.imread(sys.path[0]+'/media/back.png')

gry1 = proc.bgr2gry(im, proc.GRAY_MODE_MEAN)
gry2 = proc.bgr2gry(im, proc.GRAY_MODE_GREEN)
gry3 = proc.bgr2gry(im, proc.GRAY_MODE_BLUE_GREEN)

gry1 = proc.gry2bgr(gry1)
gry2 = proc.gry2bgr(gry2)
gry3 = proc.gry2bgr(gry3)

print(im)

cv2.imshow('proc', np.hstack((im/255, gry1/255, gry2/255, gry3/255)))
cv2.waitKey(0)
