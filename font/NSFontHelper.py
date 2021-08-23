#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import cv2
import numpy as np
import sys

#########################################################
# Source code
#########################################################

im = cv2.imread(sys.path[0]+'/NSFreeFont.png', cv2.IMREAD_GRAYSCALE)
im = cv2.threshold(im, 225, 255, cv2.THRESH_BINARY)[1]
im = ~im

H, W = im.shape[:2]

downscale = 7
im = cv2.resize(im, (W//downscale, H//downscale))
H, W = im.shape[:2]
im = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)[1]


ROWS, COLS = 7, 6
SW = W/COLS
SH = H/ROWS


class Ch:
    def __init__(self, xi, yi, ch):
        self.xi = xi
        self.yi = yi
        self.ch = ch


elements = {
    Ch(0, 0, 'A'), Ch(1, 0, 'B'), Ch(2, 0, 'C'), Ch(
        3, 0, 'D'), Ch(4, 0, 'E'), Ch(5, 0, 'F'),
    Ch(0, 1, 'G'), Ch(1, 1, 'H'), Ch(2, 1, 'I'), Ch(
        3, 1, 'J'), Ch(4, 1, 'K'), Ch(5, 1, 'L'),
    Ch(0, 2, 'M'), Ch(1, 2, 'N'), Ch(2, 2, 'O'), Ch(
        3, 2, 'P'), Ch(4, 2, 'Q'), Ch(5, 2, 'R'),
    Ch(0, 3, 'S'), Ch(1, 3, 'T'), Ch(2, 3, 'U'), Ch(
        3, 3, 'V'), Ch(4, 3, 'W'), Ch(5, 3, 'X'),
    Ch(0, 4, 'Y'), Ch(1, 4, 'Z'), Ch(2, 4, '.'), Ch(
        3, 4, ':'), Ch(4, 4, ';'), Ch(5, 4, ','),
    Ch(0, 5, '0'), Ch(1, 5, '1'), Ch(2, 5, '2'), Ch(
        3, 5, '3'), Ch(4, 5, '4'), Ch(5, 5, '5'),
    Ch(0, 6, '6'), Ch(1, 6, '7'), Ch(2, 6, '8'), Ch(
        3, 6, '9'), Ch(4, 6, '-'), Ch(5, 6, '+'),
}

dictList = {}
for el in elements:
    dictList[el.ch] = {'xi': el.xi, 'yi': el.yi}

print(dictList)

for yi in range(0, ROWS):
    for xi in range(0, COLS):
        pt1 = (int(xi*SW), int(yi*SH))
        pt2 = (int(xi*SW+SW), int(yi*SH+SH))
        cv2.rectangle(im, pt1, pt2, (0, 255, 0), 1)

im=cv2.cvtColor(im,cv2.COLOR_GRAY2BGR)
cv2.imwrite(sys.path[0]+'/NSFreeFontProcessed.png', im)


def drawNSFreeFont(im2, pos, text):
    l = 0
    for c in text:
        ptr = dictList[c]
        if ptr == None:
            ptr = dictList['-']
        x = ptr['xi']*SW
        y = ptr['yi']*SH
        Y = pos[1]+y
        X = pos[0]+l+x
        im2[int(Y):int(Y+SH), int(X):int(X+SW)] = im[int(y):int(y+SH), int(l+x):int(l+x+SW)]
        l += SW


myIm = 255 * np.ones((300, 300, 3), dtype=np.uint8)
drawNSFreeFont(myIm, (20, 20), "TEST123")

cv2.imshow('test', myIm)
cv2.waitKey(0)
