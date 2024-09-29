import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\OG Fishies\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
from PIL import Image
import pyautogui
import json
from time import sleep

myBotId = 1
config = "--psm 12"

def takescreenshot():
    myscreen = pyautogui.screenshot(region=(1290,300, 250, 580))
    myscreen.save("image1.png")

def gay():
    img = Image.open("image1.png")
    text: dict = pytesseract.image_to_data(img, config=config, output_type=Output.DICT)
    text2 = []
    for q in text["text"]:
        if q != "":
            if q != "SCORE":
                text2.append(q)
    if len(text2) == 2:
        timer = "00:00"
        blue = text2[0]
        red = text2[1]
    elif len(text2) == 3:
        timer = text2[0]
        blue = text2[1]
        red = text2[2]
    else:
        timer = "00:00"
        blue = "0"
        red = "0"
    print(f"{timer} {blue} {red}")
    with open("data.json") as f:
        data = json.load(f)
    for x in data:
        if x["botId"] == myBotId:
            x["timer"] = str(timer)
            x["blueTeam"] = str(blue)
            x["redTeam"] = str(red)
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

while True:
    takescreenshot()
    gay()
    sleep(2)