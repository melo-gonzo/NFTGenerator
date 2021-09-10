import matplotlib.pyplot as plt
from utils import *
import numpy as np
import random
import copy
import os


class NFTGenerator:
    def __init__(self):
        self.show_plots = True
        self.mask_dir = '/home/carmelo/Projects/NFTGenerator/Masks/'
        self.shape = (70, 70)
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

        self.combinations = (len(self.eyes) - 1) * len(self.hats) * len(self.masks) * len(self.backgrounds)
        print(self.combinations)

    def combine_images(self, input_image):
        for m in range(input_image.shape[0]):
            for n in range(input_image.shape[1]):
                if self.current_image[m, n, -1] != 0 and input_image[m, n, -1] != 0:
                    self.current_image[m, n, :] = input_image[m, n, :]

    def make_plot(self, input_image):
        fig = plt.figure(figsize=(10, 10))
        plt.imshow(input_image)
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
        # print(layer_mask)
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
p.show_plots = False
# p.create_background('rainbow')
# p.add_layer(p.base['base'], p.center)
# p.add_layer(p.hats['spinner'], p.hats_center)
# p.add_layer(p.masks['tongue'], p.masks_center)
# p.add_layer(p.eyes['sunglasses'], p.glasses_center)
# p.make_plot(p.current_image)

### Rarity Def's, Backgrounds specify max number of NFT's
backgrounds = {'purple': 100,
               'blue': 100,
               'green': 100,
               'yellow': 100,
               'orange': 100,
               'red': 100,
               'rainbow': 20}
background_type = list(backgrounds.keys())

backgrounds_remaining = copy.deepcopy(backgrounds)

eyes = {'ether': 75,
        'bitcoin': 75,
        'doge': 75,
        'sunglasses': 50,
        'none': 0}
eye_type = list(eyes.keys())

eyes_remaining = copy.deepcopy(eyes)

hats = {'cowboy': 75,
        'top': 100,
        'baseball': 50,
        'spinner': 30,
        'halo': 50,
        'steam': 50,
        'santa': 50,
        'none': 0}

hat_type = list(hats.keys())

hats_remaining = copy.deepcopy(hats)

faces = {'covid': 75,
         'lips': 75,
         'tongue': 75,
         'none': 0}

face_type = list(faces.keys())

faces_remaining = copy.deepcopy(faces)

types_made = []
total_made = 0
attempts = 0
while total_made < np.sum([b for b in backgrounds.values()]):
    p.reset_nft()
    layer_stack = []
    background_ = p.select_random(background_type, backgrounds_remaining)
    while background_ == 'none':
        background_ = p.select_random(background_type, backgrounds_remaining)
    eyes_ = p.select_random(eye_type, eyes_remaining)
    hat_ = p.select_random(hat_type, hats_remaining)
    face_ = p.select_random(face_type, faces_remaining)
    if eyes_ != 'none' and face_ != 'none' and face_ != 'tongue':
        base_ = 'no_eyes_no_mouth'
    elif eyes_ != 'none':
        base_ = 'no_eyes'
    elif face_ != 'none' and face_ != 'tongue':
        base_ = 'no_mouth'
    else:
        base_ = 'base'

    layer_stack = [background_, base_, eyes_, hat_, face_]
    cp_name = '-'.join(layer_stack)
    if cp_name not in types_made:
        if background_ != 'none':
            p.create_background(background_)
        if base_ != 'none':
            p.add_layer(p.base[base_], p.center)
        if eyes_ != 'none':
            if eyes_ == 'sunglasses':
                p.add_layer(p.eyes[eyes_], p.glasses_center)
            else:
                p.add_layer(p.eyes[eyes_], p.eyes_center)
        if hat_ != 'none':
            p.add_layer(p.hats[hat_], p.hats_center)
        if face_ != 'none':
            p.add_layer(p.masks[face_], p.masks_center)

        # p.make_plot(p.current_image)
        types_made.append(cp_name)
        backgrounds_remaining[background_] -= 1
        eyes_remaining[eyes_] -= 1
        hats_remaining[hat_] -= 1
        faces_remaining[face_] -= 1
        total_made += 1
        plt.imsave('CryptoPoopiesBackup/crypto_poopie_' + cp_name + '_' + str(total_made) + '.png', p.current_image)
        plt.imsave('CryptoPoopies/crypto_poopie_' + str(total_made) + '.png', p.current_image)
        print(cp_name)
    else:
        attempts += 1
        if attempts > 10000:
            break
