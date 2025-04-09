import re
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# 📌 LSTM modeli ve yardımcı dosyaları yükle
lstm_model = load_model('/Users/alioguzhan/Desktop/Python/Metin Sınıflandırma/ALL Models/final_lstm_model.h5')
tokenizer = joblib.load('/Users/alioguzhan/Desktop/Python/Metin Sınıflandırma/ALL Models/tokenizer.pkl')
label_encoder = joblib.load('/Users/alioguzhan/Desktop/Python/Metin Sınıflandırma/ALL Models/label_encoder.pkl')

# 📌 Regex Kuralları
patterns = {
    "TC_Kimlik_No": r'\b[1-9][0-9]{9}[02468]\b',
    "E_posta": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    "IBAN": r'\bTR[0-9]{2}[0-9A-Z]{22}\b',
    "Telefon": r'\b(\+90\s5\d{2}\s\d{3}\s\d{2}\s\d{2})|\b(0\d{10})|\b(0\d{3}\s\d{3}\s\d{2}\s\d{2})\b',
    "Doğum_Tarihi": r'\b(0[1-9]|[12][0-9]|3[01])[\./-](0[1-9]|1[0-2])[\./-](19[0-9]{2}|20[0-2][0-9])\b',
    "Pasaport": r'\b[A-Z]{1,2}[0-9]{6,9}\b',
    "Adres": r'\b(?:[A-ZÇĞİÖŞÜa-zçğıöşü]+\s)+(?:Mahallesi|Caddesi|Sokağı|Bulvarı|Blok|Apartmanı|Bina|Daire|İl|İlçe|Şehir|Belediyesi|\w+/\w+)\b',
    "Ad_Soyad": r'\b[A-ZÇĞİÖŞÜ][a-zçğıöşü]{2,}\s(?:[A-ZÇĞİÖŞÜ][a-zçğıöşü]{2,}\s)?[A-ZÇĞİÖŞÜ][a-zçğıöşü]{2,}\b'
}


# 📌 Regex tabanlı tespit
def regex_based_detection(text):
    detections = []
    for category, pattern in patterns.items():
        matches = re.findall(pattern, text)
        for match in matches:
            # Eğer eşleşme bir tuple ise string'e çevir
            if isinstance(match, tuple):
                match = " ".join([m for m in match if m]).strip()
            else:
                match = match.strip()

            detections.append((category, match))
    return detections


# 📌 LSTM ile sınıflandırma
def classify_with_lstm(text):
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=300, padding='post')
    prediction = lstm_model.predict(padded_sequence)
    predicted_class = np.argmax(prediction, axis=1)[0]
    predicted_label = label_encoder.inverse_transform([predicted_class])[0]
    return predicted_label


# 📌 Hibrit Tespit (Regex + LSTM)
def hybrid_detection(text):
    regex_detections = regex_based_detection(text)
    results = []

    # Regex bulduklarını LSTM ile doğrula
    for category, detected_text in regex_detections:
        lstm_predicted_class = classify_with_lstm(detected_text)

        if category == lstm_predicted_class:
            results.append((category, detected_text, f"Onaylandı (Regex: {category}, LSTM: {lstm_predicted_class})"))
        else:
            results.append(
                (category, detected_text, f"Algoritma Kabul Edildi (Regex: {category}, LSTM: {lstm_predicted_class})"))

    return results


