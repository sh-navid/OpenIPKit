#########################################################
# Author: sh-navid
#########################################################

#########################################################
# Add preprocessors
#########################################################
import os
import cv2

DEFAULT_COLOR = (128, 0, 200)
DEFAULT_TICKNESS = 5


def line(im, pt1, pt2, color=DEFAULT_COLOR, thickness=DEFAULT_TICKNESS, hasArrow=False):
    fn = cv2.line if not hasArrow else cv2.arrowedLine
    return fn(
        im,
        pt1=pt1,
        pt2=pt2,
        color=color,
        thickness=thickness,
        lineType=cv2.LINE_AA  # Anti-Aliased
    )


def drawCurve(pt1, pt2, pt3, pt4):
    # https://en.wikipedia.org/wiki/B%C3%A9zier_curve
    pass
