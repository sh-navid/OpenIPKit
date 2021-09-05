#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import sys
import numpy as np
import scripts.backend as back

#########################################################
# Source code
#########################################################

im = back.imread(sys.path[0]+'/NSFreeFont.png')
H, W = im.shape[:2]

downscale = 5
im = back.resize(im, (W//downscale, H//downscale))
H, W = im.shape[:2]

ROWS, COLS = 7, 6
SW = W/COLS
SH = H/ROWS


class Ch:
    def __init__(self, xi, yi, ch):
        self.xi = xi
        self.yi = yi
        self.ch = ch


rawList = [
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
]

dictList = {}
for el in rawList:
    dictList[el.ch] = {'xi': el.xi, 'yi': el.yi}

for yi in range(0, ROWS):
    for xi in range(0, COLS):
        pt1 = (int(xi*SW), int(yi*SH))
        pt2 = (int(xi*SW+SW), int(yi*SH+SH))

back.imwrite(sys.path[0]+'/NSFreeFontProcessed.png', im)

def drawNSFreeFont(im2, pos, text):
    l = 0
    for c in text:
        ptr = None
        try:
            ptr = dictList[c]
        except:
            ptr = dictList['-']
        x = int(ptr['xi']*SW)
        y = int(ptr['yi']*SH)
        Y = int(pos[1])
        X = int(pos[0]+l)
        SHI, SWI = int(SH), int(SW)
        im2[Y:Y+SHI, X:X+SWI] = im[y:y+SHI, x:x+SWI]
        l += SWI


myIm = 127 * np.ones((300, 300, 3), dtype=np.uint8)
drawNSFreeFont(myIm, (20, 130), "ORIGINAL")

back.imshow('test', myIm)