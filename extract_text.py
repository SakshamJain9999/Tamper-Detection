import pytesseract
from pdf2image import convert_from_path

def extract_text_to_file(path, output_file):
    images = convert_from_path(path, 300)
    full_text = ""
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        full_text += f"\n--- Page {i+1} ---\n{text}"

    with open(output_file, "w") as f:
        f.write(full_text)

if __name__ == "__main__":
    extract_text_to_file("transcript_original.pdf", "original_text.txt")
    extract_text_to_file("transcript_tampered.pdf", "tampered_text.txt")
