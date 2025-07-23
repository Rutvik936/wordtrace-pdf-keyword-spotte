import streamlit as st
<<<<<<< HEAD
=======
import pytesseract
import fitz  # PyMuPDF
>>>>>>> 4ed58c0c644588fbc119144a75b322f8951810a1
from PIL import Image, ImageDraw
from textract_utils import process_pdf_with_textract
from viewer_utils import render_pdf_with_highlights
from json_utils import save_layout_json, save_word_json
<<<<<<< HEAD
import fitz  # PyMuPDF
=======
>>>>>>> 4ed58c0c644588fbc119144a75b322f8951810a1

# Set Streamlit page config
st.set_page_config(layout="wide")
st.title("📄 Word-Level Coordinate Highlighter")

<<<<<<< HEAD
# PDF to images using PyMuPDF (no poppler needed)
=======
# Function to convert PDF to images using PyMuPDF (NO POPPLER REQUIRED)
>>>>>>> 4ed58c0c644588fbc119144a75b322f8951810a1
def convert_pdf_to_images(file):
    pdf_doc = fitz.open(stream=file.read(), filetype="pdf")
    pages = []
    for page in pdf_doc:
        pix = page.get_pixmap(dpi=150)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        pages.append(img)
    return pages

<<<<<<< HEAD
=======
# File uploader
>>>>>>> 4ed58c0c644588fbc119144a75b322f8951810a1
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

# Processing logic
if uploaded_file:
    pages = convert_pdf_to_images(uploaded_file)

    with st.spinner("⚙️ Processing... please wait..."):
        layout_json, word_json = process_pdf_with_textract(pages)
        save_layout_json(layout_json)
        save_word_json(word_json)
    st.success("✅ Processing complete! JSON files saved.")

    queries = []
    st.markdown("### 🔍 Search up to 5 Keywords")
    for i in range(5):
        word = st.text_input(f"Keyword {i+1}", key=f"query_{i}")
        if word:
            queries.append(word)

    st.markdown("---")
    if queries:
        st.markdown("### 🔦 Highlighted Results")
        render_pdf_with_highlights(pages, word_json, queries)
    else:
        st.image(pages[0], caption="Page 1", use_container_width=True)
