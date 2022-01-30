# pip install pyautogui
# pip install opencv-python

import pyautogui
from time import sleep
import os

BUTTON_ACCEPT = "accept_button.png"
BUTTON_READY = "ready_button.png"
BUTTON_PARTY = "party_button.png"
BUTTON_CONTINUE = "continue_button.png"
BUTTON_CONTINUE_RED = "continue_button_red.png"

if not (os.path.exists(".\\"+BUTTON_ACCEPT) and os.path.exists(".\\"+BUTTON_READY) and os.path.exists(".\\"+BUTTON_CONTINUE) 
and os.path.exists(".\\"+BUTTON_CONTINUE_RED) and os.path.exists(".\\"+BUTTON_PARTY)):
    print('Missing image file(s)!!!')
    exit()

def locate_and_click(button_file, button_name):
    button_loc = pyautogui.locateOnScreen(button_file, grayscale=False, confidence=0.9)
    if button_loc:
        print ('Found ' + button_name + ' button')
        pyautogui.click(button_loc)
        sleep(5)

print ('Waiting to accept')
while True:
    locate_and_click(BUTTON_ACCEPT, "accept")
    locate_and_click(BUTTON_READY, "ready")
    locate_and_click(BUTTON_PARTY, "accept party")
    locate_and_click(BUTTON_CONTINUE, "continue")
    locate_and_click(BUTTON_CONTINUE_RED, "red continue")
    sleep(1)
