import cv2
import sys
import numpy as np

left = cv2.imread(sys.path[0]+"/left.jpg")
right = cv2.imread(sys.path[0]+"/right.jpg")

LH, LW = left.shape[:2]
RH, RW = right.shape[:2]

AL, AR = (1700, 756), (320, 618)
BL, BR = (1704, 1687), (307, 1609)
xOff = RW-max(BL[0], BR[0])

topX,btmX=LW-AL[0]+AR[0],LW-BL[0]+BR[0]

topWidth = AL[0]+RW-AR[0]
btmWidth = BL[0]+RW-BR[0]

W = max(topWidth, btmWidth)

_ = np.hstack((left, right))
AR = (LW+AR[0], AR[1])
BR = (LW+BR[0], BR[1])

for p in [AL, BL, AR, BR]:
    cv2.circle(_, p, 30, (100, 255, 50), 15)

cv2.line(_, AL, AR, (100, 255, 50), 15)
cv2.line(_, BL, BR, (100, 255, 50), 15)

_inp = np.float32([AR, (LW+RW, 0), (LW+RW, RH), BR])
_out = np.float32([AL, (LW+RW-xOff, 0), (LW+RW-xOff, RH), BL])
M = cv2.getPerspectiveTransform(_inp, _out)
_ = cv2.warpPerspective(_, M, (LW+RW, LH))


_[0:LH, 0:LW-(LW-max(AL[0], BL[0]))] = left[0:LH, 0:LW-(LW-max(AL[0], BL[0]))]

cv2.imwrite(sys.path[0]+"/left+right.jpg", _)
