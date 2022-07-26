import matplotlib.pyplot as plt
import numpy as np
import cv2
import os


def make_thumbnail(base_folder, save_folder, input_image, max_size):
    threshold = 127
    if 'santa' in input_image:
        wer = 1
    if 'mask' in input_image or 'lips' in input_image:
        threshold = 230
    if isinstance(input_image, str):
        img = plt.imread(base_folder + input_image)
    else:
        img = input_image.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if 'lips' in input_image or 'santa' in input_image:
        ret, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)
    else:
        ret, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    contours, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # note that h goes with x and w with y
    if contours:
        idx = 1
        if 'santa' in input_image: idx = 0
        x, y, w, h = cv2.boundingRect(contours[idx])
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        img = img[y:y + h, x:x + w, :]
    else:
        (x, y, w, h) = (0, 0, 0, 0)
        print('No Contours')
    m, n, p = img.shape
    if m > n:
        scale = m / max_size
    else:
        scale = n / max_size
    img = cv2.resize(img, (int(n / scale), int(m / scale)))
    print(save_folder + input_image.split('.')[0] + '_thumbnail.png')
    cv2.imwrite(save_folder + input_image.split('.')[0] + '_thumbnail.png', img[:, :, ::-1])
    return (x, y, w, h), thresh


sizes = {'base': 50,
         'hat': 20,
         'eyes': 10,
         'mask': 30,
         'lips': 15}

base_folder = '/home/carmelo/Projects/NFTGenerator/NFTImages/'
save_folder = base_folder + 'Thumbnails/'

# input_image = 'base.jpg'

for input_image in os.listdir(base_folder):
    try:
        print(input_image)
        if 'hat' in input_image:
            resize = sizes['hat']
        elif 'eyes' in input_image:
            resize = sizes['eyes']
        elif 'mask' in input_image:
            resize = sizes['mask']
        elif 'base' in input_image:
            resize = sizes['base']
        elif 'lips' in input_image:
            resize = sizes['lips']
        make_thumbnail(base_folder, save_folder, input_image, resize)
    except IsADirectoryError:
        pass
