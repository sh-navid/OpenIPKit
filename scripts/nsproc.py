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
    B, G, R = split(im)
    out = None
    if graymode == GRAY_MODE_MEAN:
        out = 0.333*R + 0.333*G + 0.333*B
    elif graymode == GRAY_MODE_GREEN:
        out = 0.2*R + 0.7*G + 0.1*B
    else:
        out = 0.3*R + 0.6*G + 0.1*B
    return np.array(out).astype(np.uint8) if conv2int else out


def gry2bgr(im):
    return merge(im, im, im)

def split(im):
    # FIXME: can you make this more global
    c1 = im[:, :, 0]
    c2 = im[:, :, 1]
    c3 = im[:, :, 2]
    return c1, c2, c3

def merge(c1, c2, c3):
    return np.dstack((c1, c2, c3))
