# PyHelper
This is module a set of helper functions for OpenCV, ImageProcessing, ComputerVision and Python.

## Draw Helper
### Draw Star

~~~python
import cv2
import scripts.drawHelper as drw
import scripts.osHelper as osh
from scripts.colorHelper import *
 
im = cv2.imread(osh.getPath(__file__)+r'/media/im.png')

h, w = im.shape[:2]
cx, ch = w/2, h/2
rc = randomColor

drw.drawStar(im, (cx-cx/1.6, ch), ch/2, color=rc(), rotation=-90)
drw.drawStar(im, (cx, ch), ch/2, color=rc(), rotation=-90, thickness=10, points=9)
drw.drawStar(im, (cx+cx/1.6, ch), ch/2, color=rc(), points=15, thickness=30)
~~~

![im](showcase/drawStar4.png)

### Draw Homogeneous Polygon

~~~python
import cv2
import scripts.drawHelper as drw
import scripts.osHelper as osh
from scripts.colorHelper import *
 
im = cv2.imread(osh.getPath(__file__)+r'/media/im.png')

h, w = im.shape[:2]
cx, ch = w/2, h/2
rc = randomColor

drw.drawHomogeneousPoly(im, (cx-cx/1.6, ch), ch/2, color=rc(), rotation=-90)
drw.drawHomogeneousPoly(im, (cx, ch), ch/2, color=rc(), rotation=-90, thickness=10, points=9)
drw.drawHomogeneousPoly(im, (cx+cx/1.6, ch), ch/2, color=rc(), points=15, thickness=30)
~~~

![im](showcase/drawHomogeneousPoly.png)

### Draw Triangle
~~~python
import cv2
import scripts.drawHelper as drw
import scripts.osHelper as osh
from scripts.colorHelper import *

im = cv2.imread(osh.getPath(__file__)+r'/media/im.png')

h, w = im.shape[:2]
cx, ch, of = w/2, h/2, h/18
rc = randomColor

drw.drawTriangle(im, (cx-cx/1.6, ch+of), ch/2, color=rc(), rotation=-90)
drw.drawTriangle(im, (cx, ch-of), ch/2, color=rc(), rotation=-45, thickness=15)
drw.drawTriangle(im, (cx+cx/1.6, ch-of), ch/2, color=rc(), thickness=30)
~~~

![im](showcase/drawTriangle.png)

### Draw Line, Arrow and Multiline
~~~python
import cv2
import scripts.drawHelper as drw
import scripts.osHelper as osh
from scripts.colorHelper import *

im = cv2.imread(osh.getPath(__file__)+r'/media/im.png')

h, w = im.shape[:2]
cx, ch = w/2, h/2
rc = randomColor

drw.drawLine(im, (60, 303), (151, 40), color=rc(), hasArrow=True)
drw.drawLine(im, (240, 307), (330, 40), color=rc(), hasArrow=False)

pts = [(418, 303), (461, 195),  (539, 140), (520, 40)]
drw.drawMultiLine(im, pts, color=rc(), arrowType=drw.MULTILINE_ARROW_NONE)
#or
drw.drawMultiLine(im, pts, color=rc(), arrowType=drw.MULTILINE_ARROW_END)
#or
drw.drawMultiLine(im, pts, color=rc(), arrowType=drw.MULTILINE_MULTIPLE_ARROW)
~~~

![im](showcase/drawMultiLine.png)

### Draw Circles and Arcs
~~~python
import cv2
import scripts.drawHelper as drw
import scripts.osHelper as osh
from scripts.colorHelper import *
from inspect import signature

im = cv2.imread(osh.getPath(__file__)+r'/media/im.png')

h, w = im.shape[:2]
ox, oh, cx, cy, o = w/4, h/4, w/2, h/2, (w/2)/1.6
rc = randomColor

drw.drawCircle(im, (cx-o, cy), h/14, color=rc(), thickness=2, arc=180, rotation=0)
drw.drawCircle(im, (cx-o, cy), h/7, color=rc(), thickness=10, arc=90, rotation=-90)
drw.drawCircle(im, (cx-o, cy), h/4, color=rc(), thickness=25, arc=270, rotation=-180)

drw.drawCircle(im, (cx, cy), h/14, color=rc(), thickness=2)
drw.drawCircle(im, (cx, cy), h/7, color=rc(), thickness=10)
drw.drawCircle(im, (cx, cy), h/4, color=rc(), thickness=25)

drw.drawCircle(im, (cx+o, cy), h/14, color=rc(), endLastLine=False, thickness=2, arc=180, rotation=0)
drw.drawCircle(im, (cx+o, cy), h/7, color=rc(), endLastLine=False, thickness=10, arc=90, rotation=-90)
drw.drawCircle(im, (cx+o, cy), h/4, color=rc(), endLastLine=False, thickness=25, arc=270, rotation=-180)


~~~

![im](showcase/drawArc.png)

## OS Helper

## Color Helper
### Random Color
~~~python
from scripts.colorHelper import *

print(randomColor(min=0, max=255))
print(randomLightColors())
print(randomDarkColors())
~~~

>(135, 231, 232)   
>(251, 207, 165)   
>(5, 121, 79)

### Re-Map HSV Color

## Math Helper

## Array Helper

## Font Helper

## Future works
- [x] Draw arc
- [ ] Add a simple vector font, something that i can rotate, sheer, resize and ...
- [ ] Draw shaped line, dashed line, dotted line in every draw function
- [ ] Draw bullet and other markers on every point of multiline function


<table>
    <tr>
        <td>A</td><td>B</td><td>C</td><td>D</td>
    </tr>
</table>


<pre style='line-height:10px'>
╔═══════════════╦═══════════════╗
║       A       ║       B       ║
╚═══════════════╩═══════════════╝

╔═══════════════╦═══════════════╗
║       A       ║       B       ║
╟───────────────╫───────────────╢
║       C       ║       D       ║
╚═══════════════╩═══════════════╝
</pre>


## License
**This library is licensed by MIT. But used modules, including OpenCV and Python, may have other licenses. Then; To use, consider the licenses of those modules.**