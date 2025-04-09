from Detector import hybrid_detection
from pdf import extract_text_from_pdf
from word import extract_text_from_word
from excel import extract_text_from_excel
from ocr import extract_text_from_image
from labeling import check_critical_data


def process_text(text):
    detections = hybrid_detection(text)
    categorized_data, has_critical = check_critical_data(detections)

    if has_critical:
        print("⚠️ Çok Kritik Veri Tespit Edildi!")

    print(categorized_data)


if __name__ == "__main__":
    #test_text = "Ahmet Yılmaz, TC Kimlik No: 12345678902, IBAN: TR320010009999999999999001, e-posta: ahmet@example.com."
    #process_text(test_text)

    # Test dosyaları için
    print("📄 PDF Dosya Taraması:")
    pdf_text = extract_text_from_pdf('/Users/alioguzhan/Desktop/Python/Metin Sınıflandırma/Test/test-.pdf')
    process_text(pdf_text)

    #print("📝 Word Dosya Taraması:")
    #word_text = extract_text_from_word('/Users/alioguzhan/Desktop/Python/Metin Sınıflandırma/Test/Metin Veri Seti.docx')
    #process_text(word_text)

    #print("📊 Excel Dosya Taraması:")
    #excel_text = extract_text_from_excel('/Users/alioguzhan/Desktop/Python/Metin Sınıflandırma/Test/Ayse_Kaya_Bilgiler.xlsx')
    #process_text(excel_text)

    #print("🖼 OCR ile Resim Taraması:")
    #image_text = extract_text_from_image('/Users/alioguzhan/Desktop/Python/Metin Sınıflandırma/Test/Ekran Resmi 2025-02-21 13.48.14.png')
    #process_text(image_text)
