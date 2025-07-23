import streamlit as st
from pdf2image import convert_from_bytes
from PIL import ImageDraw, Image
import pytesseract
import json
import os

# Save layout and word json
def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# Process PDF pages and extract word-level bounding boxes
def process_pdf_with_tesseract(pages, max_pages):
    layout_json = {}
    word_json = {}

    for i, page in enumerate(pages):
        if i >= max_pages:
            break

        width, height = page.size
        layout_json[str(i)] = {
            "image_name": f"page-{i}.jpg",
            "width": width,
            "height": height,
            "sections": []
        }

        word_json[str(i)] = []

        ocr = pytesseract.image_to_data(page, output_type=pytesseract.Output.DICT)
        all_text = []

        for j in range(len(ocr["text"])):
            word = ocr["text"][j].strip()
            if word:
                x = ocr["left"][j]
                y = ocr["top"][j]
                w = ocr["width"][j]
                h = ocr["height"][j]
                word_json[str(i)].append({
                    "text": word,
                    "bbox": [x, y, x + w, y + h]
                })
                all_text.append(word)

        layout_json[str(i)]["sections"].append({
            "bbox": [0, 0, 1, 1],
            "class": "FullPage",
            "score": 1.0,
            "text": " ".join(all_text)
        })

    return layout_json, word_json

# Highlight words in image
def render_with_highlights(pages, word_json, queries):
    for i, page in enumerate(pages):
        if str(i) not in word_json:
            continue

        draw = ImageDraw.Draw(page)

        for word_obj in word_json[str(i)]:
            word_text = word_obj["text"].lower()
            if any(q.lower() in word_text for q in queries):
                x1, y1, x2, y2 = word_obj["bbox"]
                draw.rectangle([x1, y1, x2, y2], outline="red", width=2)

        st.image(page, caption=f"Page {i+1}", use_container_width=True)

# ------------------ STREAMLIT APP ------------------

st.set_page_config(layout="wide")
st.title("📄 Word-Level Coordinate Highlighter (Tesseract + Streamlit)")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    max_pages = st.number_input("📥 Enter number of pages to process", min_value=1, value=5)

    with st.spinner("⚙️ Processing... please wait..."):
        pages = convert_from_bytes(uploaded_file.read(), fmt="jpeg")
        layout_json, word_json = process_pdf_with_tesseract(pages, max_pages)
        save_json(layout_json, "output/layout.json")
        save_json(word_json, "output/wordjson.json")

    st.success("✅ Processing complete! JSON files saved.")

    # Keyword search
    queries = []
    st.markdown("### 🔍 Search up to 5 Keywords")
    for i in range(5):
        word = st.text_input(f"Keyword {i+1}", key=f"query_{i}")
        if word:
            queries.append(word)

    st.markdown("---")
    if queries:
        st.markdown("### 🔦 Highlighted Results")
        render_with_highlights(pages, word_json, queries)
    else:
        st.image(pages[0], caption="Page 1", use_container_width=True)
