import pyautogui

myscreen = pyautogui.screenshot(region=(1290,300, 250, 580))

myscreen.save("test.png")