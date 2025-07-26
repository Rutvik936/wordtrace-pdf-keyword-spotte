
# 🧠 WordTrace: PDF Keyword Spotter using Streamlit and OCR (OCR + Streamlit)

This project is a **streamlit-based UI tool** for detecting layout elements in multi-page financial PDFs and highlighting **word-level coordinates** using OCR.

---

## 🚀 Features

- 📄 Upload financial PDF (multi-page)
- 📦 Detect key sections (Title, Table) using layout-based cropping
- 🔍 Apply OCR only on selected layout areas (not whole page)
- 🧠 Extract text and bounding boxes using EasyOCR
- 💡 Store structured data in:
  - `layout.json` (normalized section-level layout)
  - `wordjson.json` (absolute word-level positions)
- 🟥 Real-time keyword search (up to 5 terms)
- 🔦 Highlight matching words with red bounding boxes
- 🖥️ Visual PDF viewer on left + keyword search on right

---

## 🛠️ Tech Stack

| Tool/Library | Purpose |
|--------------|---------|
| `Streamlit` | Interactive web UI |
| `PyMuPDF` (`fitz`) | PDF rendering & image generation |
| `EasyOCR` | Lightweight OCR engine |
| `Pillow` | Drawing highlights |
| `NumPy` | Image processing |
| `JSON` | Data storage for layout + word positions |

---

## 📁 Folder Structure

```
.
├── app.py                # Streamlit app
├── textract_utils.py     # OCR & layout logic
├── json_utils.py         # Load/save JSONs
├── viewer_utils.py       # Render highlights
├── requirements.txt
├── output/               # Contains layout.json & wordjson.json
└── README.md
```

---

## ⚠️ Notes

- ❌ No external dependencies like Tesseract CLI or Poppler — works with just pip packages.
- ✅ Fully portable and works on any OS.

---

## 🧪 How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/your-username/wordtrace-pdf-keyword-spotter.git
cd wordtrace-pdf-keyword-spotter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

---

## 🌐 Optional: Host on Streamlit Cloud

- Push your repo to GitHub ✅
- Go to [streamlit.io/cloud](https://streamlit.io/cloud) and connect your GitHub
- Deploy the app with just one click 🚀

---

## 📸 Sample Screenshot

_Add a screenshot here showing highlighted keywords_

---

## 🤝 Contributions

Pull requests and suggestions are welcome!

---

## 📄 License

This project is for academic/demo purposes only.

---
