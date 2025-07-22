# ✅ textract_utils.py (Updated for layout JSON format)

import pytesseract
from pytesseract import Output
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# ✅ Updated function to include layout.json structure

def process_pdf_with_textract(pages):
    layout_json = {}
    word_json = {}

    for i, page in enumerate(pages):
        page_num = str(i)
        width, height = page.size

        # 👇 Define dummy layout regions (replace with real detection later)
        title_box = [int(width * 0.1), int(height * 0.05), int(width * 0.9), int(height * 0.15)]
        table_box = [int(width * 0.1), int(height * 0.25), int(width * 0.9), int(height * 0.75)]

        layout_json[page_num] = {
            "image_name": f"page-{page_num}.jpg",
            "width": width,
            "height": height,
            "sections": []
        }

        word_json[page_num] = []

        for region_class, region_box in zip(["Title", "Table"], [title_box, table_box]):
            cropped_region = page.crop(region_box)
            ocr_data = pytesseract.image_to_data(cropped_region, output_type=Output.DICT)

            text_buffer = []

            for j in range(len(ocr_data["text"])):
                word = ocr_data["text"][j].strip()
                if word:
                    x, y, w, h = (
                        ocr_data["left"][j] + region_box[0],
                        ocr_data["top"][j] + region_box[1],
                        ocr_data["width"][j],
                        ocr_data["height"][j],
                    )
                    x1, y1, x2, y2 = x, y, x + w, y + h

                    word_json[page_num].append({
                        "text": word,
                        "bbox": [x1, y1, x2, y2]
                    })

                    text_buffer.append(word)

            # Normalize bbox to [0–1] for layout.json
            x1_norm = region_box[0] / width
            y1_norm = region_box[1] / height
            x2_norm = region_box[2] / width
            y2_norm = region_box[3] / height

            layout_json[page_num]["sections"].append({
                "bbox": [x1_norm, y1_norm, x2_norm, y2_norm],
                "class": region_class,
                "score": 0.85,
                "text": " ".join(text_buffer)
            })

    return layout_json, word_json