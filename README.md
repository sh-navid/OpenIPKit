# PyHelper
This module a set of helper functions for OpenCV, ImageProcessing, CV and Python.

## Draw Functions
### Draw Star and Triangle

~~~python
drawStar(im, (w//4, h//4), w//8, color=(200, 100, 220))
drawStar(im, (w-w//4, h//4), w//8, color=(150, 100, 220), points=7)

drawStar(im, (w//4, h-h//4), w//8, color=(41, 100, 220), points=9)
drawStar(im, (w-w//4, h-h//4), w//8, color=(41, 200, 50), points=11,thickness=15)

drawTriangle(im, (w//4, h//2), w//12, color=(50, 10, 220),thickness=20)
drawTriangle(im, (w-w//4, h//2), w//12, color=(220, 50, 100), rotation=45)
~~~

<img src='showcase/drawStar.png' width='300px'/>