# Handwritten to Text Converter

A Python-based tool to convert handwritten text from images into digital text using Tesseract OCR.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install Tesseract OCR:
   - **Windows**: [Download and install](https://github.com/UB-Mannheim/tesseract/wiki)
   - **Linux**:
     ```bash
     sudo apt install tesseract-ocr
     ```
   - **Mac**:
     ```bash
     brew install tesseract
     ```
3. Run the application:
   ```bash
   python main.py
   ```
4. Use the GUI to select an image or folder for text extraction.

## Features
- ✅ Supports PNG, JPG, JPEG images
- ✅ Image preprocessing for better OCR results
- ✅ Batch processing for multiple images
- ✅ Export extracted text to a file

## Test the Application
Use the GUI interface or manually test with:
```bash
python ocr.py path/to/image.png
```

