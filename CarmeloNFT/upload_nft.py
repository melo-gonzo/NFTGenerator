import numpy as np
import pyautogui
import time
import os
import random
import csv
import pandas as pd

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

def write_to_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
    csvfile.close()

def add_to_csv(l,filename):
    with open(filename, 'a+', newline='') as csvfile:
        write_row = csv.writer(csvfile)
        write_row.writerows([l])
    csvfile.close()

def csv_to_list(filename):
    df = pd.read_csv(filename,header=None)
    data = df[0].tolist()
    return data

if __name__ == '__main__':
    #record_mouse_location()
    os.chdir('C:\\Users\\Ljubo\\Desktop\\nft\\larger\\')
    csv_filename = 'test.csv'
    NUMBER_CREATED = 38
    if os.path.isfile(csv_filename):
        print('Completed List exists...loading it.')
        complete = csv_to_list(csv_filename)
    else:
        write_to_csv(csv_filename)
        complete = [26,81,19,175,31,4,22,31,29,73,80,6,209,15,150,170,38,122,227,221,128,20,16,83,8,5,10,7,23,40,4,232,216,64,10,3,204,231,240,37,14,26,198,12,108]
        for row in complete:
            print(row)
            add_to_csv([row],csv_filename)
    print(complete)
    files = os.listdir('C:\\Users\\Ljubo\\Desktop\\nft\\larger\\')
    random.shuffle(files)
    total = len(complete)
    all_times = []
    go_on = True
    # for idx in range(len(files)):
    idx=1
    for file in files:
        if file.endswith(".csv"):
            go_on = False
            break
        else:
            if int(file.split('-')[-1].split('_')[1].split('.')[0]) not in complete:
                go_on = True
            else:
                go_on = False
        
        if go_on == True:
            print("File: %s" % file)
            start_time = time.time()
            steps = {'click_url': (1634, 61),
                        'type_url_enter': 'https://opensea.io/collection/crypto-minecraft-collection',
                        'click_add_item': (2488, 218),
                        'click_drag_and_drop': (1709, 509),
                        'click_search': (1503, 538),
                        'type_file_enter': file,
                        'click_name': (1629, 847),
                        'type_name': 'Crypto Minecraft #' + str(int(idx) + NUMBER_CREATED),
                        'scroll_down_100': 100,
                        #'click_description': (2171, 1364),
                        #'type_description': 'Pi Digits ' + str(total * 10 + 1) + '-' + str((total + 1) * 10),
                        'click_properties': (2272,1361),
                        'type_background': 'Background',
                        'click_background_box': (1987,483),
                        'type_background_color': '{0}'.format(str(file.split('-')[0]).capitalize()),
                        'click_add_more1': (1752,552),
                        'click_helmet_box': (1762,553),
                        'type_helmet': 'Helmet',
                        'click_helmet_color': (2000,553),
                        'type_helmet_color': '{0}'.format(str(file.split('-')[1]).capitalize()),
                        'click_add_more2': (1743,621),
                        'click_chest_box': (1800,624),
                        'type_chest': 'Chest plate',
                        'click_chest_color': (1996,627),
                        'type_chest_color': '{0}'.format(str(file.split('-')[2]).capitalize()),
                        'click_add_more3': (1756,689),
                        'click_pants_box': (1776,700),
                        'type_pants': 'Pants',
                        'click_pants_color': (1993,694),
                        'type_pants_color': '{0}'.format(str(file.split('-')[3].split('_')[0]).capitalize()),
                        'click_save_prop': (1929,860),
                        'click_to_end': (2548,1371),
                        'click_create': (1571, 1243),
                        'click_exit': (2160, 276),
                        'click_sell': (2399, 215),
                        'click_amount': (1804, 485),
                        'type_price': '0.004',
                        'click_complete_listing': (1918, 938),
                        'click_sign': (1696, 539),
                        'click_sign_confirm': (2486, 557)
                        }
            sleep = [3] * len(steps)
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
                step += 1
            total += 1
            idx += 1
            all_times.append(time.time() - start_time)
            print("Avg. Time: %f" % np.round(np.mean(all_times), 3))
            print('Adding {0} to completed list.'.format(int(file.split('-')[-1].split('_')[1].split('.')[0])))
            add_to_csv([int(file.split('-')[-1].split('_')[1].split('.')[0])],csv_filename)

