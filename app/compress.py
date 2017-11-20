import os
import numpy as np
from numpy import r_
from scipy import signal, misc, fftpack


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
	
	thresh = 0.1
	dct_thresh = dct * (abs(dct) > (thresh*np.max(dct)))
	#percent_nonzeros = np.sum( dct_thresh != 0.0 ) / (imsize[0]*imsize[1]*1.0)
	
	im_dct = np.zeros(imsize)
	for i in r_[:imsize[0]:8]:
	    for j in r_[:imsize[1]:8]:
	        im_dct[i:(i+8),j:(j+8)] = idct2( dct_thresh[i:(i+8),j:(j+8)] )
	
	misc.imsave(path + des, im_dct)
	filesize = os.path.getsize(path+des)
	tree.append(des)
	tree.append(filesize)
	return tree

def dct2(a):
    return fftpack.dct(fftpack.dct( a, norm='ortho' ), norm='ortho' )

def idct2(a):
    return fftpack.idct(fftpack.idct( a , norm='ortho'), norm='ortho')


