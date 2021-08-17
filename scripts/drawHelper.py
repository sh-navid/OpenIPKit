#########################################################
# Author: sh-navid
#########################################################
'''
I want to add more functionality to opencv
'''
#########################################################
# Add preprocessors
#########################################################
import cv2
import math
import numpy as np
import scripts.osHelper as osh
import scripts.arrayHelper as arh

#########################################################
# Constants
#########################################################
DEFAULT_COLOR = (128, 0, 200)
DEFAULT_TICKNESS = 5
DEFAULT_MARKER = cv2.MARKER_CROSS
DEFAULT_MARKER_SIZE = 5
DEFAULT_ROTATION=-90
DEFAULT_ARC=360

MULTILINE_ARROW_NONE, MULTILINE_ARROW_END, MULTILINE_MULTIPLE_ARROW = 'MLAN', 'MLAE', 'MLMA'

#########################################################
# Functions
#########################################################

# Fixme: this is buggy; fix it


def drawMarker(im, pt, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS, markerType=DEFAULT_MARKER, markerSize=DEFAULT_MARKER_SIZE):
    cv2.drawMarker(
        im,
        pos=pt,
        color=color,
        markerType=markerType,
        thickness=int(thickness),
        markerSize=markerSize,
        line_type=cv2.LINE_AA
    )


def drawHomogeneousPoly(im, center, radius, points=5, rotation=-DEFAULT_ROTATION, arc=DEFAULT_ARC, endLastLine=True, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
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


def drawStar(im, center, radius, points=5, rotation=-DEFAULT_ROTATION, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
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


def drawPoly(im, pts, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
    cv2.polylines(
        im,
        pts=[np.int32(pts)],
        isClosed=True,
        color=color,
        thickness=int(thickness),
        lineType=cv2.LINE_AA
    )


def drawLine(im, pt1, pt2, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS, hasArrow=False):
    fn = cv2.line if not hasArrow else cv2.arrowedLine
    type = 'lineType' if not hasArrow else 'line_type'
    eval(f'''fn(
        im,
        pt1={arh.toInt1dArray(pt1)},
        pt2={arh.toInt1dArray(pt2)},
        color={color},
        thickness={int(thickness)},
        {type}=cv2.LINE_AA
    )''')


def drawMultiLine(im, pts, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS, arrowType=MULTILINE_ARROW_NONE):
    pts = arh.toInt2dArray(pts)
    last = pts[0]
    num = len(pts)
    for i in range(1, num):
        drawLine(im, last, pts[i], color=color, thickness=thickness, hasArrow=(
            (arrowType == MULTILINE_MULTIPLE_ARROW)
            or
            (arrowType == MULTILINE_ARROW_END and i == num-1)
        ))
        last = pts[i]


def drawCircle(im, center, radius, rotation=-DEFAULT_ROTATION, arc=DEFAULT_ARC, endLastLine=True, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
    # I think this function is not optimized; for now its better to use OpenCV builtin function
    drawHomogeneousPoly(im, center, radius, rotation=rotation, arc=arc,
        endLastLine=endLastLine, points=DEFAULT_ARC, color=color, thickness=thickness)


def drawTriangle(im, center, radius, rotation=-DEFAULT_ROTATION, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
    drawHomogeneousPoly(im, center, radius, points=3, rotation=rotation,
        color=color, thickness=thickness)


def drawRectFromCenter():
    pass


def drawRectFromTopLeft():
    pass


def drawSquareFromCenter():
    pass


def drawSquareFromTopLeft():
    pass


def drawOval():
    pass


def drawCurve(pt1, pt2, pt3, pt4):
    # https://en.wikipedia.org/wiki/B%C3%A9zier_curve
    # For now just draw over 3 points
    pass
