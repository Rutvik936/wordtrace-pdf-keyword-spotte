import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
from textract_utils import process_pdf_with_textract
from viewer_utils import render_pdf_with_highlights
from json_utils import save_layout_json, save_word_json

st.set_page_config(layout="wide")
st.title("📄 Word-Level Coordinate Highlighter")

# ✅ Ask how many pages to process
max_pages = st.number_input("How many PDF pages to process?", min_value=1, max_value=50, value=3)

# ✅ Convert PDF to image pages
def convert_pdf_to_images(file, max_pages):
    pdf_doc = fitz.open(stream=file.read(), filetype="pdf")
    pages = []
    for i, page in enumerate(pdf_doc):
        if i >= max_pages:
            break
        pix = page.get_pixmap(dpi=100)  # 🔽 Low DPI for speed
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        pages.append(img)
    return pages

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    pages = convert_pdf_to_images(uploaded_file, max_pages)

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
