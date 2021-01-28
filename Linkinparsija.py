from PIL import Image
import pytesseract
import argparse
import cv2
import os
import subprocess
import sys
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\uxiut\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
ap = argparse.ArgumentParser()
ap.add_argument("-i", '--image', 
    help="path to input image to be OCR'd", default = "C:\\Users\\uxiut\\Downloads\\MicrosoftTeams-image.png")
image = cv2.imread("C:\\Users\\uxiut\\Downloads\\MicrosoftTeams-image.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
filename = "C:\\Users\\uxiut\\Downloads\\MicrosoftTeams-image.png"
text = pytesseract.image_to_string(Image.open(filename))
print(text)
cv2.imshow("image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)

import re

pattern = '(https.*)'
result = re.findall(pattern, text) 
print(result)
strresult = '''
'''.join(map(str, result))

semifinal = strresult.replace(" ",".")
final = semifinal.replace(",", " ")
print(final)
#pywinauto ei täyttänyt toiveita, muutin menetelmää.

import sys

print('This message will be displayed on the screen.')

original_stdout = sys.stdout 

with open('Linkit.txt', 'w') as f:
    sys.stdout = f 
    print(final)
    sys.stdout = original_stdout 