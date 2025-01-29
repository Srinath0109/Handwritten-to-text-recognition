import tkinter as tk
from tkinter import filedialog, messagebox
from ocr import extract_text, batch_extract_text
from image_processing import preprocess_image

def select_image():
    """Open file dialog to select a single image and extract text."""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    
    if file_path:
        processed_path = preprocess_image(file_path)
        text = extract_text(processed_path)
        
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, text)

def select_folder():
    """Open folder dialog for batch OCR processing."""
    folder_path = filedialog.askdirectory()
    
    if folder_path:
        extracted_data = batch_extract_text(folder_path)
        
        output_text = "\n\n".join([f"{file}:\n{text}" for file, text in extracted_data.items()])
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, output_text)

def save_text():
    """Save extracted text to a file."""
    text = result_text.get("1.0", tk.END).strip()
    if text:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text)
            messagebox.showinfo("Success", "Text saved successfully!")

# GUI Setup
root = tk.Tk()
root.title("Handwritten to Text Converter")
root.geometry("600x500")

# Buttons
btn_select_image = tk.Button(root, text="Select Image", command=select_image)
btn_select_folder = tk.Button(root, text="Batch Process Folder", command=select_folder)
btn_save_text = tk.Button(root, text="Save Extracted Text", command=save_text)

btn_select_image.pack(pady=5)
btn_select_folder.pack(pady=5)
btn_save_text.pack(pady=5)

# Text Area
result_text = tk.Text(root, wrap=tk.WORD, height=15, width=60)
result_text.pack(pady=10)

# Run GUI
root.mainloop()
