import cv2
import numpy as np
from PIL import Image

def preprocess_image(image_path):
    """Preprocess image to improve OCR accuracy."""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
    img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]  # Binarization
    img = cv2.medianBlur(img, 3)  # Noise removal
    
    processed_path = "processed_image.png"
    cv2.imwrite(processed_path, img)
    return processed_path
