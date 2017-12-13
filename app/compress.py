import os
import numpy as np
import random
from numpy import r_
from scipy import signal, misc, fftpack, ndimage
from pprint import pprint
import cv2


def imgCompress(image, quality):
    def dct2(a):
        return fftpack.dct(fftpack.dct(a, norm='ortho'), norm='ortho')

    def idct2(a):
        return fftpack.idct(fftpack.idct(a, norm='ortho'), norm='ortho')

    tree = []
    img = misc.imread('app/static/images/' + image)
    imsize = img.shape
    dct = np.zeros(imsize)
    des = str(random.randint(1000, 9999)) + image
    path = "app/static/images/"
    for i in r_[:imsize[0]:8]:
        for j in r_[:imsize[1]:8]:
            dct[i:(i + 8), j:(j + 8)] = dct2(img[i:(i + 8), j:(j + 8)])
    quality = int(quality)
    thresh = 0.01 * (100 - quality)
    dct_thresh = dct * (abs(dct) > (thresh * np.max(dct)))
    im_dct = np.zeros(imsize)
    for i in r_[:imsize[0]:8]:
        for j in r_[:imsize[1]:8]:
            im_dct[i:(i + 8), j:(j + 8)] = idct2(dct_thresh[i:(i + 8), j:(j + 8)])

    misc.imsave(path + des, im_dct)
    filesize = os.path.getsize(path + des)
    tree.append(des)
    tree.append(filesize)
    pprint(tree)
    return tree


def imgCrop(image, x1, y1, x2, y2, width, height):
    tree = []
    img = misc.imread('app/static/images/' + image)
    imsize = img.shape
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    width = float(width)
    height = float(height)
    w1 = int(x1 * imsize[0] / width)
    w2 = int(x2 * imsize[0] / width)
    h1 = int(y1 * imsize[1] / height)
    h2 = int(y2 * imsize[1] / height)

    cropsize = (w2 - w1, h2 - h1, 3)
    imgcrop = np.zeros(cropsize)
    imgcrop = img[h1:h2, w1:w2]
    des = str(random.randint(1000, 9999)) + image
    path = "app/static/images/"
    misc.imsave(path + des, imgcrop)
    filesize = os.path.getsize(path + des)
    tree.append(des)
    tree.append(filesize)
    return tree


def imgRotate(image, horizontally, vertically, rot):
    tree = []
    img = misc.imread('app/static/images/' + image)

    pprint(rot)
    if horizontally == True:
        img = np.fliplr(img)

    if vertically == True:
        img = np.flipud(img)
    if rot:
        rot = float(rot)
        img = ndimage.rotate(img, rot)
    des = str(random.randint(1000, 9999)) + image
    path = "app/static/images/"
    misc.imsave(path + des, img)
    filesize = os.path.getsize(path + des)
    tree.append(des)
    tree.append(filesize)
    return tree


def imgResize(image, height, width):
    tree = []
    img = misc.imread('app/static/images/' + image)
    imsize = img.shape
    height = float(height)
    width = float(width)
    height = int(height)
    width = int(width)
    img1 = np.zeros((width, height))
    img1 = misc.imresize(img, (height, width), interp='bilinear', mode=None)
    des = str(random.randint(1000, 9999)) + image
    path = "app/static/images/"
    misc.imsave(path + des, img1)
    filesize = os.path.getsize(path + des)
    tree.append(des)
    tree.append(filesize)
    return tree


def imgEffect(image, s, g, v, l, b, c):
    def sepia(image):
        sepia = np.zeros(image.shape)
        r, g, b = image[:, :, 0], image[:, :, 1], image[:, :, 2]
        newR = (r * 0.393 + g * 0.769 + b * 0.189)
        newG = (r * 0.349 + g * 0.686 + b * 0.168)
        newB = (r * 0.272 + g * 0.534 + b * 0.131)
        sepia[:, :, 0], sepia[:, :, 1], sepia[:, :, 2] = newR, newG, newB
        return sepia

    def greyscale(rgb):
        r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray

    def contrast(image, contrast_value):
        height, width, channels = image.shape
        for x in range(height):
            for y in range(width):
                for c in range(channels):
                    if image[x, y, c] + contrast_value > 255:
                        image[x, y, c] = 255
                    elif image[x, y, c] + contrast_value < 0:
                        image[x, y, c] = 0
                    else:
                        image[x, y, c] += contrast_value
        return image

    def brightness(image, brightness_value):
        # Convert BGR to HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        height, width, channels = hsv.shape
        for x in range(height):
            for y in range(width):
                if hsv[x, y, 2] + brightness_value > 255:
                    hsv[x, y, 2] = 255
                elif hsv[x, y, 2] + brightness_value < 0:
                    hsv[x, y, 2] = 0
                else:
                    hsv[x, y, 2] += brightness_value
                    # Write new pixel channel value
        edit_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        return edit_img

    def vignettet(image):
        rows, cols = image.shape[:2]
        kernel_x = cv2.getGaussianKernel(cols, cols / 3)
        kernel_y = cv2.getGaussianKernel(rows, rows / 3)
        kernel = kernel_y * kernel_x.T
        mask = 255 * kernel / np.linalg.norm(kernel)
        output = np.copy(img)
        for i in range(3):
            output[:, :, i] = output[:, :, i] * mask
        return output

    def linedraw(image):
        def cvt(x):
            if x == 0:
                return 255
            elif x == 255:
                return 0

        edges = cv2.Canny(image, 100, 200)
        height, width = edges.shape
        for x in range(height):
            for y in range(width):
                edges[x, y] = cvt(edges[x, y])
        return edges

    b = int(b)
    c = int(c)

    tree = []
    img = misc.imread('app/static/images/' + image)
    imsize = img.shape
    img1 = np.zeros(imsize)

    if s:
        img1 = sepia(img)
    elif g:
        img1 = greyscale(img)
    elif v:
        img1 = vignettet(img)
    elif l:
        img1 = linedraw(img)
    else:
        img1 = np.copy(img)
    if b != 0 and s is False and g is False and l is False:
        img1 = brightness(img1, b)
    if c != 0 and s is False and g is False and l is False:
        img1 = contrast(img1, c)

    des = str(random.randint(1000, 9999)) + image
    path = "app/static/images/"
    misc.imsave(path + des, img1)
    filesize = os.path.getsize(path + des)
    tree.append(des)
    tree.append(filesize)

    return tree
