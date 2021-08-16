#########################################################
# Author: sh-navid
#########################################################

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

#########################################################
# Functions
#########################################################

def drawMarker(im, pos, color=(128, 0, 255)):
    return cv2.drawMarker(
        im,
        pos,
        color=color,
        markerType=cv2.MARKER_TRIANGLE_DOWN,
        thickness=5,
        markerSize=40,
        line_type=cv2.LINE_AA,
    )


def drawPoly(im, points, color=(128, 0, 200), thickness=10):
    return cv2.polylines(
        im,
        pts=[np.int32(points)],
        isClosed=True,
        color=color,
        thickness=thickness,
        lineType=cv2.LINE_AA,  # Anti-Aliased
    )

def drawLine(im, pt1, pt2, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS, hasArrow=False):
    fn = cv2.line if not hasArrow else cv2.arrowedLine
    type = 'lineType' if not hasArrow else 'line_type'
    return eval(f'''fn(
        im,
        pt1=pt1,
        pt2=pt2,
        color=color,
        thickness=thickness,
        {type}=cv2.LINE_AA
    )''')


def drawCircle():
    pass


def drawCurve(pt1, pt2, pt3, pt4):
    # https://en.wikipedia.org/wiki/B%C3%A9zier_curve
    pass


if __name__ == '__main__':
    print('unit tests')
    dir = osh.getRoot(__file__)

    im = cv2.imread(dir+r'/media/im.png')
    h, w = im.shape[:2]

    im = drawLine(im, (0, 0), (w//2, h//2),hasArrow=True)
    
    cv2.imshow('Test',im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
