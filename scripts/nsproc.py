import numpy as np


def fill(im, pos=(0, 0), color=(0, 0, 0), diff=0):
    pass


def treshChannel(im, thresh, channel=0):
    im = im.copy()
    im[np.where(im[:, :, channel] < thresh)] = 0
    im[np.where(im[:, :, channel] >= thresh)] = 255
    return im


def treshSimple(im, thresh):
    im = im.copy()
    im[np.where(im < thresh)] = 0
    im[np.where(im >= thresh)] = 255
    return im


GRAY_MODE_A = 1
GRAY_MODE_B = 2
GRAY_MODE_C = 3


def toGray(im, graymode=GRAY_MODE_A, floatmode=True):
    b, g, r = split(im)
    out = None
    if graymode == GRAY_MODE_A:
        out = 0.3*r + 0.3*g + 0.4*b
    elif graymode == GRAY_MODE_B:
        out = 0.2*r + 0.7*g + 0.1*b
    else:
        out = 0.3*r + 0.6*g + 0.1*b
    return np.array(out).astype(np.uint8) if not floatmode else out


def toBGR(im):
    return merge(im, im, im)


def split(im):
    # FIXME: can you make this more global
    c1 = im[:, :, 0]
    c2 = im[:, :, 1]
    c3 = im[:, :, 2]
    return c1, c2, c3


def merge(c1, c2, c3):
    return np.dstack((c1, c2, c3))


def tinning(im):
    pass


def ticking(im):
    pass


KERNEL_TYPE_RECT = 1


def kernel(size: tuple, kerneltype: int = KERNEL_TYPE_RECT):
    if kerneltype == KERNEL_TYPE_RECT:
        return np.ones(size)
    return None
