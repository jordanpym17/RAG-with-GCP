import os
from pdfminer.high_level import extract_text

def check_pdf_directory(directory):
    pdfs_without_text = []

    # Walk through all directories in the directory tree
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                # Attempt to extract text from the PDF
                text = extract_text(pdf_path)
                if not text.strip():  # Check if the extracted text is empty or whitespace
                    pdfs_without_text.append(pdf_path)
                    print(f"No readable text found in: {pdf_path}")

    return pdfs_without_text

# Specify your directory path here
directory_path = "inserd directory"
pdfs_without_text = check_pdf_directory(directory_path)

# Print all PDFs that have no readable text
if pdfs_without_text:
    print("\nList of PDFs with no readable text:")
    for pdf in pdfs_without_text:
        print(pdf)   
else:
    print("All PDFs have readable text.")
