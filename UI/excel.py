import openpyxl

def extract_text_from_excel(xlsx_path):
    wb = openpyxl.load_workbook(xlsx_path)
    sheet = wb.active
    text = "\n".join([" ".join(map(str, row)) for row in sheet.iter_rows(values_only=True)])
    return text
