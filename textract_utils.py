import easyocr
import numpy as np
from PIL import Image

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'], gpu=False)

def process_pdf_with_textract(pages):
    layout_json = {}
    word_json = {}

    for i, page in enumerate(pages):
        page_num = str(i)
        width, height = page.size

        # Define dummy layout regions (can be replaced with model-based detection)
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
            cropped = page.crop(region_box)

            # ✅ Convert PIL image to numpy array before passing to EasyOCR
            results = reader.readtext(np.array(cropped))

            text_buffer = []

            for (bbox, text, conf) in results:
                # bbox is a list of 4 points: [[x1, y1], [x2, y2], ...]
                x_coords = [pt[0] + region_box[0] for pt in bbox]
                y_coords = [pt[1] + region_box[1] for pt in bbox]
                x1, y1, x2, y2 = min(x_coords), min(y_coords), max(x_coords), max(y_coords)

                word_json[page_num].append({
                    "text": text,
                    "bbox": [x1, y1, x2, y2]
                })

                text_buffer.append(text)

            # Normalize layout section bbox to [0–1] format
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
