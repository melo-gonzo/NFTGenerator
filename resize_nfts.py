import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

nft_location = '/home/carmelo/Projects/NFTGenerator/CryptoPoopiesBackup/'
larger_location = '/home/carmelo/Projects/NFTGenerator/CryptoPoopiesLarger/'
meta = []
lips = []
for poopie in os.listdir(nft_location):
    img = plt.imread(nft_location + poopie)
    big = cv2.resize(img, (420, 420), fx=0, fy=0, interpolation=cv2.INTER_NEAREST)
    plt.imsave(larger_location + 'crypto_poopie_' + number + '.png', big)