import os
import pytesseract
import cv2


import os
os.environ['TESSDATA_PREFIX'] = '/opt/homebrew/share/tessdata/'


def extract_text_from_image(image_path):
    if not os.path.exists(image_path):
        return "Hata: Resim dosyası bulunamadı!"

    img = cv2.imread(image_path)
    if img is None:
        return "Hata: Resim dosyası açılamadı!"

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    extracted_text = pytesseract.image_to_string(img_gray, lang='tur')
    return extracted_text
