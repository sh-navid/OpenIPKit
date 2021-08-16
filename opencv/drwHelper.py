#########################################################
# Author: sh-navid
#########################################################

#########################################################
# Add preprocessors
#########################################################
import os
import cv2

def line(im, start, end, color=(128, 0, 200), thickness=5):
    return cv2.line(
        im,
        pt1=(start[0], start[1]),
        pt2=(end[0], end[1]),
        color=color,
        thickness=thickness,
        lineType=cv2.LINE_AA,  # Anti-Aliased
    )

# https://en.wikipedia.org/wiki/B%C3%A9zier_curve
def drawCurve(pt1,pt2,pt3,pt4):
    pass