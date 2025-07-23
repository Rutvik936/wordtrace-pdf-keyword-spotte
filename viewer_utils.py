import streamlit as st
from PIL import ImageDraw

def render_pdf_with_highlights(pages, word_json, queries):
    for i, page in enumerate(pages):
        img_copy = page.copy()
        draw = ImageDraw.Draw(img_copy)

        for word_obj in word_json.get(str(i), []):
            word_text = word_obj["text"].lower()
            if any(q.lower() in word_text for q in queries):
                box = word_obj["bbox"]
                draw.rectangle(box, outline="red", width=2)

        st.image(img_copy, caption=f"Page {i+1}", use_container_width=True)
