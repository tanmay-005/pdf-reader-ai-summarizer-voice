import pdfplumber
import PyPDF2

def extract_text_with_pdfplumber(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text



def extract_text_with_pypdf2(path):
    text = ""
    reader = PyPDF2.PdfReader(path)
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text