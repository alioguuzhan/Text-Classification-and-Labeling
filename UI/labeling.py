CRITICAL_CATEGORIES = ["TC_Kimlik_No", "IBAN", "Pasaport"]

def check_critical_data(detections):
    categorized_data = []
    has_critical = False

    with open("tespit_raporu.txt", "w", encoding="utf-8") as report_file:
        report_file.write("Tespit Raporu\n")
        report_file.write("=" * 50 + "\n")

        for detection in detections:
            if len(detection) == 3:
                category, detected_text, _ = detection  # Durumu kullanmayacağız
            elif len(detection) == 2:
                category, detected_text = detection
            else:
                continue  # Beklenmedik yapı varsa geç

            if category in CRITICAL_CATEGORIES:
                label = "Çok Kritik"
                has_critical = True
            else:
                label = "Az Kritik"

            entry = f"Kategori: {category}, Tespit Edilen: {detected_text}, Etiket: {label}\n"
            print(entry.strip())
            report_file.write(entry)

            categorized_data.append((category, detected_text, label))

        report_file.write("=" * 50 + "\n")
        report_file.write("Rapor Sonu\n")

    return categorized_data, has_critical
