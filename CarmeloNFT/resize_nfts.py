import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

nft_location = "D:\\Git\\nftgen\\NFTGenerator\\final_images\\"
larger_location = "D:\\Git\\nftgen\\NFTGenerator\\final_larger\\"
meta = []
lips = []
for poopie in os.listdir(nft_location):
    img = plt.imread(nft_location + poopie)
    big = cv2.resize(img, (400, 400), fx=0, fy=0, interpolation=cv2.INTER_NEAREST)
    plt.imsave(larger_location + 'crypto_minecraft_' + number + '.png', big)