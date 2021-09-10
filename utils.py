# import matplotlib.pyplot as plt
# import numpy as np
# import cv2
#
#
# def get_bounding_box(input_image):
#     threshold = 127
#     if isinstance(input_image, str):
#         img = plt.imread(input_image)
#     else:
#         img = input_image.copy()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     ret, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
#     contours, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     # note that h goes with x and w with y
#     x, y, w, h = cv2.boundingRect(contours[1])
#     # for c in contours:
#     #     rect = cv2.boundingRect(c)
#     #     x, y, w, h = rect
#     #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     #     plt.imshow(img)
#     #     plt.show()
#     return (x, y, w, h), thresh
#
#
# def get_poop_mask(base_folder, save_folder, input_image):
#     img = plt.imread(base_folder + input_image).astype(uint8)
#     # img = cv2.GaussianBlur(img, (5, 5), 0)
#     img = cv2.resize(img, (50, 50))
#     img = np.pad(img, ((10, 10), (10, 10), (0, 0)), 'constant', constant_values=(255, 255))
#     (x, y, w, h), thresh = get_bounding_box(img)
#     img = img[:, :, ::-1]
#     alpha_channel = 255 * np.zeros(img[:, :, 0].shape, dtype=img.dtype)
#     alpha_channel[np.nonzero(thresh == 0)] = 255
#     img = cv2.merge((img, alpha_channel))
#     print(img.shape)
#     cv2.imwrite(save_folder + input_image.split('.')[0] + '_mask.png', img)
#
#
# def get_cowboy_hat_mask(base_folder, save_folder, input_image):
#     img = plt.imread(base_folder + input_image)
#     img = img[10:-10, 10:-10, :]
#     img = cv2.GaussianBlur(img, (5, 5), 0)
#     # img = cv2.resize(img, (50, 50))
#     # img = np.pad(img, ((10, 10), (10, 10), (0, 0)), 'constant', constant_values=(255, 255))
#     (x, y, w, h), thresh = get_bounding_box(img)
#     img = img[y:y + h, x:x + w, :]
#     scale = 20
#     new_h = int(img.shape[0] / scale)
#     new_w = int(img.shape[1] / scale)
#     pad_h = int((70 - new_h) / 2)
#     pad_w = int((70 - new_w) / 2)
#     if new_h % 2 == 1:
#         new_h += 1
#     if new_w % 2 == 1:
#         new_w += 1
#     img = cv2.resize(img, (new_w, new_h))
#
#     v_offset = 20
#     print(img.shape)
#     # img = np.pad(img, ((1, 100), (1, 100), (0, 0)), 'constant', constant_values=(255, 255))
#     img = np.pad(img, ((pad_h - v_offset, pad_h + v_offset), (pad_w, pad_w), (0, 0)), 'constant',
#                  constant_values=(255, 255))
#     (x, y, w, h), thresh = get_bounding_box(img)
#     img = img[:, :, ::-1]
#     alpha_channel = 255 * np.zeros(img[:, :, 0].shape, dtype=img.dtype)
#     alpha_channel[np.nonzero(thresh == 0)] = 255
#     img = cv2.merge((img, alpha_channel))
#     print(img.shape)
#     cv2.imwrite(save_folder + input_image.split('.')[0] + '_mask.png', img)
#
#
# def get_top_hat_mask(base_folder, save_folder, input_image):
#     img = plt.imread(base_folder + input_image) * 255
#     img = img.astype('uint8')
#     img = cv2.GaussianBlur(img, (5, 5), 0)
#     (x, y, w, h), thresh = get_bounding_box(img)
#     img = img[y:y + h, x:x + w, :]
#     scale = 50
#     new_h = int(img.shape[0] / scale)
#     new_w = int(img.shape[1] / scale)
#     pad_h = int((70 - new_h) / 2)
#     pad_w = int((70 - new_w) / 2)
#     if new_h % 2 == 1:
#         new_h += 1
#     if new_w % 2 == 1:
#         new_w += 1
#
#     img = cv2.resize(img, (new_w, new_h))
#
#     v_offset = 20
#     print(img.shape)
#     # img = np.pad(img, ((1, 100), (1, 100), (0, 0)), 'constant', constant_values=(255, 255))
#     img = np.pad(img, ((pad_h - v_offset, pad_h + v_offset), (pad_w, pad_w), (0, 0)), 'constant',
#                  constant_values=(255, 255))
#     (x, y, w, h), thresh = get_bounding_box(img)
#     img = img[:, :, ::-1]
#     alpha_channel = 255 * np.zeros(img[:, :, 0].shape, dtype=img.dtype)
#     alpha_channel[np.nonzero(thresh == 0)] = 255
#     img = cv2.merge((img, alpha_channel))
#     print(img.shape)
#     cv2.imwrite(save_folder + input_image.split('.')[0] + '_mask.png', img)
#
#
# base_folder = '/home/carmelo/Projects/NFTGenerator/'
# save_folder = base_folder + 'Masks/'
# input_image = 'top_hat.png'
# # input_image = 'cowboy_hat.jpg'
# # get_poop_mask(base_folder, save_folder, input_image)
# # get_cowboy_hat_mask(base_folder, save_folder, input_image)
# get_top_hat_mask(base_folder, save_folder, input_image)
# img1 = plt.imread(save_folder + 'poop_mask.png')
# img2 = plt.imread(save_folder + 'top_hat_mask.png')
#
# new_img = np.zeros(img1.shape, dtype=img1.dtype)
# for m in range(img1.shape[0]):
#     for n in range(img1.shape[1]):
#         if img1[m, n, -1] != 0 and img2[m, n, -1] == 0:
#             new_img[m, n, :] = img1[m, n, :]
#         else:
#             new_img[m, n, :] = img2[m, n, :]
#
# plt.imshow(new_img)
# plt.show()

from numpy import random as rnd


def hex_to_RGB(hex):
    ''' "#FFFFFF" -> [255,255,255] '''
    # Pass 16 to the integer function for change of base
    return [int(hex[i:i + 2], 16) for i in range(1, 6, 2)]


def RGB_to_hex(RGB):
    ''' [255,255,255] -> "#FFFFFF" '''
    # Components need to be integers for hex to make sense
    RGB = [int(x) for x in RGB]
    return "#" + "".join(["0{0:x}".format(v) if v < 16 else
                          "{0:x}".format(v) for v in RGB])


def color_dict(gradient):
    ''' Takes in a list of RGB sub-lists and returns dictionary of
      colors in RGB and hex form for use in a graphing function
      defined later on '''
    return {"hex": [RGB_to_hex(RGB) for RGB in gradient],
            "r": [RGB[0] for RGB in gradient],
            "g": [RGB[1] for RGB in gradient],
            "b": [RGB[2] for RGB in gradient]}


def linear_gradient(start_hex, finish_hex="#FFFFFF", n=10):
    ''' returns a gradient list of (n) colors between
      two hex colors. start_hex and finish_hex
      should be the full six-digit color string,
      inlcuding the number sign ("#FFFFFF") '''
    # Starting and ending colors in RGB form
    s = hex_to_RGB(start_hex)
    f = hex_to_RGB(finish_hex)
    # Initilize a list of the output colors with the starting color
    RGB_list = [s]
    # Calcuate a color at each evenly spaced value of t from 1 to n
    for t in range(1, n):
        # Interpolate RGB vector for color at the current value of t
        curr_vector = [
            int(s[j] + (float(t) / (n - 1)) * (f[j] - s[j]))
            for j in range(3)
        ]
        # Add it to our list of output colors
        RGB_list.append(curr_vector)

    return color_dict(RGB_list)


def rand_hex_color(num=1):
    ''' Generate random hex colors, default is one,
        returning a string. If num is greater than
        1, an array of strings is returned. '''
    colors = [
        RGB_to_hex([x * 255 for x in rnd.rand(3)])
        for i in range(num)
    ]
    if num == 1:
        return colors[0]
    else:
        return colors


def polylinear_gradient(colors, n):
    ''' returns a list of colors forming linear gradients between
        all sequential pairs of colors. "n" specifies the total
        number of desired output colors '''
    # The number of colors per individual linear gradient
    n_out = int(float(n) / (len(colors) - 1))
    # returns dictionary defined by color_dict()
    gradient_dict = linear_gradient(colors[0], colors[1], n_out)

    if len(colors) > 1:
        for col in range(1, len(colors) - 1):
            next = linear_gradient(colors[col], colors[col + 1], n_out)
            for k in ("hex", "r", "g", "b"):
                # Exclude first point to avoid duplicates
                gradient_dict[k] += next[k][1:]

    return gradient_dict


# colors_in = [(204, 153, 210),
#              (158, 193, 207),
#              (158, 224, 158),
#              (253, 253, 151),
#              (254, 177, 68),
#              (255, 102, 99)]
#
# colors_in = [RGB_to_hex(color) for color in colors_in]
# #
# colors_out = polylinear_gradient(colors_in, 145)
# print(len(colors_out['hex']))
# a = 1