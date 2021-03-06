# OpenIPKit
This module is a set of helper functions for ImageProcessing and ComputerVision.

## ML
### Simple Trainer and Detector
Machine learning algorithms are both complex and require a powerful computer. I wrote a simple algorithm for training, modeling, and object recognition. In special circumstances, it can be trained with a smaller number of samples and diagnose quickly. To test numbers from 1 to 4, I trained it with Persian number trainset and test these models.

~~~python
import openipkit.ml.nslearn as learn

# You can make a separate model for each category (In this case for each number)
model = learn.simpleLearn(trainImageList, 32, 16)

# Finally, you can compare the distance between the models. A lower number indicates more similarity but there is a possibility of error.
dist = learn.simpleDetect(im, model)        
~~~

![im](showcase/train_showcase.png)

## Draw Functions
### Draw Chess Grid
~~~python
import scripts.nsdraw as draw
im = draw.grid(im)
~~~

**Parameters**  
- **im:** numpy.ndarray  
- **color1:** tuple  
- **color2:** tuple  
- **thickness:** int  

![im](showcase/_grid1.png)


### Draw Star

~~~python
import scripts.nsdraw as draw

draw.triangle(im, (100, 100), 50, color=(0,0,0), rotation=-90)
~~~

![im](showcase/drawStar4.png)

### Draw Homogeneous Polygon

~~~python
import scripts.nsdraw as draw

draw.hPoly(im, (100,100), 50, color=(0,0,0), rotation=-90)
~~~

![im](showcase/drawHomogeneousPoly.png)

### Draw Triangle
~~~python
import scripts.nsdraw as draw

draw.triangle(im, (100,100), 50, color=(0,0,0), rotation=-90)
~~~

![im](showcase/drawTriangle.png)

### Draw Line, Arrow and Multiline
~~~python
import scripts.nsdraw as draw

draw.line(im, (240, 307), (330, 40), color=(0,0,0))
# or
pts = [(418, 303), (461, 195),  (539, 140), (520, 40)]
draw.multiline(im, pts, color=(0,0,0), arrowType=drw.MULTILINE_ARROW_NONE)
~~~

~~~python
arrowType= draw.MULTILINE_ARROW_NONE   
arrowType= draw.MULTILINE_ARROW_END   
arrowType= draw.MULTILINE_MULTIPLE_ARROW   
~~~

![im](showcase/drawMultiLine.png)

### Draw Circles and Arcs
~~~python
import scripts.nsdraw as draw

draw.circle(im, (100, 100), 50, color=rc(), thickness=2, arc=180, rotation=0)
~~~

![im](showcase/drawArc.png)

## Math
|FIXME|

## Font
|FIXME|

## Future works
- [x] Draw arc
- [ ] Make a font and font-wrapper
- [ ] Add a simple vector font, something that i can rotate, sheer, resize and ...
- [ ] Draw shaped line, dashed line, dotted line in every draw function
- [ ] Draw bullet and other markers on every point of multiline function
- [ ] Make a simpler structure for put small image in big image
- [ ] Make a simpler structure for rotate and transform images
- [ ] Make a simple FeatureMatcher
- [ ] Add some features to console table maker
- [ ] Make 3D renderer for image slices

- [ ] Make a stitcher algorithm 


## License
License of this repository [LICENSE](/LICENSE).


NOTICE: In this project, two different modules are used as backend. Please consider the licenses of these two modules before using this repository.
[OpenCV](https://github.com/opencv), [NumPy](https://numpy.org/about/)
