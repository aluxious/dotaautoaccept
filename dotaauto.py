# pip install pyautogui
# pip install opencv-python

import pyautogui
from time import sleep
import os

BUTTON_ACCEPT = "accept_button.png"
BUTTON_READY = "ready_button.png"
if not (os.path.exists(".\\"+BUTTON_ACCEPT) and os.path.exists(".\\"+BUTTON_READY)):
    print('Missing image file(s)!!!')
    exit()

width_acc, height_acc = pyautogui.size()
center_acc = pyautogui.center((0, 0, width_acc, height_acc))
isfound_accept = None

width_rdy, height_rdy = pyautogui.size()
center_rdy = pyautogui.center((-180, 120, width_rdy, height_rdy))
isfound_ready = None

print ('Waiting to accept')
while True:
    isfound_accept = pyautogui.locateOnScreen(BUTTON_ACCEPT, grayscale=False, confidence=0.9)
    if isfound_accept:
        print ('Found accept button')
        pyautogui.click(center_acc)
        sleep(5)
    isfound_ready = pyautogui.locateOnScreen(BUTTON_READY, grayscale=False, confidence=0.9)
    if isfound_ready:
        print ('Found ready button')
        pyautogui.click(center_rdy)
        sleep(5)
    sleep(1)
