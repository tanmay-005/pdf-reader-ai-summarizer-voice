import pdf_utils
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.title("My Tkinter Window")
root.geometry("800x600")

label = tk.Label(root, text="PDF Reader + AI Summarizer + Voice", font=("Arial", 18)) # Creates a label widget with specified text and font
label.pack()


def upload_pdf():
    file_path = filedialog.askopenfilename(
    title = "Select a PDF file",
    filetypes = [("PDF Files", "*.pdf"), ("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    print("Selected file:", file_path)
    # extracted_text = pdf_utils.extract_text_with_pdfplumber(file_path) # Calls the extract_text_with_pypdf2 function from pdf_utils.py to extract text from the selected PDF file
    extracted_text = pdf_utils.extract_text_with_pypdf2(file_path)
    text_box.delete("1.0", tk.END) # Clears the text box before inserting new text
    text_box.insert("1.0", extracted_text) # Inserts the extracted text into the text box

upload_btn = tk.Button(root, text="Upload PDF", command=upload_pdf, font=("Arial", 14)) # Creates a button widget with specified text and font, and assigns the upload_pdf function to be called when the button is clicked
upload_btn.pack(padx=100, pady=100) # Makes the button visible in the window with specified padding


text_box = tk.Text(root, height=20, width=90)
text_box.pack()

root.mainloop()