#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import math
import numpy as np
import openipkit.nsproc as proc
import openipkit.nsmath as nmth
import openipkit.nsarray as arr

#########################################################
# Constants
#########################################################
DEFAULT_COLOR = (128, 0, 200)
DEFAULT_TICKNESS = 5
DEFAULT_MARKER_SIZE = 5
DEFAULT_ROTATION = -90
DEFAULT_ARC = 360
MULTILINE_ARROW_NONE, MULTILINE_ARROW_END, MULTILINE_MULTIPLE_ARROW = 'MLAN', 'MLAE', 'MLMA'

#########################################################
# Functions
#########################################################


def line(im: np.ndarray, pt1, pt2, color=(0, 0, 0), thickness=5,aa=True):
    '''
    '''
    t = thickness
    kType=proc.KERNEL_TYPE_CIRCULAR_EDGE_FADE if aa else proc.KERNEL_TYPE_CIRCULAR
    kernel = proc.kernel((t, t), kType)

    block = proc.merge([kernel, kernel, kernel])
    block[np.where(kernel != 0)] = color
    m, b = nmth.lineEq(pt1, pt2)
    dx, dy = nmth.dXY(pt1, pt2)
    r1 = int(t/2)
    r2 = t-r1

    # FIXME: you can make STATIC kernels and add to list every new kenel and do not make them every time
    # FIXME: optimize the AA kernel later
    # print(kernel)

    con = np.where(kernel != 0)
    def draw(x, y):
        roi = im[int(y-r1):int(y+r2), int(x-r1):int(x+r2)]
        if aa:
            for c in [0,1,2]:
                roi[:,:,c] = kernel*block[:,:,c]+(1-kernel)*roi[:,:,c]
        else:
            roi[con] = block[con]
        im[int(y-r1):int(y+r2), int(x-r1):int(x+r2)] = roi

    scale = 1
    if abs(dx) >= abs(dy):
        for i in range(0, int(dx*scale), 1 if dx > 0 else -1):
            x = pt1[0]+i/scale
            y = nmth.calcLineY(m, b, x)
            draw(x, y)
    else:
        for i in range(0, int(dy*scale), 1 if dy > 0 else -1):
            y = pt1[1]+i/scale
            x = nmth.calcLineX(m, b, y)
            draw(x, y)
    return im


def rect(im: np.ndarray):
    return im


def ellipes(im: np.ndarray):
    return im


def polygon(im: np.ndarray):
    return im


def marker(im: np.ndarray):
    return im


def vText(im: np.ndarray):
    '''
    Use vector font
    '''
    return im


def rText(im: np.ndarray):
    '''
    Use raster bitmap
    '''
    return im


def curve(im: np.ndarray):
    return im


def grid(im: np.ndarray, color1: tuple = (0, 0, 0), color2: tuple = (255, 255, 255), thickness: int = 50):
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


def hPoly(im: np.ndarray, center, radius, points=5, rotation=-DEFAULT_ROTATION, arc=DEFAULT_ARC, endLastLine=True, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
    off, angle = arc/points, rotation
    pts = []
    for i in range(0, points):
        x = radius*math.cos(math.radians(angle))
        y = radius*math.sin(math.radians(angle))
        pos = (center[0]+x, center[1]+y)
        pts.append(pos)
        angle += off
    last = pts[0]
    for i in range(1, points):
        line(im, last, pts[i], color=color, thickness=thickness)
        last = pts[i]
    if endLastLine:
        line(im, last, pts[0], color=color, thickness=thickness)


def star(im: np.ndarray, center, radius, points=5, rotation=-DEFAULT_ROTATION, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
    off, angle = 360/points, rotation
    pts = []
    for i in range(0, points):
        x = radius*math.cos(math.radians(angle))
        y = radius*math.sin(math.radians(angle))
        pos = (center[0]+x, center[1]+y)
        pts.append(pos)
        angle += off
    last, idx = pts[0], 0
    for i in range(0, points):
        idx += points-2
        if idx > points-1:
            idx -= points
        line(im, last, pts[idx], color=color, thickness=thickness)
        last = pts[idx]


def multiline(im: np.ndarray, pts, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS, arrowType=MULTILINE_ARROW_NONE):
    c1 = (arrowType == MULTILINE_MULTIPLE_ARROW)
    pts = arr.toInt2dArray(pts)
    last = pts[0]
    num = len(pts)
    for i in range(1, num):
        line(im, last, pts[i], color=color, thickness=thickness)

        c2 = (arrowType == MULTILINE_ARROW_END and i == num-1)
        if c1 or c2:
            dx, dy = nmth.dXY(last, pts[i])
            deg = math.degrees(math.atan(dy/dx))
            if dx < 0:
                deg -= 180
            end = (last[0]+(dx/2), last[1]+(dy/2)) if c1 else pts[i]
            triangle(im, end, thickness *
                     2, rotation=deg, color=color, thickness=thickness)

        last = pts[i]


def circle(im: np.ndarray, center, radius, rotation=-DEFAULT_ROTATION, arc=DEFAULT_ARC, endLastLine=True, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
    """
    DEPRECATED
    This is not optimized
    Rebuild it using x2+y2=r2 later
    """
    hPoly(im, center, radius, rotation=rotation, arc=arc,
          endLastLine=endLastLine, points=DEFAULT_ARC, color=color, thickness=thickness)


def triangle(im: np.ndarray, center, radius, rotation=-DEFAULT_ROTATION, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
    hPoly(im, center, radius, points=3, rotation=rotation,
          color=color, thickness=thickness)
