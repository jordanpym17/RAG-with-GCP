import os
import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Set the path to Tesseract executable if needed
# pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'

def ocr_pdf(input_pdf_path, output_pdf_path):
    # Convert PDF to images
    images = convert_from_path(input_pdf_path)

    # Create a new PDF with OCR text
    doc = fitz.open()  # New empty PDF

    for image in images:
        # Perform OCR on the image
        ocr_text = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')

        # Append OCR text to the new PDF
        img_doc = fitz.open("pdf", ocr_text)
        doc.insert_pdf(img_doc)

    # Save the OCR'd PDF
    doc.save(output_pdf_path)

def process_pdfs_in_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.pdf'):
            input_pdf_path = os.path.join(input_dir, filename)
            output_pdf_path = os.path.join(output_dir, filename)

            print(f"Processing {filename}...")
            ocr_pdf(input_pdf_path, output_pdf_path)

    print("Processing complete.")



