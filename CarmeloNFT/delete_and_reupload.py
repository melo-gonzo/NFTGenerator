import numpy as np
import pyautogui
import time


def record_mouse_location():
    while True:
        print(pyautogui.position())
        time.sleep(1)


def click(x, y, sleep, do_text=False, text='', do_enter=False):
    pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
    time.sleep(sleep)
    if do_text:
        pyautogui.typewrite(text, interval=0.05)
    if do_enter:
        pyautogui.press("enter")
    if do_text and do_enter:
        time.sleep(sleep)


def scroll(scrolls):
    c = 0
    while c < scrolls:
        time.sleep(0.05)
        pyautogui.scroll(-1)
        c += 1


if __name__ == '__main__':
    # record_mouse_location()
    total = 0
    while True:
        total += 1
        steps = ['url', 'click first poop', 'click edit', 'scroll', 'click delete', 'confirm delete']
        locs = [(1264, 223),
                (1190, 2279),
                (2345, 547),
                (-1, -1),
                (2582, 2035),
                (2000, 975)]
        first_poop = [(1190, 2279),
                      (1925, 2317),
                      (2656, 2310),
                      (3420, 2288)]
        sleep = [4, 4, 4, 0.5, 0.5, 0.5]
        url1 = 'https://opensea.io/collection/crypto-poopies-collection'
        text_steps = [0]
        step = 0
        poop_idx = total % 4
        for x, y in locs:
            if step == 1:
                x, y = first_poop[poop_idx]
            print(steps[step] + '\n')
            if x != -1 and y != -1:
                if step in text_steps:
                    click(x, y, sleep[step], do_text=True, text=url1, do_enter=True)
                else:
                    click(x, y, sleep[step])
            else:
                scroll(25)
            step += 1

    # record_mouse_location()
