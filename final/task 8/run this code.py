

    
import pytesseract

from PIL import Image

from read_image import read_image
    
    
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

res = 0
foo = input(" enter name of image file 1  ")

op = input("enter operator,  +  -  /   *  ")

woop = input(" enter name of image file 2  ")

f1 = int(read_image(foo))

f2 = int(read_image(woop))

if op == "+":
    res = f1 + f2

elif op == "-":
    res = f1 - f2

elif op == "/":
    res = f1 / f2

elif op == "*":
    res = f1 * f2

print ("the result is  ", res)






