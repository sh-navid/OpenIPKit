#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import sys
sys.path.append('.')
import openipkit.nssys as nss
import openipkit.nsmath as nmth
import openipkit.nsproc as proc
import openipkit.nsdraw as draw
import openipkit.nscolor as nsc
import openipkit.backend as back
import openipkit.ml.nslearn as learn

#########################################################
# Source code
#########################################################
im = back.imread(sys.path[0]+'/media/im.png')

def run():
    h, w = im.shape[:2]
    ox, oh, cx, cy, o = w/4, h/4, w/2, h/2, (w/2)/1.6
    rc = nsc.randomColor

    pt1, pt2, pt3 = (ox, h-h/8), (cx, oh), (w-ox, h-h/8)
    draw.multiline(im, [pt1, pt2, pt3], thickness=5)

    slices = 8
    d12 = nmth.dist(pt1, pt2)/slices
    d23 = nmth.dist(pt2, pt3)/slices

    m1, b1 = nmth.lineEq(pt1, pt2)
    m2, b2 = nmth.lineEq(pt2, pt3)
    for i in range(0, slices-1):
        x1 = int(pt1[0]+(i*d12))
        y1 = int(nmth.calcLineY(m1, b1, x1))
        #cv2.circle(im, (x1, y1), 2, color=(160, 20, 255),
        #           thickness=2, lineType=cv2.LINE_AA)

        x2 = int(pt2[0]+(i*d23))
        y2 = int(nmth.calcLineY(m2, b2, x2))
        #cv2.circle(im, (x2, y2), 2, color=(160, 20, 255),
        #           thickness=2, lineType=cv2.LINE_AA)

        draw.multiline(im, [(x1, y1), (x2, y2)],
                          thickness=5, color=(200, 30, 100))

nss.execMonitor(run,True)
back.imshow('Test', im)