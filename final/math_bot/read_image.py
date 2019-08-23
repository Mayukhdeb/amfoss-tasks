
## god bless pytesseract

    
import pytesseract

from PIL import Image
    

def read_image(image_name):
    
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  


    text = pytesseract.image_to_string(Image.open(image_name))    
    
    

    return text






