# 🕵️‍♀️ Tamper Detection in Academic Documents

## 📌 Introduction

In an increasingly digital academic ecosystem, verifying the authenticity of official documents is crucial to combat fraudulent degrees and certifications. This project presents a prototype system for **detecting tampering in academic documents** (degrees, transcripts, certificates) using:

- PDF metadata inspection  
- Layout similarity comparison using SSIM  
- OCR-based text extraction

The system supports detection of unauthorized modifications and flags discrepancies between original and tampered versions.

---

## 🛠️ Methodology

### 📄 1. Document Preparation

Mock datasets were created with both original and tampered versions of:

- Degree Certificate  
- Academic Transcript  
- Course Completion Certificate  

**Tampering operations included:**

- Modifying names, GPA, course titles, and dates  
- Changing layout (e.g., fake seals, institution names)  
- Altering metadata (e.g., software used, timestamps)

---

### 📑 2. Metadata Analysis

**Tool Used:** `PyPDF2`

Metadata fields extracted and compared:
- `/CreationDate`  
- `/ModDate`  
- `/Producer`  

**Heuristic Rule:**  
If `/ModDate` > `/CreationDate`, document is flagged as potentially modified. Suspicious producers (e.g., “Fake PDF Editor”) are also treated as red flags.

#### 🖼️ Result Image – Metadata Analysis

![Metadata Result](results/metadata_result.png)

---

### 🖼️ 3. Layout Comparison via SSIM

**Tools:** `pdf2image`, `OpenCV`, `skimage.metrics`

**Process:**
1. Convert original and tampered PDFs to images (first page only)  
2. Convert to grayscale  
3. Compare using Structural Similarity Index (SSIM)

**Threshold:**  
SSIM score < `0.95` implies layout inconsistency (e.g., fake seals, logo changes).

#### 🖼️ Result Image – Layout Comparison

![Layout SSIM Result](results/layout_ssim_result.png)

---

### 🔍 4. OCR-Based Text Extraction

**Tools:** `pytesseract`, `pdf2image`

**Steps:**
1. Convert PDF pages to high-resolution images  
2. Extract text using Tesseract OCR  
3. Compare original vs tampered text using `difflib` or fuzzy matching  

**Tamper Detection Focus:**
- Names (e.g., "Alex Carter" → "Alex Smith")  
- Altered grades, course titles, or GPA  
- Changed issue dates  

#### 🖼️ Result Image – OCR Comparison

![OCR Result](results/ocr_result.png)

---

## ✅ Conclusion

This system effectively detects tampering in academic PDFs through a multi-pronged approach—analyzing metadata, layout similarity, and extracted text. While the prototype performs well in a controlled setting, real-world deployment may require:

- Handling noisy scans  
- Scaling to diverse document types  
- Enhancing UI and automation  

With further improvements, this tool can serve academic institutions, HR teams, and legal departments in verifying the authenticity of documents.

---

