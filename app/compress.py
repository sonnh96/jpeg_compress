import os
import numpy as np
from numpy import r_
from scipy import signal, misc, fftpack, ndimage
from pprint import pprint

def compression(image, quality):
	tree = []
	img = misc.imread('app/static/images/origin/' + image)
	imsize = img.shape
	dct = np.zeros(imsize)
	des = "compress_" + image
	path = "app/static/images/compress/"
	for i in r_[:imsize[0]:8]:
	    for j in r_[:imsize[1]:8]:
	        dct[i:(i+8),j:(j+8)] = dct2( img[i:(i+8),j:(j+8)] )
	quality = int(quality)
	thresh = 0.001*(100-quality)
	dct_thresh = dct * (abs(dct) > (thresh*np.max(dct)))
	im_dct = np.zeros(imsize)
	for i in r_[:imsize[0]:8]:
	    for j in r_[:imsize[1]:8]:
	        im_dct[i:(i+8),j:(j+8)] = idct2( dct_thresh[i:(i+8),j:(j+8)] )
	
	misc.imsave(path + des, im_dct)
	filesize = os.path.getsize(path+des)
	tree.append(des)
	tree.append(filesize)
	pprint(tree)
	return tree

def dct2(a):
    return fftpack.dct(fftpack.dct( a, norm='ortho' ), norm='ortho' )

def idct2(a):
    return fftpack.idct(fftpack.idct( a , norm='ortho'), norm='ortho')

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
    imgcrop = np.zeros(cropsize)
    imgcrop = img[h1:h2,w1:w2]
    des = "crop_" + image
    path = "app/static/images/compress/"
    misc.imsave(path + des, imgcrop)
    filesize = os.path.getsize(path + des)
    tree.append(des)
    tree.append(filesize)
    return tree

def rotation(image, horizontally, vertically, rot):
    tree = []
    img = misc.imread('app/static/images/origin/' + image)
    imsize = img.shape

    pprint(rot)
    if horizontally == True:
        img = np.fliplr(img)

    if vertically == True:
        img = np.flipud(img)
    if rot:
        rot = float(rot)
        img = ndimage.rotate(img, rot)
    des = "rotate_" + image
    path = "app/static/images/compress/"
    misc.imsave(path + des, img)
    filesize = os.path.getsize(path + des)
    tree.append(des)
    tree.append(filesize)
    return tree