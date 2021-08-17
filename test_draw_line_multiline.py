import cv2
import scripts.drawHelper as drw
import scripts.osHelper as osh
from scripts.colorHelper import *

#########################################################
# Source code
#########################################################

dir = osh.getPath(__file__)
im = cv2.imread(dir+r'/media/im.png')

h, w = im.shape[:2]
cx, ch = w/2, h/2
rc = randomColor

drw.drawLine(im, (60, 303), (151, 40), color=rc(), hasArrow=True)

drw.drawLine(im, (240, 307), (330, 40), color=rc(), hasArrow=False)

x = 0
pts = [(418+x, 303), (461+x, 195),  (539+x, 140), (520+x, 40)]
drw.drawMultiLine(im, pts, color=rc(), arrowType=drw.MULTILINE_ARROW_NONE)

x = 205
pts = [(418+x, 303), (461+x, 195),  (539+x, 140), (520+x, 40)]
drw.drawMultiLine(im, pts, color=rc(), arrowType=drw.MULTILINE_ARROW_END)

x = 410
pts = [(418+x, 303), (461+x, 195),  (539+x, 140), (520+x, 40)]
drw.drawMultiLine(im, pts, color=rc(), arrowType=drw.MULTILINE_MULTIPLE_ARROW)


cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
