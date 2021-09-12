import matplotlib.pyplot as plt
from utils import *
import numpy as np
import random
import copy
import os

from nft_generator import NFTGenerator

p = NFTGenerator()
p.show_plots = False

### Rarity Def's, Backgrounds specify max number of NFT's
# backgrounds = {'purple': 100,
#                'blue': 100,
#                'green': 100,
#                'yellow': 100,
#                'orange': 100,
#                'red': 100,
#                'rainbow': 20}
# background_type = list(backgrounds.keys())
#
# backgrounds_remaining = copy.deepcopy(backgrounds)
#
# helmet = {'leather': 55,
#         'gold': 45,
#         'none': 0}
# helmet_type = list(helmet.keys())
# helmet_remaining = copy.deepcopy(helmet)
#
# chest = {'leather': 50,
#         #'gold': 50,
#         'none': 50}
# chest_type = list(chest.keys())
# chest_remaining = copy.deepcopy(chest)
#
# pants = {'leather': 50,
#         #'gold': 50,
#         'none': 50}
# pants_type = list(pants.keys())
# pants_remaining = copy.deepcopy(pants)
#
# eyes = {'ether': 75,
#         'bitcoin': 75,
#         'doge': 75,
#         'sunglasses': 50,
#         'none': 0}
# eye_type = list(eyes.keys())
#
# eyes_remaining = copy.deepcopy(eyes)
#
# hats = {'cowboy': 75,
#         'top': 100,
#         'baseball': 50,
#         'spinner': 30,
#         'halo': 50,
#         'steam': 50,
#         'santa': 50,
#         'none': 0}
#
# hat_type = list(hats.keys())
#
# hats_remaining = copy.deepcopy(hats)
#
# faces = {'covid': 75,
#          'lips': 75,
#          'tongue': 75,
#          'none': 0}
#
# face_type = list(faces.keys())
#
# faces_remaining = copy.deepcopy(faces)
#
# types_made = []
# total_made = 0
# attempts = 0
# while total_made < np.sum([b for b in backgrounds.values()]):
#     p.reset_nft()
#     layer_stack = []
#     background_ = p.select_random(background_type, backgrounds_remaining)
#     while background_ == 'none':
#         background_ = p.select_random(background_type, backgrounds_remaining)
#
#     helmet_ = p.select_random(helmet_type, helmet_remaining)
#     chest_ = p.select_random(chest_type, chest_remaining)
#     pants_ = p.select_random(pants_type, pants_remaining)
#     base_ = 'default' #default character
#
#     #if helmet_ != 'none' and chest_ != 'none' and chest != 'none':
#     #    base_ = 'no_eyes_no_mouth'
#     #elif eyes_ != 'none':
#     #    base_ = 'no_eyes'
#     #elif face_ != 'none' and face_ != 'tongue':
#     #    base_ = 'no_mouth'
#     #else:
#     #    base_ = 'base'
#
#     layer_stack = [background_, helmet_, chest_, pants_]
#     cp_name = '-'.join(layer_stack)
#     if cp_name not in types_made:
#         if background_ != 'none':
#             p.create_background(background_)
#         if base_ != 'none':
#             p.add_layer(p.minecraft[base_], p.center)
#         if helmet_ != 'none':
#             if helmet_ == 'sunglasses':
#                 p.add_layer(p.helmet[helmet_], p.helmet_center)
#             else:
#                 p.add_layer(p.helmet[helmet_], p.helmet_center)
#         if chest_ != 'none':
#             p.add_layer(p.chest[chest_], p.chest_center)
#         if pants_ != 'none':
#             p.add_layer(p.pants[pants_], p.pants_center)
#
#         # p.make_plot(p.current_image)
#         types_made.append(cp_name)
#         backgrounds_remaining[background_] -= 1
#         helmet_remaining[helmet_] -= 1
#         chest_remaining[chest_] -= 1
#         pants_remaining[pants_] -= 1
#         total_made += 1
#         plt.imsave("D:\\Git\\nftgen\\NFTGenerator\\final_images\\" + cp_name + '_' + str(total_made) + '.png', p.current_image)
#         plt.imsave("D:\\Git\\nftgen\\NFTGenerator\\final_images\\" + str(total_made) + '.png', p.current_image)
#         print(cp_name)
#     else:
#         attempts += 1
#         if attempts > 10000:
#             break
