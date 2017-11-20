import numpy as np
from numpy import r_
from scipy import signal, misc, fftpack
from matplotlib import pyplot as plt
from pprint import pprint
import Image
import cv2

img1 = misc.imread('2.jpg')

def dct2(a):
    return fftpack.dct(fftpack.dct( a, norm='ortho' ), norm='ortho' )

def idct2(a):
    return fftpack.idct(fftpack.idct( a, norm='ortho'), norm='ortho')

imsize = img1.shape
dct = np.zeros(imsize)
for i in r_[:imsize[0]:8]:
    for j in r_[:imsize[1]:8]:
        dct[i:(i+8),j:(j+8)] = np.round(dct2(img1[i:(i+8),j:(j+8)]))
        #pprint(dct[i:(i+8),j:(j+8)])

thresh = 0.01
dct_thresh = dct * (abs(dct) > (thresh*np.max(dct)))
percent_nonzeros = np.sum( dct_thresh != 0.0 ) / (imsize[0]*imsize[1]*1.0)

im_dct = np.zeros(imsize)

for i in r_[:imsize[0]:8]:
    for j in r_[:imsize[1]:8]:
        im_dct[i:(i+8),j:(j+8)] = idct2( dct_thresh[i:(i+8),j:(j+8)] )
        
misc.imsave('cp.jpg', im_dct)
