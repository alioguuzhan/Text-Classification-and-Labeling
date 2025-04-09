# 🔍 FORENTRACK - Akıllı Metin Sınıflandırma ve Kritik Veri Tespiti

FORENTRACK, PDF, Word, Excel ve görsel (OCR) dosyaları üzerinde metin taraması yapan, kritik veri içeren metinleri tespit edip etiketleyen, kullanıcı dostu bir masaüstü uygulamasıdır. Yapay zeka destekli algoritmalar ve regex desenleriyle güçlü bir tespit sağlar.


- 📄 **PDF**, 📝 **Word**, 📊 **Excel**, 🖼️ **Görsel (OCR)** dosyalarını analiz edebilir
- 🧠 **LSTM + FastText** destekli yapay zeka tabanlı sınıflandırma
- 🧾 Regex kurallarıyla ön tespit, ardından model doğrulaması
- ⚠️ Kritik veri tespitinde kullanıcıya uyarı verir
- 💾 Her analiz sonucunu otomatik olarak `.txt` dosyasına kaydeder

## 🖥️ Uygulama Arayüzü

| Ana Ekran | Sonuç Kaydedildi | Kritik Veri Uyarısı |
|----------|------------------|----------------------|
| ![UI](docs/ui_main.jpeg) | ![Saved](docs/ui_saved.jpeg) | ![Warning](docs/ui_warning.jpeg) |


## 🧪 Kullanılan Teknolojiler

- Python 3.9
- TensorFlow / Keras (LSTM Modeli)
- FastText (Türkçe önceden eğitilmiş word embeddings)
- scikit-learn (Label Encoding, Model değerlendirme)
- Pillow, Tkinter (Arayüz)
- PyMuPDF, docx2txt, pandas, pytesseract (Dosya okuma ve OCR)


## requirements

tensorflow==2.14.0
keras==2.14.0
scikit-learn==1.3.0
pandas==2.0.3
numpy==1.23.5
nltk==3.8.1
opencv-python==4.9.0.80
pytesseract==0.3.10
python-docx==1.1.0
openpyxl==3.1.2
PyMuPDF==1.23.21
Pillow==10.2.0
joblib==1.3.2

