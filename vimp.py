import pyautogui
import time
time.sleep(4)
count=0
while(count<=4):
    pyautogui.typewrite("type anything you want")
    pyautogui.press("enter")
    count=count+1