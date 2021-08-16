import cv2
import scripts.drwHelper as drw
import scripts.osHelper as osh

dir = osh.getRoot(__file__)

im = cv2.imread(dir+r'/media/im.png')
h, w = im.shape[:2]
drw.drawLine(im, (0, 0), (w//2, h//2), hasArrow=True)

f = 2.5
drw.drawPoly(im, [(w/f, h/f), (w-w/f, h/2), (w/2, h-h/f)])

drw.drawStar(im, (w/4, h/4), w/8, color=(200, 100, 220))
drw.drawStar(im, (w-w/4, h/4), w/8, color=(150, 100, 220), points=7)

drw.drawStar(im, (w/4, h-h/4), w/8, color=(41, 100, 220), points=9)
drw.drawStar(im, (w-w/4, h-h/4), w/8,
             color=(41, 200, 50), points=11, thickness=15)

drw.drawTriangle(im, (w/4, h/2), w/12, color=(50, 10, 220), thickness=20)
drw.drawTriangle(im, (w-w/4, h/2), w/12, color=(220, 50, 100), rotation=45)

# drawMarker(im,(w//2,h//2))

cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
