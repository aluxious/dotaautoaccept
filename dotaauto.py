# pip install pyautogui
# pip install opencv-python

import pyautogui
from time import sleep
import os

BUTTON_ACCEPT = "accept_button.png"
BUTTON_READY = "ready_button.png"
BUTTON_CONTINUE = "continue_button.png"
if not (os.path.exists(".\\"+BUTTON_ACCEPT) and os.path.exists(".\\"+BUTTON_READY) and os.path.exists(".\\"+BUTTON_CONTINUE)):
    print('Missing image file(s)!!!')
    exit()

width_acc, height_acc = pyautogui.size()
center_acc = pyautogui.center((0, 0, width_acc, height_acc))
isfound_accept = None

width_rdy, height_rdy = pyautogui.size()
center_rdy = pyautogui.center((-180, 120, width_rdy, height_rdy))
isfound_ready = None

width_con, height_con = pyautogui.size()
center_con = pyautogui.center((0, 505, width_rdy, height_rdy))
isfound_continue = None

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
    isfound_continue = pyautogui.locateOnScreen(BUTTON_CONTINUE, grayscale=False, confidence=0.9)
    if isfound_continue:
        print ('Found continue button')
        pyautogui.click(center_con)
        sleep(5)      
    sleep(1)
