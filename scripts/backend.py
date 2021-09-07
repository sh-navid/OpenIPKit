import cv2
import scripts.exphandle as exp

# This is backend; default backend id OpenCV
# Please check OpenCV License before use
# Or you can change this and use any other module you want

BACKEND_OPENCV = 0

backend_engine = BACKEND_OPENCV


def imread(pth):
    if backend_engine == BACKEND_OPENCV:
        return cv2.imread(pth, -1)
    exp.echo(exp.DEFINE_BACKEND)
    return None


def imwrite(pth, im):
    if backend_engine == BACKEND_OPENCV:
        cv2.imwrite(pth, im)
        return True
    exp.echo(exp.DEFINE_BACKEND)
    return False


def imshow(title, im):
    if backend_engine == BACKEND_OPENCV:
        cv2.imshow(title, im)
        cv2.waitKey(0)
        return True
    exp.echo(exp.DEFINE_BACKEND)
    return False


def resize(im, newSize):
    if backend_engine == BACKEND_OPENCV:
        return cv2.resize(im, newSize)
    exp.echo(exp.DEFINE_BACKEND)
    return None