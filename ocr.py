import pytesseract
from PIL import Image
import os

# Windows Users: Uncomment & set Tesseract path if needed
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    """Extract text from an image using Tesseract OCR."""
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        return f"Error processing image: {e}"

def batch_extract_text(image_folder):
    """Extract text from all images in a folder."""
    extracted_texts = {}
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            full_path = os.path.join(image_folder, filename)
            extracted_texts[filename] = extract_text(full_path)
    return extracted_texts
