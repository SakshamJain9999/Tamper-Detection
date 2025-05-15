from pdf2image import convert_from_path

def convert_pdf_to_image(pdf_path, output_image_path):
    pages = convert_from_path(pdf_path, 300)
    pages[0].save(output_image_path, "PNG")

if __name__ == "__main__":
    convert_pdf_to_image("degree_original.pdf", "degree_original.png")
    convert_pdf_to_image("degree_tampered.pdf", "degree_tampered.png")
