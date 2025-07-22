# 📄 Word-Level Coordinate Highlighter (OCR + Streamlit)

This project allows users to upload multi-page financial documents (PDFs), detects layout sections like Titles and Tables, and performs OCR **only within selected sections**. Users can search up to 5 words, and the app highlights their **exact word-level bounding boxes** on the document.

---

## 🚀 Features

- ✅ Upload multi-page PDFs
- ✅ Auto-detect layout sections (Title, Table, etc.)
- ✅ Perform **region-specific OCR** (not entire page)
- ✅ Save bounding box and text in structured JSON
- ✅ Search for up to 5 keywords
- ✅ See **live highlighted** coordinates on PDF images
- ✅ Built using Python, Streamlit, and Tesseract OCR

---

## 🧠 Tech Stack

| Area          | Tool/Library           |
|---------------|------------------------|
| Frontend UI   | Streamlit              |
| OCR Engine    | Tesseract + pytesseract|
| PDF Handling  | pdf2image + Pillow     |
| Layout Logic  | Custom Rule-based Logic|
| Deployment    | Streamlit Cloud        |

---

## 🗂️ Project Structure
word-coordinate-app/
│
├── app.py # Streamlit App
├── textract_utils.py # OCR Processing
├── viewer_utils.py # Image Highlights
├── json_utils.py # Save/Load JSONs
├── requirements.txt # Python dependencies
└── output/ # JSON output folder (created at runtime)


---

## 📦 How to Run Locally

```bash
git clone https://github.com/Anuragpandey2005/word-coordinate-app.git
cd word-coordinate-app
pip install -r requirements.txt
streamlit run app.py
