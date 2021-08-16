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
import osHelper as osh

#########################################################
# Constants
#########################################################
DEFAULT_COLOR = (128, 0, 200)
DEFAULT_TICKNESS = 5
DEFAULT_MARKER = cv2.MARKER_CROSS
DEFAULT_MARKER_SIZE = 5

#########################################################
# Functions
#########################################################


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


def drawStar(im, center, radius, points=5, rotation=-90, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
    off, deg = 360/points, rotation
    pts = []
    for i in range(0, points):
        x = radius*math.cos(math.radians(deg))
        y = radius*math.sin(math.radians(deg))
        pos = (center[0]+x, center[1]+y)
        pts.append(pos)
        deg += off
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
    pt1 = [int(x) for x in pt1]
    pt2 = [int(x) for x in pt2]
    fn = cv2.line if not hasArrow else cv2.arrowedLine
    type = 'lineType' if not hasArrow else 'line_type'
    eval(f'''fn(
        im,
        pt1={pt1},
        pt2={pt2},
        color={color},
        thickness={int(thickness)},
        {type}=cv2.LINE_AA
    )''')


def drawCircle():
    pass


def drawTriangle(im, center, radius, rotation=-90, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS):
    drawStar(im, center, radius, points=3, rotation=rotation,
             color=color, thickness=thickness)


def drawRect():
    pass


def drawSquare():
    pass


def drawOval():
    pass


def drawCurve(pt1, pt2, pt3, pt4):
    # https://en.wikipedia.org/wiki/B%C3%A9zier_curve
    pass


#########################################################
# Tests
#########################################################
if __name__ == '__main__':
    print('unit tests')
    dir = osh.getRoot(__file__)

    im = cv2.imread(dir+r'/media/im.png')
    h, w = im.shape[:2]

    # drawLine(im, (0, 0), (w//2, h//2), hasArrow=True)
    # drawPoly(im, [(0, 0), (w, h//2), (w//2, h)])

    drawStar(im, (w//4, h//4), w//8, color=(200, 100, 220))
    drawStar(im, (w-w//4, h//4), w//8, color=(150, 100, 220), points=7)

    drawStar(im, (w//4, h-h//4), w//8, color=(41, 100, 220), points=9)
    drawStar(im, (w-w//4, h-h//4), w//8, color=(41, 200, 50), points=11,thickness=15)

    drawTriangle(im, (w//4, h//2), w//12, color=(50, 10, 220),thickness=20)
    drawTriangle(im, (w-w//4, h//2), w//12, color=(220, 50, 100), rotation=45)

    cv2.imshow('Test', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
