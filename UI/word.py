import docx

def extract_text_from_word(docx_path):
    try:
        doc = docx.Document(docx_path)
        return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
    except Exception as e:
        return f"Hata: Word dosyası okunamadı! ({e})"
