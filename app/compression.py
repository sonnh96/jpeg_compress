import numpy as np
from numpy import r_
from scipy import signal, misc, fftpack
from matplotlib import pyplot as plt
from pprint import pprint
import Image
import cv2

def dct2(a):
    return fftpack.dct(fftpack.dct( a, axis=0, norm='ortho' ), axis=1, norm='ortho' )

def idct2(a):
    return fftpack.idct(fftpack.idct( a, axis=0 , norm='ortho'), axis=1 , norm='ortho')

# def rgb2ycbcr(im):
#     xform = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
#     ycbcr = im.dot(xform.T)
#     ycbcr[:,:,[1,2]] += 128
#     return np.uint8(ycbcr)

# def ycbcr2rgb(im):
#     xform = np.array([[1, 0, 1.402], [1, -0.34414, -.71414], [1, 1.772, 0]])
#     rgb = im.astype(np.float)
#     rgb[:,:,[1,2]] -= 128
#     return np.uint8(rgb.dot(xform.T))

def quantize(input_matrix,block_size,qr):

    quantize_matrix = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]])

    if block_size == 16:
        quantize_matrix_double = np.zeros((block_size, block_size))
        for i in range(0,8):
            for j in range(0, 8):
                temp = quantize_matrix[i][j]
                quantize_matrix_double[2 * i][2 * j] = temp
                quantize_matrix_double[2 * i + 1][2 * j] = temp
                quantize_matrix_double[2 * i][2 * j + 1] = temp
                quantize_matrix_double[2 * i + 1][2 * j + 1] = temp
        used_quantize_matrix = quantize_matrix_double
    else:
        used_quantize_matrix = quantize_matrix

    used_quantize_matrix = used_quantize_matrix/qr
    quantized_matrix = input_matrix/used_quantize_matrix
    quantized_matrix = np.rint(quantized_matrix)
    return quantized_matrix

# quantize_matrix = np.array([
# [16, 11, 10, 16, 24, 40, 51, 61],
# [12, 12, 14, 19, 26, 58, 60, 55],
# [14, 13, 16, 24, 40, 57, 69, 56],
# [14, 17, 22, 29, 51, 87, 80, 62],
# [18, 22, 37, 56, 68, 109, 103, 77],
# [24, 35, 55, 64, 81, 104, 113, 92],
# [49, 64, 78, 87, 103, 121, 120, 101],
# [72, 92, 95, 98, 112, 100, 103, 99]])

# quantize_matrix = quantize_matrix/16

img1 = misc.imread('2.jpg')

imgr = img1[:,:,0]
imgg = img1[:,:,1]
imgb = img1[:,:,2]

imsize = img1.shape
dct = np.zeros(imsize)

for i in r_[:imsize[0]:8]:
    for j in r_[:imsize[1]:8]:
        dct[i:(i+8),j:(j+8),0] = quantize( dct2(imgr[i:(i+8),j:(j+8)]), 8, 10)
for i in r_[:imsize[0]:8]:
    for j in r_[:imsize[1]:8]:
        dct[i:(i+8),j:(j+8),1] = quantize( dct2(imgg[i:(i+8),j:(j+8)]), 8, 10)
for i in r_[:imsize[0]:8]:
    for j in r_[:imsize[1]:8]:
        dct[i:(i+8),j:(j+8),2] = quantize( dct2(imgb[i:(i+8),j:(j+8)]), 8, 10)


im_dct = np.zeros(imsize)

for i in r_[:imsize[0]:8]:
    for j in r_[:imsize[1]:8]:
        im_dct[i:(i+8),j:(j+8),0] = idct2( dct[i:(i+8),j:(j+8),0] )
for i in r_[:imsize[0]:8]:
    for j in r_[:imsize[1]:8]:
        im_dct[i:(i+8),j:(j+8),1] = idct2( dct[i:(i+8),j:(j+8),1] )
for i in r_[:imsize[0]:8]:
    for j in r_[:imsize[1]:8]:
        im_dct[i:(i+8),j:(j+8),2] = idct2( dct[i:(i+8),j:(j+8),2] )

misc.imsave('cp1.jpg', im_dct)
# imgr = img1[:,:,0]
# imgg = img1[:,:,1]
# imgb = img1[:,:,2]

# img2 = rgb2ycbcr(img1)

# pprint(img2.shape)
# imsize = imgr.shape
# y = img2[:,:,0]
# cb = img2[:,:,1]
# cr = img2[:,:,2]

# dctr = np.zeros(imsize)
# dctg = np.zeros(imsize)
# dctb = np.zeros(imsize)

# for i in r_[:imsize[0]:8]:
#     for j in r_[:imsize[1]:8]:
#         dctr[i:(i+8),j:(j+8)] = np.rint(dct2( y[i:(i+8),j:(j+8)] )/quantize_matrix)
        #pprint(dctr[i:(i+8),j:(j+8)])
# for i in r_[:imsize[0]:8]:
#     for j in r_[:imsize[1]:8]:
#         dctg[i:(i+8),j:(j+8)] = np.rint(dct2( y[i:(i+8),j:(j+8)] )/quantize_matrix)
        #pprint(dctr[i:(i+8),j:(j+8)])
# for i in r_[:imsize[0]:8]:
#     for j in r_[:imsize[1]:8]:
#         dctb[i:(i+8),j:(j+8)] = np.rint(dct2( y[i:(i+8),j:(j+8)] )/quantize_matrix)
        #pprint(dctr[i:(i+8),j:(j+8)])


# thresh = 0
# dct_thresh = dct * (abs(dct) > (thresh*np.max(dct)))
# percent_nonzeros = np.sum( dct_thresh != 0.0 ) / (imsize[0]*imsize[1]*1.0)

# im_dct = np.zeros(imsize)
# im_dctr = np.zeros(imsize)
# im_dctg = np.zeros(imsize)
# im_dctb = np.zeros(imsize)

# for i in r_[:imsize[0]:8]:
#     for j in r_[:imsize[1]:8]:
#         im_dctr[i:(i+8),j:(j+8)] = idct2( dctr[i:(i+8),j:(j+8)] )
# for i in r_[:imsize[0]:8]:
# 	for j in r_[:imsize[1]:8]:
# 		im_dctg[i:(i+8),j:(j+8)] = idct2( dctg[i:(i+8),j:(j+8)] )
# for i in r_[:imsize[0]:8]:
#     for j in r_[:imsize[1]:8]:
#         im_dctb[i:(i+8),j:(j+8)] = idct2( dctb[i:(i+8),j:(j+8)] )
        
# img3 = np.zeros(img1.shape)

# img3[:,:,0] = im_dctr
# img3[:,:,1] = im_dctg
# img3[:,:,2] = im_dctb

# img3 = ycbcr2rgb(img3)

# misc.imsave('raw.jpg', img3)







def zig_zag(input_matrix,block_size):
    z = np.empty([block_size*block_size])
    index = -1
    bound = 0
    for i in range(0, 2 * block_size -1):
        if i < block_size:
            bound = 0
        else:
            bound = i - block_size + 1
        for j in range(bound, i - bound + 1):
            index += 1
            if i % 2 == 1:
                z[index] = input_matrix[j, i-j]
            else:
                z[index] = input_matrix[i-j, j]
    return z