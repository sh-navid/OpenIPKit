import numpy as np

def fill(im,pos=(0,0),color=(0,0,0),diff=0):
    pass

def tresh_simple(im,thresh):
    im[np.where(im<thresh)]=0
    im[np.where(im>=thresh)]=255
    return im