import pdfplumber
import PyPDF2


# This function extracts text from a PDF file using the pdfplumber library.
def extract_text_with_pdfplumber(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


# This function extracts text from a PDF file using the PyPDF2 library.
def extract_text_with_pypdf2(path):
    text = ""
    reader = PyPDF2.PdfReader(path)
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text