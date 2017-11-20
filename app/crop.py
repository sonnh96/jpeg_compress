import os
import numpy as np
from scipy import signal, misc, fftpack
from pprint import pprint

def cropper(image, x1, y1, x2, y2, width, height):
    tree = []
    img = misc.imread('app/static/images/origin/' + image)
    imsize = img.shape
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    width = float(width)
    height = float(height)
    w1 = int(x1*imsize[0]/width)
    w2 = int(x2*imsize[0]/width)
    h1 = int(y1*imsize[1]/height)
    h2 = int(y2*imsize[1]/height)

    cropsize = (w2-w1, h2-h1, 3)
    pprint(cropsize)
    imgcrop = np.zeros(cropsize)
    imgcrop = img[h1:h2,w1:w2]
    pprint(imgcrop)
    des = "compress_" + image
    path = "app/static/images/compress/"
    misc.imsave(path + des, imgcrop)
    filesize = os.path.getsize(path + des)
    tree.append(des)
    tree.append(filesize)
    return tree