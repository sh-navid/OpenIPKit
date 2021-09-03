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
import scripts.nsproc as proc
import scripts.nsmath as math

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

# Fixme: this is buggy; fix it


def homogeneousPoly(im, center, radius, points=5, rotation=-DEFAULT_ROTATION, arc=DEFAULT_ARC, endLastLine=True, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
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
        drawLine(im, last, pts[i], color=color, thickness=thickness)
        last = pts[i]
    if endLastLine:
        drawLine(im, last, pts[0], color=color, thickness=thickness)


def star(im, center, radius, points=5, rotation=-DEFAULT_ROTATION, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
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
        drawLine(im, last, pts[idx], color=color, thickness=thickness)
        last = pts[idx]


def multiline(im, pts, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS, arrowType=MULTILINE_ARROW_NONE):
    c1 = (arrowType == MULTILINE_MULTIPLE_ARROW)
    pts = arh.toInt2dArray(pts)
    last = pts[0]
    num = len(pts)
    for i in range(1, num):
        drawLine(im, last, pts[i], color=color, thickness=thickness)

        c2 = (arrowType == MULTILINE_ARROW_END and i == num-1)
        if c1 or c2:
            dx, dy = mth.dXY(last, pts[i])
            deg = math.degrees(math.atan(dy/dx))
            if dx < 0:
                deg -= 180
            end=(last[0]+(dx/2), last[1]+(dy/2)) if c1 else pts[i]
            triangle(im, end, thickness *
                         2, rotation=deg, color=color, thickness=thickness)

        last = pts[i]


def circle(im, center, radius, rotation=-DEFAULT_ROTATION, arc=DEFAULT_ARC, endLastLine=True, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
    # I think this function is not optimized; for now its better to use OpenCV builtin function
    homogeneousPoly(im, center, radius, rotation=rotation, arc=arc,
                        endLastLine=endLastLine, points=DEFAULT_ARC, color=color, thickness=thickness)


def triangle(im, center, radius, rotation=-DEFAULT_ROTATION, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
    homogeneousPoly(im, center, radius, points=3, rotation=rotation,
                        color=color, thickness=thickness)