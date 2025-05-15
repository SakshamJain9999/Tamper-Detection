from PyPDF2 import PdfReader

def analyze_metadata(path):
    reader = PdfReader(path)
    metadata = reader.metadata
    print(f"Metadata for {path}:")
    for key, value in metadata.items():
        print(f"{key}: {value}")
    if '/ModDate' in metadata and '/CreationDate' in metadata:
        if metadata['/ModDate'] > metadata['/CreationDate']:
            print("⚠️  Modification after creation – Possible tampering!")

if __name__ == "__main__":
    analyze_metadata("degree_tampered.pdf")  # Change file name here if needed
