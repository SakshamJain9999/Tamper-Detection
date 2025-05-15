# Tamper Detection in Academic Documents

## Introduction

In an increasingly digital academic ecosystem, verifying the authenticity of official documents is crucial to combat fraudulent degrees and certifications. This project presents a prototype system for detecting tampering in academic documents (degrees, transcripts, certificates) using a combination of PDF metadata inspection, layout similarity comparison, and OCR-based text extraction.

The system supports the detection of unauthorized modifications and provides alerts when discrepancies are found between original and tampered versions.

---

## Methodology

### A) Document Preparation

We manually created mock datasets with both original and tampered PDF versions of:

- Degree Certificate  
- Academic Transcript  
- Course Completion Certificate  

Tampering operations included:

- Modifying names, GPA, course titles, and dates  
- Changing layout (e.g., fake seals, institution names)  
- Altering metadata (modification dates or software used)  

---

### B) Metadata Analysis

**Tool Used:** `PyPDF2`  
We extracted and analyzed key PDF metadata fields such as:

- `/CreationDate`
- `/ModDate`
- `/Producer`

**Heuristic Used:**  
If `/ModDate` > `/CreationDate`, the document is flagged as potentially modified. Suspicious `/Producer` values like “Fake PDF Editor” are also flagged.

#### 🖼️ Result Image – Metadata Analysis

![Metadata Analysis](https://github.com/SakshamJain9999/Tamper-Detection/blob/main/Results/MetaData%20Analysis.png)

---

### C) Layout Comparison via SSIM

**Tools Used:** `pdf2image`, `OpenCV`, `skimage.metrics`  

**Steps:**
- Convert the first page of both PDFs into images  
- Convert the images to grayscale  
- Use Structural Similarity Index (SSIM) to compare the layout  
- A threshold of SSIM score < 0.95 indicates layout inconsistencies  

#### 🖼️ Converted Images – Before Layout Comparison

**Original Document (Image):**  
![Original PDF Image](https://github.com/SakshamJain9999/Tamper-Detection/blob/main/Results/Pdf%20to%20Img/degree_original.png)

**Tampered Document (Image):**  
![Tampered PDF Image](https://github.com/SakshamJain9999/Tamper-Detection/blob/main/Results/Pdf%20to%20Img/degree_tampered.png)

#### 🖼️ Layout SSIM Comparison Result

![Layout SSIM Result](https://github.com/SakshamJain9999/Tamper-Detection/blob/main/Results/Layout%20Compare.png)

---

### 2.4 OCR-Based Text Extraction

**Tools Used:** `pytesseract`, `pdf2image`  

**Steps:**
- Convert each PDF page into an image  
- Use OCR (Tesseract) to extract the text  
- Compare the extracted text using Python’s `difflib` or manual inspection

Focus Points for Tampering Detection:
- Changed names (e.g., “Alex Carter” → “Alex Smith”)  
- Added or removed courses  
- Altered GPA or grades  
- Modified dates or institutions  

#### 🖼️ OCR Extracted Text Images

**Original Document OCR Output:** 
- [Original OCR Text](https://github.com/SakshamJain9999/Tamper-Detection/blob/main/Results/Extract%20Text/original_text.txt)

**Tampered Document OCR Output:**  
- [Tampered OCR Text](https://github.com/SakshamJain9999/Tamper-Detection/blob/main/Results/Extract%20Text/tampered_text.txt)

#### 🖼️ Text Difference Visualization

![Text Diff Result](https://github.com/SakshamJain9999/Tamper-Detection/blob/main/Results/Text%20Diff.png)

---

## Conclusion

The developed system demonstrates an effective approach for detecting tampering in academic documents using open-source tools. It covers multiple layers of inspection—metadata, layout, and content—which complement each other.

While the prototype works well in a controlled environment, real-world deployment will require handling diverse file types, noisy scans, and adversarial tampering techniques.

With improvements in automation, UI, and tamper classification, this solution can serve as a valuable tool for academic verification offices and recruitment agencies.

---

