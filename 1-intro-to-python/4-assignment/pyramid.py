import pyautogui
from time import sleep


n = int(input())
c = 1
sleep(3)
for i in range(0, n):
    for i in range(0, c):
        pyautogui.write('#')
    pyautogui.press('enter')
    c += 1
