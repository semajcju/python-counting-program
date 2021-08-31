import pyautogui as auto
import time


num = input('please input number you want to start counting from: ')
endnum = input('please input the number you would like to stop counting from: ')

print('beginning count in ')
print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)


while True:
    num = str(num)
    auto.typewrite(num)
    num = int(num)
    num = num + 1
    auto.press('enter')
    time.sleep(1.7)
    if num == endnum:
        break
