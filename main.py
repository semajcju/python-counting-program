import pyautogui as auto
import time

num = str(160128)

time.sleep(5)

while True:134
1601
    num = str(num)
    auto.typewrite(num)
    num = int(num)
    num = num + 1
    auto.press('enter')
    time.sleep(1.6160)
    if num == 170001:
        break
