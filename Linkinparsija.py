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
#ap.add_argument("-p", "--preprocess", type=str, default ="thresh",
#    help="type of preprocessing to be done")
#args = vars(ap.parse_args())
# load the example image and convert it to grayscale
image = cv2.imread("C:\\Users\\uxiut\\Downloads\\MicrosoftTeams-image.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# check to see if we should apply thresholding to preprocess the
# image
#if args["preprocess"] == "thresh":
#    gray = cv2.threshold(gray, 0, 255,
#        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# make a check to see if median blurring should be done to remove
# noise
#elif args["preprocess"] == "blur":
#    gray = cv2.medianBlur(gray, 3)
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "C:\\Users\\uxiut\\Downloads\\MicrosoftTeams-image.png"
#cv2.imwrite(filename, gray)
# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
print(text)
# show the output images
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
#pywinauto ei täyttänyt toiveta, muutin menetelmää.
'''import pywinauto
from pywinauto.application import Application
app = Application().start("notepad.exe")
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)'''


import sys

print('This message will be displayed on the screen.')

original_stdout = sys.stdout # Save a reference to the original standard output

with open('Linkit.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(final)
    sys.stdout = original_stdout # Reset the standard output to its original value