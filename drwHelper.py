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
import numpy as np
import osHelper as osh

#########################################################
# Constants
#########################################################
DEFAULT_COLOR = (128, 0, 200)
DEFAULT_TICKNESS = 5
DEFAULT_MARKER = cv2.MARKER_CROSS
DEFAULT_MARKER_SIZE = DEFAULT_TICKNESS*2

#########################################################
# Functions
#########################################################


def drawMarker(im, pt, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS, markerType=DEFAULT_MARKER, markerSize=DEFAULT_MARKER_SIZE):
    cv2.drawMarker(
        im,
        pt,
        color=color,
        markerType=markerType,
        thickness=int(thickness),
        markerSize=markerSize,
        line_type=cv2.LINE_AA
    )

EXTRA_MARKER_5_POINTS_STAR=1001
def drawExtraMarkers():
    pass


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
        pt1=pt1,
        pt2=pt2,
        color=color,
        thickness={int(thickness)},
        {type}=cv2.LINE_AA
    )''')


def drawCircle():
    pass

def drawTriangle():
    pass

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

    drawLine(im, (0, 0), (w//2, h//2), hasArrow=True)
    drawPoly(im, [(0, 0), (w, h//2), (w//2, h)])

    cv2.imshow('Test', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
