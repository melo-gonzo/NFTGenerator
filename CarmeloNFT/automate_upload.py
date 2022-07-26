import numpy as np
import pyautogui
import time

csv = open('meta.csv', 'r').read()
csv = csv.split('\n')[:-1]
csv = [c.split(',') for c in csv]

url = 'https://opensea.io/collection/crypto-poopies-collection'

x, y = 2683, 225
pyautogui.moveTo(x, y, duration=0.1)
pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
pyautogui.typewrite(url, interval=0.05)
pyautogui.press("enter")
time.sleep(5)

poopies_uploaded = [num for num in np.arange(1, 180)]
poop_idx = len(poopies_uploaded) + 1
start_time = time.time()
times = []
measure_now = False
while poop_idx <= 383:
    print('Poopie number %i of %i' % (poop_idx, 383))
    if poop_idx not in poopies_uploaded:

        x, y = 3650, 550
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
        time.sleep(2)

        # x, y = 3793, 375
        # pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
        # time.sleep(0.2)

        x, y = 2484, 1052
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
        time.sleep(0.2)
        # if len(poopies_uploaded) > 0:
        #     for k in range(len(poopies_uploaded)):
        #         time.sleep(0.1)
        #         pyautogui.press("down")

        x, y = 3537, 659
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

        time.sleep(0.1)
        x, y = 2778, 750
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
        time.sleep(0.1)
        pyautogui.typewrite("crypto_poopie_" + str(poop_idx) + ".png", interval=0.05)
        time.sleep(0.1)
        x, y = 3652, 659
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

        time.sleep(0.1)

        # time.sleep(0.1)
        # pyautogui.press("enter")
        # time.sleep(0.1)

        time.sleep(0.1)
        x, y = 2210, 1800
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
        time.sleep(0.1)

        name = "Crypto Poopie #" + str(poop_idx)
        pyautogui.typewrite(name, interval=0.05)
        time.sleep(0.1)
        x, y = 2060, 1803
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
        time.sleep(0.1)
        c = 0
        while c < 10:
            time.sleep(0.1)
            pyautogui.scroll(-1)
            c += 1

        x, y = 2166, 1361
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

        Text = "Crypto Poopie #" + str(poop_idx)
        pyautogui.typewrite(Text, interval=0.05)

        x, y = 3610, 1935
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
        added = 0
        for idx, k in enumerate(csv[poop_idx - 1][1:]):
            print(k)
            if idx == 0 and k != 'none':
                x, y = 2591, int(1022 + added * 150)
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
                pyautogui.typewrite("Color", interval=0.05)
                x, y = 3187, int(1022 + added * 150)
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
                pyautogui.typewrite(k, interval=0.05)
                added += 1
                x, y = 2552, int(1022 + added * 150)
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
            elif idx == 1 and k != 'none':
                x, y = 2591, int(1022 + added * 150)
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
                pyautogui.typewrite("Eyes", interval=0.05)
                x, y = 3187, int(1022 + added * 150)
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
                pyautogui.typewrite(k, interval=0.05)
                added += 1
                x, y = 2552, int(1022 + added * 150)
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
            elif idx == 2 and k != 'none':
                x, y = 2591, int(1022 + added * 150)
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
                pyautogui.typewrite("Hat", interval=0.05)
                x, y = 3187, int(1022 + added * 150)
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
                pyautogui.typewrite(k, interval=0.05)
                added += 1
                x, y = 2552, int(1022 + added * 150)
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
            elif idx == 3 and k != 'none':
                x, y = 2591, int(1022 + added * 150)
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
                pyautogui.typewrite("Face", interval=0.05)
                x, y = 3187, int(1022 + added * 150)
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
                pyautogui.typewrite(k, interval=0.05)
                added += 1
                x, y = 2552, int(1022 + added * 150)
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
            y_last = y

        x, y = 2852, int(y_last + 150 * 2.45)
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

        c = 0
        while c < 20:
            time.sleep(0.1)
            pyautogui.scroll(-1)
            c += 1

        x, y = 2433, 1395
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

        x, y = 2458, 1521
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

        x, y = 2220, 2038
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

        time.sleep(3)

        x, y = 3380, 607
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

        x, y = 3580, 2327
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

        time.sleep(3)

        x, y = 2377, 859
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

        x, y = 2708, 1020
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
        time.sleep(0.1)
        pyautogui.typewrite("0.005", interval=0.1)
        time.sleep(0.1)
        x, y = 2907, 1939
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
        time.sleep(1)
        if measure_now:
            times.append(time.time() - start_time)
        measure_now = True
        while time.time() - start_time < 48:
            time.sleep(0.01)

        print("Avg time: %f" % np.round(np.mean(times), 2))
        start_time = time.time()

        x, y = 2452, 1138
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
        # c = 0
        # while c < 5:
        #     time.sleep(0.1)
        #     pyautogui.scroll(-1)
        #     c += 1
        #
        # x, y = 2382, 1893
        # pyautogui.moveTo(x, y, duration=0.1)
        # pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')

        time.sleep(5)

        x, y = 2683, 225
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x=x, y=y, clicks=1, interval=0.1, button='left')
        pyautogui.typewrite(url, interval=0.05)
        pyautogui.press("enter")
        time.sleep(5)
        poopies_uploaded.append(poop_idx)
        poop_idx += 1
    else:
        poop_idx += 1
