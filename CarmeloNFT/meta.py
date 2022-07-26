import matplotlib.pyplot as plt
import numpy as np
import cv2
import csv
import os
import pyautogui
import time

nft_location = '/home/carmelo/Projects/NFTGenerator/CryptoPoopiesBackup/'
larger_location = '/home/carmelo/Projects/NFTGenerator/CryptoPoopiesLarger/'

# meta = []
#
# lips = []
# for poopie in os.listdir(nft_location):
#     img = plt.imread(nft_location + poopie)
#     data = poopie.split('-')
#     color = data[0].split('_')[-1]
#     number = data[-1].split('_')
#     face = number[0]
#     number = number[-1].split('.')[0]
#     eyes = data[2]
#     hat = data[3]
#     if face == 'lips':
#         # img[51, 30, :] = img[49, 31, :]
#         # big = cv2.resize(img, (420, 420), fx=0, fy=0, interpolation=cv2.INTER_NEAREST)
#         # plt.imsave(larger_location + 'crypto_poopie_' + number + '.png', big)
#         # lips_num.append(number)
#         lips.append('crypto_poopie_' + number + '.png')
#     # meta.append([number, color, eyes, hat, face])
#     # with open('meta_csv.csv','a') as csv_file:
#     #     csvwriter = csv.writer(csv_file)
#     #     csvwriter.writerows([[number, color, eyes, hat, face]])
#
#
# lips = lips[::-1]
# lips = lips[4:]

numbers = [86, 233, 13]
lips = []
lips = ['crypto_poopie_' + str(number) + '.png' for number in numbers]

a = 1

url = 'https://opensea.io/collection/crypto-poopies-collection'

x, y = 2683, 225
pyautogui.moveTo(x, y, duration=0.1)
pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
pyautogui.typewrite(url, interval=0.05)
pyautogui.press("enter")
time.sleep(5)

for LIP in lips:
    print(LIP)
    x, y = 2898, 1922
    LIP_num = LIP.split('_')[-1]
    LIP_num = LIP_num.split('.')[0]
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
    pyautogui.typewrite(LIP_num, interval=0.05)
    pyautogui.press("enter")
    time.sleep(2)

    x, y = 3230, 1506
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

    time.sleep(3)
    x, y = 2913, 2330
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
    time.sleep(1)

    x, y = 2473, 1250
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

    time.sleep(0.3)
    x, y = 3537, 653
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
    time.sleep(0.1)
    pyautogui.typewrite(LIP, interval=0.05)
    time.sleep(0.1)
    pyautogui.press("enter")

    c = 0
    while c < 25:
        time.sleep(0.05)
        pyautogui.scroll(-1)
        c += 1

    x, y = 2285, 2045
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

    x, y = 2420, 225
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

    pyautogui.typewrite(url, interval=0.05)
    pyautogui.press("enter")
    time.sleep(5)

pyautogui.position()
