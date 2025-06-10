import pyttsx3
from PyPDF2 import PdfReader
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Initialize Tkinter root (to avoid empty GUI window)
root = Tk()
root.withdraw()  # Hide the root window

# Ask user to select a PDF file
book = askopenfilename(filetypes=[("PDF files", "*.pdf")])
if not book:
    print("No file selected.")
    exit()

# Load the PDF
try:
    pdfreader = PdfReader(book)
    speaker = pyttsx3.init()
    
    for page in pdfreader.pages:
        text = page.extract_text()
        if text:  # Only speak if text is present
            speaker.say(text)
            speaker.runAndWait()
except Exception as e:
    print("An error occurred:", e)
