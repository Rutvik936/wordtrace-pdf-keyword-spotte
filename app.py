# ✅ 1. app.py
import streamlit as st
from pdf2image import convert_from_bytes
from textract_utils import process_pdf_with_textract
from viewer_utils import render_pdf_with_highlights
from json_utils import save_layout_json, save_word_json
import os

# ✅ Update with your actual Poppler path
POPPLER_PATH = r"C:\\Users\\rutvi\\Downloads\\Release-24.08.0-0\\poppler-24.08.0\\Library\\bin"

st.set_page_config(layout="wide")
st.title("📄 Word-Level Coordinate Highlighter")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    pages = convert_from_bytes(uploaded_file.read(), poppler_path=POPPLER_PATH)

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
        st.image(pages[0], caption="Page 1", use_column_width=True)