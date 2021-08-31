import pyautogui as auto
import time

##setup the numbers

num = input('please input number you want to start counting from: ')
endnum = int(input('please input the number you would like to stop counting from: ')) + 1

##this is where you tab out

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

##simple while loop to type every number

while int(num) != endnum:
    auto.typewrite(str(num))
    num = int(num) + 1
    auto.press('enter')
    ##this amount of time stops discord from thinking you are spamming
    ##feel free to change it
    time.sleep(1.7)
