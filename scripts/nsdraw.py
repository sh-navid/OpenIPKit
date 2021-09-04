from cv2 import KMEANS_RANDOM_CENTERS
import numpy as np
import scripts.nsproc as proc
import scripts.nsmath as nmth


def line(im, pt1, pt2, color=(0, 0, 0), thickness=5, aa=False):
    kt=proc.KERNEL_TYPE_CIRCULAR
    thickness = 1

    kernel = proc.kernel((thickness, thickness),
                         kerneltype=kt if aa else proc.KERNEL_TYPE_RECT)
    block = proc.merge(kernel, kernel, kernel)
    block[np.where(kernel == 1)] = color
    m, b = nmth.lineEq(pt1, pt2)
    r1 = int(thickness/2)
    r2 = thickness-r1

    dx, dy = nmth.dXY(pt1, pt2)

    def draw(x, y):
        if not aa:
            im[int(y-r1):int(y+r2), int(x-r1):int(x+r2)] = 127
        else:
            roi = im[int(y-r1):int(y+r2), int(x-r1):int(x+r2)]
            roi[np.where(kernel == 1)] = block[np.where(kernel == 1)]
            im[int(y-r1):int(y+r2), int(x-r1):int(x+r2)] = roi

    aa = False
    if abs(dx) >= abs(dy):
        for i in range(0, int(dx),1 if dx>0 else -1):
            x = pt1[0]+i
            y = pt1[1]+nmth.calcLineY(m, b, i)
            draw(x, y)
    else:
        for i in range(0, int(dy),1 if dy>0 else -1):
            y = pt1[1]+i
            x = pt1[0]+nmth.calcLineX(m, b, i)
            draw(x, y)
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
