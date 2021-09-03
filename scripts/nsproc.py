import numpy as np


def fill(im, pos=(0, 0), color=(0, 0, 0), diff=0):
    pass


def tresh_channel(im, thresh, channel=0):
    im[np.where(im[:, :, channel] < thresh)] = 0
    im[np.where(im[:, :, channel] >= thresh)] = 255
    return im


def tresh_simple(im, thresh):
    im[np.where(im < thresh)] = 0
    im[np.where(im >= thresh)] = 255
    return im


GRAY_MODE_MEAN = 1
GRAY_MODE_GREEN = 2
GRAY_MODE_BLUE_GREEN = 3


def bgr2gry(im, graymode=GRAY_MODE_MEAN, conv2int=False):
    B = im[:, :, 0]
    G = im[:, :, 1]
    R = im[:, :, 2]
    out = None
    if graymode == GRAY_MODE_MEAN:
        out = 0.333*R + 0.333*G + 0.333*B
    elif graymode == GRAY_MODE_BLUE_GREEN:
        out = 0.2126*R + 0.7152*G + 0.0722*B
    else:
        out = 0.299*R + 0.587*G + 0.114*B
    return np.array(out).astype(int) if conv2int else out

def split(im):
    c1 = im[:, :, 0]
    c2 = im[:, :, 1]
    c3 = im[:, :, 2]
    return c1,c2,c3