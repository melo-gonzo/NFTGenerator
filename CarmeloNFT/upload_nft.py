import numpy as np
import pyautogui
import time
import os


def record_mouse_location():
    while True:
        print(pyautogui.position())
        time.sleep(0.5)


def click(x, y, sleep, do_enter=False):
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
    pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
    time.sleep(0.1)
    if do_enter:
        time.sleep(0.2)
        pyautogui.press("enter")
        print('pressing enter')
    time.sleep(sleep)


def type(sleep, text='', do_enter=False):
    if 'http' in text:
        pyautogui.hotkey('ctrl', 'a')
        print('hotkey')
    pyautogui.typewrite(text, interval=0.05)
    if do_enter:
        time.sleep(0.2)
        pyautogui.press("enter")
        print('pressing enter')

    time.sleep(sleep)


def scroll(scrolls):
    c = 0
    while c < scrolls:
        time.sleep(0.05)
        pyautogui.scroll(-1)
        c += 1


def do_properties(properties):
    type_ = [2550, 1020]
    name_ = [3150, 1020]
    add_ = [2550, 1160]
    y_bonus = 40
    for idx, key in enumerate(properties.keys()):
        click(type_[0], type_[1] + idx * y_bonus, 0.1, do_enter=enter)
        type(0.1, key)
        click(name_[0], name_[1] + idx * y_bonus, 0.1, do_enter=enter)
        type(0.1, properties[key])
        click(add_[0], add_[1] + idx * y_bonus, 0.1, do_enter=enter)
        # pass


if __name__ == '__main__':
    # record_mouse_location()
    files = os.listdir('DigitsOfPi/')
    complete = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    total = len(complete)
    all_times = []
    for idx in range(len(files)):
        go_on = False
        for file in files:
            idxs = len(str(idx)) + 1
            if str(idx) + "_" == file[:idxs] and idx not in complete:
                go_on = True
                break
        if not go_on:
            continue
        print("File: %s" % file)
        start_time = time.time()
        steps = {'click_url': (2350, 227),
                 'type_url_enter': 'https://opensea.io/collection/digits-of-pi-collection',
                 'click_add_item': (3648, 538),
                 'click_drag_and_drop': (2471, 1085),
                 'click_search': (3537, 655),
                 'type_file_enter': file,
                 'click_name': (2171, 1803),
                 'type_name': 'Pi Digits NFT #' + str(int(file.split('_')[0]) + 1),
                 'scroll_down_10': 10,
                 'click_description': (2171, 1364),
                 'type_description': 'Pi Digits ' + str(total * 10 + 1) + '-' + str((total + 1) * 10),
                 'scroll_down_20': 20,
                 'click_create': (2218, 2042),
                 'click_exit': (3382, 610),
                 'click_sell': (3574, 2329),
                 'click_amount': (2665, 1025),
                 'type_price': '0.01',
                 'click_complete_listing': (2903, 1946),
                 'click_sign': (2447, 1135),
                 'click_sign_confirm': (3638, 1344)
                 }
        # sleep = [5] * len(steps)
        fille = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        sleep = [1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1,   3,  4,  5, 5,   5, 3,  1.5, 2,  5]
        text_steps = [0, 4, 6, 9]
        step = 0
        for step_num, key in enumerate(steps.keys()):
            print("Step number %i is %s" % (step_num, key))
            if step >= 0:
                if 'click' in key:
                    x, y = steps[key]
                    enter = True if 'enter' in key else False
                    click(x, y, sleep[step], do_enter=enter)
                if 'type' in key:
                    enter = True if 'enter' in key else False
                    type(sleep[step], steps[key], do_enter=enter)
                if 'scroll' in key:
                    scroll(steps[key])
                    time.sleep(sleep[step])
                if 'properties' in key:
                    do_properties(steps[key])
            step += 1
        total += 1
        all_times.append(time.time() - start_time)
        print("Avg. Time: %f" % np.round(np.mean(all_times), 3))


