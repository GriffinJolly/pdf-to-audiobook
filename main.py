import pyttsx3
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog, ttk, messagebox

# Initialize TTS engine globally
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# GUI Functions
def choose_file():
    global pdfreader, book_path
    book_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if book_path:
        try:
            pdfreader = PdfReader(book_path)
            filename = book_path.split("/")[-1]
            file_label.config(text=f"Loaded: {filename}")
            page_count_label.config(text=f"Total Pages: {len(pdfreader.pages)}")
            status_label.config(text="PDF loaded successfully.", fg="green")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load PDF: {e}")

def read_pdf():
    try:
        start = int(start_page.get()) - 1
        end = int(end_page.get())
        if start < 0 or end > len(pdfreader.pages):
            raise ValueError("Page range out of bounds")
        engine.setProperty('voice', voices[voice_dropdown.current()].id)

        for num in range(start, end):
            text = pdfreader.pages[num].extract_text()
            if text:
                engine.say(text)
        engine.runAndWait()
        status_label.config(text="Reading complete.", fg="blue")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def save_audio():
    try:
        start = int(start_page.get()) - 1
        end = int(end_page.get())
        if start < 0 or end > len(pdfreader.pages):
            raise ValueError("Page range out of bounds")
        text_content = ""
        for num in range(start, end):
            text = pdfreader.pages[num].extract_text()
            if text:
                text_content += text + "\n"

        save_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                 filetypes=[("Audio Files", "*.mp3")])
        if save_path:
            engine.setProperty('voice', voices[voice_dropdown.current()].id)
            engine.save_to_file(text_content, save_path)
            engine.runAndWait()
            messagebox.showinfo("Success", "Audio file saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = Tk()
root.title("PDF to Speech Reader")
root.geometry("500x400")
root.resizable(False, False)

Label(root, text="PDF to Speech Converter", font=("Arial", 18)).pack(pady=10)

Button(root, text="Choose PDF File", command=choose_file, width=30).pack(pady=5)

file_label = Label(root, text="No file selected", fg="grey")
file_label.pack()

page_count_label = Label(root, text="")
page_count_label.pack()

# Page Range Frame
range_frame = Frame(root)
range_frame.pack(pady=10)

Label(range_frame, text="Start Page:").grid(row=0, column=0, padx=5)
start_page = Entry(range_frame, width=5)
start_page.grid(row=0, column=1, padx=5)

Label(range_frame, text="End Page:").grid(row=0, column=2, padx=5)
end_page = Entry(range_frame, width=5)
end_page.grid(row=0, column=3, padx=5)

# Voice Selection
voice_frame = Frame(root)
voice_frame.pack(pady=10)

Label(voice_frame, text="Select Voice:").pack(side=LEFT)
voice_dropdown = ttk.Combobox(voice_frame, width=30, state="readonly")
voice_dropdown['values'] = [voice.name for voice in voices]
voice_dropdown.current(0)
voice_dropdown.pack(side=LEFT, padx=10)

# Buttons for Actions
action_frame = Frame(root)
action_frame.pack(pady=20)

Button(action_frame, text="Read PDF", command=read_pdf, width=15).grid(row=0, column=0, padx=10)
Button(action_frame, text="Save as Audio", command=save_audio, width=15).grid(row=0, column=1, padx=10)

status_label = Label(root, text="", fg="green")
status_label.pack(pady=10)

root.mainloop()
