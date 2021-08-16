# PyHelper
This module a set of helper functions for OpenCV, ImageProcessing, CV and Python.

## Draw Functions
### Draw Star and Triangle

~~~python
import cv2
import scripts.drawHelper as drw
import scripts.osHelper as osh
from scripts.colorHelper import *

dir = osh.getPath(__file__)
im = cv2.imread(dir+r'/media/im.png')

h, w = im.shape[:2]
f, ox, oh, cx, cy = 2.5, w/12, h/4, w/2, h/2
rc = randomDarkColors

drw.drawLine(im, (cx-ox, cy-oh), (cx+ox, cy+oh), color=rc(), hasArrow=True)
drw.drawLine(im, (cx-ox, cy-oh+oh/2), (cx+ox, cy+oh+oh/2), color=rc(), hasArrow=False)
drw.drawPoly(im, [(w/f, h/f), (w-w/f, h/2), (w/2, h-h/f)], color=rc())

drw.drawStar(im, (ox, oh), oh/2, color=rc(), rotation=45)
drw.drawStar(im, (w-ox, oh), oh/2, color=rc(), points=7)

drw.drawStar(im, (ox*3, oh), oh/2, color=rc(), rotation=65,thickness=2)
drw.drawStar(im, (w-ox*3, oh), oh/2, color=rc(), points=8,rotation=25)

drw.drawStar(im, (ox, h-oh), oh/2, color=rc(), points=9)
drw.drawStar(im, (w-ox, h-oh), oh/2, color=rc(), points=11, thickness=15)

drw.drawTriangle(im, (ox, h/2), oh/f, color=rc(), thickness=20)
drw.drawTriangle(im, (w-ox, h/2), oh/f, color=rc(), rotation=45)
~~~

![im](showcase/drawStar2.png)

___
**This library is licensed by MIT. But used modules, including OpenCV and Python, may have other licenses. Then; To use, consider the licenses of those modules.**