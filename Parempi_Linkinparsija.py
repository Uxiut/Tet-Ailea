'''
reitti = "\\A\\"
valmis_reitti = reitti.replace('\\', '\\\\')
print(valmis_reitti)'''
from PIL import Image
from easygui import *
import pytesseract
import argparse
import cv2
import os
import subprocess
import sys
import numpy 

def user_dialog(): #user_diealog sisältää koodin allaan

    reitti = enterbox(msg='Reitti kuvaan, josta haluat linkit ulos:', title='Linkinparsija', default='')
    print(reitti)
    valmis_reitti = reitti.replace('\\', '\\\\')
    print("Reitti oikeassa muodossa:", valmis_reitti) 
    if '"' in valmis_reitti:
        valmis_reitti = valmis_reitti.replace('"', '') #Poistaa hipsukat kokonaan
    return valmis_reitti #palauttaa käyttäjän antamat tiedot muuttujassa
    
def use_value(valmis_reitti):

    pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\tr0640\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", '--image', 
        help="path to input image to be OCR'd", default = valmis_reitti)
    image = cv2.imread(valmis_reitti)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filename = (valmis_reitti)
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

    import sys

    original_stdout = sys.stdout 

    with open('Linkit.txt', 'w') as f:
        sys.stdout = f 
        print(final)
        sys.stdout = original_stdout 

a = user_dialog()
# a = käyttäjän tieto palautettuna ja paketoitu a:han
use_value(a)
#use_value käyttää käyttäjän antamaa arvoa