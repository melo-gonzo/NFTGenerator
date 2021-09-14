import matplotlib.pyplot as plt
from utils import *
import numpy as np
import random
import copy
import os

class NFTGenerator:
    def __init__(self):
        self.show_plots = True
        self.mask_dir = "D:\\Git\\nftgen\\NFTGenerator\\images_gimp\\"
        # self.mask_dir = '/home/carmelo/Projects/NFTGenerator/images_gimp/'
        self.shape = (50, 50)
        self.center = [int(self.shape[0] / 2), int(self.shape[1] / 2)]
        self.background = 1 * np.ones((self.shape[0], self.shape[1], 4)).astype('float32')
        self.background_mask = 0 * np.ones((self.shape[0], self.shape[1], 4)).astype('float32')
        self.current_image = self.background.copy()
        self.backgrounds = {'purple': (204, 153, 210),
                            'blue': (158, 193, 207),
                            'green': (158, 224, 158),
                            'yellow': (253, 253, 151),
                            'orange': (254, 177, 68),
                            'red': (255, 102, 99)}
        self.helmet = {'leather': 'leather_helmet.png',
                       'chainmail': 'chainmail_helmet.png',
                       'iron': 'iron_helmet.png',
                       'gold': 'gold_helmet.png',
                       'diamond': 'diamond_helmet.png'}
        self.head_center = [[39, 27], [39, 44]]
        # center coordinates [y, x]
        # helmet center is [6,24]
        self.helmet_center = [[6, 24]]

        self.chest = {'leather': 'leather_chest.png',
                      'chainmail': 'chainmail_chest.png',
                      'iron': 'iron_chest.png',
                      'gold': 'gold_chest.png',
                      'diamond': 'diamond_chest.png'}
        # chest center is [22,24]
        self.chest_center = [[22, 24]]

        self.pants = {'leather': 'leather_pants.png',
                      'chainmail': 'chainmail_pants.png',
                      'iron': 'iron_pants.png',
                      'gold': 'gold_pants.png',
                      'diamond': 'diamond_pants.png'}
        # pants center is [38,24]
        self.pants_center = [[38, 24]]

        self.minecraft = {'default': 'final_char.png'}

        self.eyes = {'ether': 'ethereum_eyes_thumbnail_mask_new.png',
                     'bitcoin': 'bitcoin_eyes_thumbnail_mask.png',
                     'custom': 'base_white_eyes_thumbnail_mask.png',
                     'doge': 'dogecoin_eyes_thumbnail_mask.png',
                     'sunglasses': 'sunglasses_thumbnail_mask.png'}
        self.eyes_center = [[39, 27], [39, 44]]
        self.glasses_center = [[39, 35]]

        self.hats = {'cowboy': 'cowboy_hat_thumbnail_mask.png',
                     'top': 'top_hat_thumbnail_mask.png',
                     'baseball': 'baseball_hat_thumbnail_mask.png',
                     'spinner': 'spinner_hat_thumbnail_mask.png',
                     'halo': 'halo_hat_thumbnail_mask.png',
                     'steam': 'steam_hat_thumbnail_mask.png',
                     'santa': 'santa_hat_thumbnail_mask_new.png'}
        self.hats_center = [[14, 35]]

        self.masks = {'covid': 'covid_mask_thumbnail_mask.png',
                      'lips': 'lips_thumbnail_mask.png',
                      'tongue': 'tongue_thumbnail_mask.png'}
        self.masks_center = [[52, 35]]

        self.base = {'no_eyes_no_mouth': 'base_no_eyes_no_mouth_thumbnail_mask.png',
                     'no_mouth': 'base_no_mouth_thumbnail_mask.png',
                     'no_eyes': 'base_no_eyes_thumbnail_mask.png',
                     'base': 'base_thumbnail_mask.png'}

        self.center = [[int(self.shape[0] / 2), int(self.shape[1] / 2)]]

        # self.combinations = (len(self.eyes) - 1) * len(self.hats) * len(self.masks) * len(self.backgrounds)
        self.combinations = (len(self.helmet) - 1) * len(self.chest) * len(self.pants)
        print("Combinations: %i" % self.combinations)

    def combine_images(self, input_image):
        for m in range(input_image.shape[0]):
            for n in range(input_image.shape[1]):
                if self.current_image[m, n, -1] != 0 and input_image[m, n, -1] != 0:
                    self.current_image[m, n, :] = input_image[m, n, :]

    def make_plot(self, input_image):
        fig = plt.figure(figsize=(10, 10))
        plt.imshow(input_image)
        plt.imsave("D:\\Git\\nftgen\\NFTGenerator\\final_images\\"  + 'diamond_red' + '.png', input_image)
        plt.show()

    def create_background(self, color):
        if color == 'rainbow':
            colors_in = [RGB_to_hex(color) for color in self.backgrounds.values()]
            colors_out = polylinear_gradient(colors_in, 145)
            full_idx = 0
            idx = 0
            while idx < self.shape[0]:
                n = 0
                m = idx
                while m >= 0:
                    self.background[m, n, :3] = np.array(hex_to_RGB(colors_out['hex'][full_idx])) / 255
                    m -= 1
                    n += 1
                idx += 1
                full_idx += 1

            idx = 1
            while idx < self.shape[0]:
                m = self.shape[0] - 1
                n = idx
                while n < self.shape[0]:
                    self.background[m, n, :3] = np.array(hex_to_RGB(colors_out['hex'][full_idx])) / 255
                    m -= 1
                    n += 1
                idx += 1
                full_idx += 1
        else:
            for k in range(3):
                self.background[:, :, k] = self.backgrounds[color][k] / 255

        self.combine_images(self.background)
        if self.show_plots: self.make_plot(self.current_image)

    def add_layer(self, layer_mask, center):
        print(layer_mask)
        if isinstance(layer_mask, str):
            layer_mask = plt.imread(self.mask_dir + layer_mask)
            a = layer_mask.copy()
            a[np.where(a[:, :, -1] < 0.9)] = 0
            layer_mask = a

        new_layer = self.background_mask.copy()
        m, n = layer_mask.shape[:2]
        mc, nc = int(m / 2), int(n / 2)
        for c in center:
            xc, yc = c
            if m % 2 == 1 and n % 2 == 1:
                new_layer[xc - mc - 1:xc + mc, yc - nc - 1:yc + nc, :] = layer_mask
            elif m % 2 == 1:
                new_layer[xc - mc - 1:xc + mc, yc - nc:yc + nc, :] = layer_mask
            elif n % 2 == 1:
                new_layer[xc - mc:xc + mc, yc - nc - 1:yc + nc, :] = layer_mask
            else:
                new_layer[xc - mc:xc + mc, yc - nc:yc + nc, :] = layer_mask
            self.combine_images(new_layer)
        if self.show_plots: self.make_plot(self.current_image)

    def select_random(self, attribute, attribute_remaining):
        output = random.choice(attribute)
        if attribute_remaining[output] <= 0:
            output = 'none'
        return output

    def reset_nft(self):
        self.background = 1 * np.ones((self.shape[0], self.shape[1], 4)).astype('float32')
        self.current_image = self.background.copy()

p = NFTGenerator()
#p.show_plots = False
p.create_background('red')
p.add_layer(p.minecraft['default'], p.center)
p.add_layer(p.helmet['diamond'], p.helmet_center)
p.add_layer(p.chest['diamond'], p.chest_center)
p.add_layer(p.pants['diamond'], p.pants_center)
p.make_plot(p.current_image)
