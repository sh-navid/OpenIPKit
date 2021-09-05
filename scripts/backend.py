import cv2

# This is backend; you can use any other module you want

def imread(pth):
    return cv2.imread(pth,-1)

def imwrite(pth,im):
    cv2.imwrite(pth,im)

def imshow(title,im):
    cv2.imshow(title,im)
    cv2.waitKey(0)

def resize(im,newSize):
    cv2.resize(im, newSize)