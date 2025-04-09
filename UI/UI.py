import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
from Detector import hybrid_detection
from labeling import check_critical_data
from pdf import extract_text_from_pdf
from word import extract_text_from_word
from excel import extract_text_from_excel
from ocr import extract_text_from_image

# 🖥️ Ana pencere oluşturma
root = tk.Tk()
root.title("FORENTRACK")
root.geometry("650x550")
#root.configure(bg="#e0e0e0")

# 📌 **Arka plan resmi ekleme**
try:
    bg_image_path = "/Users/alioguzhan/Desktop/Python/Metin Sınıflandırma/Ekran Resmi 2025-03-18 01.41.04.png"
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((650, 550))
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(root, width=650, height=550)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

except Exception as e:
    print(f"⚠️ Arka plan yüklenemedi: {e}")

# 📂 **Seçilen dosyanın yolu ve türü**
selected_file = None
file_type = None

def select_file(file_ext):
    global selected_file, file_type

    file_types = {
        'pdf': [('PDF Files', '*.pdf')],
        'word': [('Word Files', '*.docx')],
        'excel': [('Excel Files', '*.xlsx')],
        'image': [("PNG", "*.png"), ("JPEG", "*.jpg"), ("JPEG", "*.jpeg"), ("BMP", "*.bmp"), ("GIF", "*.gif")]
    }

    file_path = filedialog.askopenfilename(title="Dosya Seçin", filetypes=file_types.get(file_ext, []))

    if not file_path:
        messagebox.showerror("Hata", "Geçerli bir dosya seçilmedi!")
        return

    selected_file = file_path
    file_type = file_ext
    lbl_selected_file.config(text=f"📂 Seçilen Dosya: {os.path.basename(file_path)}")

def process_file():
    global selected_file, file_type

    if not selected_file:
        messagebox.showerror("Hata", "Lütfen bir dosya seçin!")
        return

    try:
        if file_type == 'pdf':
            text = extract_text_from_pdf(selected_file)
        elif file_type == 'word':
            text = extract_text_from_word(selected_file)
        elif file_type == 'excel':
            text = extract_text_from_excel(selected_file)
        elif file_type == 'image':
            text = extract_text_from_image(selected_file)
        else:
            messagebox.showerror("Hata", "Bilinmeyen dosya türü!")
            return
    except Exception as e:
        messagebox.showerror("Hata", f"Dosya işlenirken bir hata oluştu:\n{e}")
        return

    detections = hybrid_detection(text)
    categorized_data, has_critical = check_critical_data(detections)
    save_results(categorized_data, selected_file)

    if has_critical:
        messagebox.showwarning("Kritik Veri Tespit Edildi", "⚠️ Dosyada kritik veri tespit edildi!")
    else:
        messagebox.showinfo("Tamamlandı", "Tespit işlemi tamamlandı.")

def save_results(data, file_path):
    save_path = f"{os.path.splitext(file_path)[0]}_tespit.txt"

    with open(save_path, "w", encoding="utf-8") as f:
        for item in data:
            if len(item) == 2:
                category, detected_text = item
                f.write(f"{category}: {detected_text}\n")
            elif len(item) >= 3:
                category, detected_text, *_ = item
                f.write(f"{category}: {detected_text}\n")

    messagebox.showinfo("Sonuç Kaydedildi", f"Sonuçlar kaydedildi:\n{save_path}")


# 📌 Kırmızı Buton Oluşturma
btn_pdf = tk.Button(root, text="📄 PDF", command=lambda: select_file('pdf'),
                    bg="red", fg="black", font=("Arial", 10, "bold"), padx=10, pady=5)
canvas.create_window(80, 250, window=btn_pdf)

btn_word = tk.Button(root, text="📝 Word", command=lambda: select_file('word'),
                     bg="red", fg="black", font=("Arial", 10, "bold"), padx=10, pady=5)
canvas.create_window(570, 250, window=btn_word)

btn_excel = tk.Button(root, text="📊 Excel", command=lambda: select_file('excel'),
                      bg="red", fg="black", font=("Arial", 10, "bold"), padx=10, pady=5)
canvas.create_window(80, 300, window=btn_excel)

btn_image = tk.Button(root, text="🖼️ Image", command=lambda: select_file('image'),
                      bg="red", fg="black", font=("Arial", 10, "bold"), padx=10, pady=5)
canvas.create_window(570, 300, window=btn_image)

btn_process = tk.Button(root, text="🔍 SEARCH", command=process_file,
                        bg="red", fg="black", font=("Arial", 15, "bold"), padx=10, pady=5)
canvas.create_window(325, 470, window=btn_process)


root.mainloop()
