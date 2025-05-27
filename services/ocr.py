# services/ocr.py
from PIL import Image
img = Image.open("images/image for begining.jpg")
img.show()

import pytesseract

#  Tesseract का path सही से set करो — अपने system के हिसाब से
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'

def image_to_text(image_path):
    return pytesseract.image_to_string(Image.open(image_path))



