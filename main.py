import pyautogui as auto
import time

num = str(160134)

time.sleep(5)

while True:
    num = str(num)
    auto.typewrite(num)
    num = int(num)
    num = num + 1
    auto.press('enter')
    time.sleep(1.7)
    if num == 170001:
        break
60158
160159
160160
160161
