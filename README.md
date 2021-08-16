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
<pre style='text-align:center'>
    <img src='showcase/drawStar.png' width='300px'/>
</pre>