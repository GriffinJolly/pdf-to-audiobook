# PDF to Audiobook Converter

A simple and user-friendly desktop application that converts PDF documents into spoken audio. Built with Python and Tkinter, this tool allows you to either listen to your PDFs directly or save them as MP3 files for offline listening.

## Features

- Convert PDFs to spoken audio
- Listen to PDFs directly through your computer's speakers
- Save PDF content as MP3 files
- Select specific page ranges for conversion
- Choose from different voice options
- Simple and intuitive graphical user interface
- Cross-platform compatibility (Windows, macOS, Linux)

## Requirements

- Python 3.6 or higher
- Tkinter (usually comes with Python)
- pyttsx3
- PyPDF2

## Installation

1. Clone this repository or download the source code
   ```
   git clone https://github.com/GriffinJolly/pdf-to-audiobook.git
   cd pdf-to-audiobook
   ```

2. Install the required Python packages:
   ```
   pip install pyttsx3 PyPDF2
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Click "Choose PDF File" to select a PDF document
3. (Optional) Specify the page range you want to convert
4. Choose a voice from the dropdown menu
5. Click "Read PDF" to listen immediately or "Save as Audio" to save as an MP3 file

## Supported Platforms

- Windows
- macOS
- Linux

## Dependencies

- [pyttsx3](https://pypi.org/project/pyttsx3/) - Text-to-speech conversion
- [PyPDF2](https://pypi.org/project/PyPDF2/) - PDF text extraction
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - GUI framework

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.
