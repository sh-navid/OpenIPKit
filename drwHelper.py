#########################################################
# Author: sh-navid
#########################################################

#########################################################
# Add preprocessors
#########################################################
import os
import cv2
import osHelper as osh

#########################################################
# Constants
#########################################################
DEFAULT_COLOR = (128, 0, 200)
DEFAULT_TICKNESS = 5

#########################################################
# Functions
#########################################################


def line(im, pt1, pt2, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS, hasArrow=False):
    fn = cv2.line if not hasArrow else cv2.arrowedLine
    type = 'lineType' if not hasArrow else 'line_type'
    return eval(f'''{fn}(
        {im},
        pt1={pt1},
        pt2={pt2},
        color={color},
        thickness={thickness},
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
    print(dir)
