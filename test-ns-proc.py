import cv2
import sys
import numpy as np
import scripts.nsproc as proc

im = cv2.imread(sys.path[0]+'/media/back.png')

gry1 = proc.bgr2gry(im, proc.GRAY_MODE_MEAN)
gry2 = proc.bgr2gry(im, proc.GRAY_MODE_GREEN)
gry3 = proc.bgr2gry(im, proc.GRAY_MODE_BLUE_GREEN)

print(im)
print(gry1)

cv2.imshow('proc', np.hstack((im,gry1/255, gry2/255, gry3/255)))
cv2.waitKey(0)
