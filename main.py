import pyautogui as auto
import time

num = str(157293159679)

time.sleep(5)

while True:
    num = str(num)
    auto.typewrite(num)
    num = int(num)
    num = num + 1
    auto.press('enter')
    time.sleep(3)