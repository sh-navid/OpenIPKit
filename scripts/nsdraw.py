import numpy as np
import scripts.nsproc as proc
import scripts.nsmath as math


def line(im, pt1, pt2, color=(0, 0, 0), thickness=5):
    k = proc.kernel((thickness, thickness), proc.KERNEL_TYPE_CIRCULAR)
    print(k)
    k = proc.merge(k, k, k)
    k[np.where(k[:, :, 0] == 1)] = color
    m, b = math.lineEq(pt1, pt2)
    dist = math.dist(pt1, pt2)
    rad = thickness//2
    for i in range(0, math.absDXY(pt1,pt2)[0],2):
        x = pt1[0]+i
        y = pt1[1]+int(math.calcLineY(m, b, x))
        im[y-rad:y-rad+thickness, x-rad:x-rad+thickness] = k
    return im


def rect(im):
    return im


def ellipes(im):
    return im


def circle(im):
    return im


def hPolygon(im):
    return im


def polygon(im):
    return im


def multiline(im):
    return im


def marker(im):
    return im


def vText(im):
    '''
    Use vector font
    '''
    return im


def rText(im):
    '''
    Use raster bitmap
    '''
    return im


def curve(im):
    return im


def triangle(im):
    return im


def star(im):
    return im


def chessGrid(im: np.ndarray, color1: tuple = (0, 0, 0), color2: tuple = (255, 255, 255), thickness: int = 50):
    '''
    '''
    # FIXME: check this in different sizes; does not work sometimes
    k = proc.kernel((thickness, thickness), proc.KERNEL_TYPE_RECT)
    h, w = im.shape[:2]
    nh, nw = h//thickness, w//thickness
    im[:] = color2
    paint = True
    for hh in range(0, nh+1):
        for ww in range(0, nw+1):
            paint = not paint
            if paint:
                continue
            y = hh*thickness
            x = ww*thickness
            im[y:y+thickness, x:x+thickness] = color1
    return im
