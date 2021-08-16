# PyHelper
This module a set of helper functions for OpenCV, ImageProcessing, CV and Python.

## Draw Functions
### Draw Star and Triangle

~~~python
import drwHelper as drw

drw.drawStar(im, (x,y), rad)
drw.drawStar(im, (x,y), rad, points=7)

drw.drawStar(im, (x,y), rad, points=9)
drw.drawStar(im, (x,y), rad, color=(41, 200, 50), points=11, thickness=15)

drw.drawTriangle(im, (x,y), rad, color=(50, 10, 220), thickness=20)
drw.drawTriangle(im, (x,y), rad, color=(220, 50, 100), rotation=45)
~~~

![im](showcase/drawStar2.png)

___
This library is licensed by MIT. But used modules, including OpenCV and Python, may have other licenses. Then; To use, consider the licenses of those modules.