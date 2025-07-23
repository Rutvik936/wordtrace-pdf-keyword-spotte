import easyocr
<<<<<<< HEAD
import numpy as np
from PIL import Image

# Initialize EasyOCR reader
=======
from PIL import Image

>>>>>>> 4ed58c0c644588fbc119144a75b322f8951810a1
reader = easyocr.Reader(['en'], gpu=False)

def process_pdf_with_textract(pages):
    layout_json = {}
    word_json = {}

    for i, page in enumerate(pages):
        page_num = str(i)
        width, height = page.size

<<<<<<< HEAD
        # Define dummy layout regions (can be replaced with model-based detection)
=======
        # Dummy layout regions
>>>>>>> 4ed58c0c644588fbc119144a75b322f8951810a1
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
<<<<<<< HEAD

            # ✅ Convert PIL image to numpy array before passing to EasyOCR
            results = reader.readtext(np.array(cropped))
=======
            results = reader.readtext(cropped)
>>>>>>> 4ed58c0c644588fbc119144a75b322f8951810a1

            text_buffer = []

            for (bbox, text, conf) in results:
<<<<<<< HEAD
                # bbox is a list of 4 points: [[x1, y1], [x2, y2], ...]
=======
                # bbox = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
>>>>>>> 4ed58c0c644588fbc119144a75b322f8951810a1
                x_coords = [pt[0] + region_box[0] for pt in bbox]
                y_coords = [pt[1] + region_box[1] for pt in bbox]
                x1, y1, x2, y2 = min(x_coords), min(y_coords), max(x_coords), max(y_coords)

                word_json[page_num].append({
                    "text": text,
                    "bbox": [x1, y1, x2, y2]
                })

                text_buffer.append(text)

<<<<<<< HEAD
            # Normalize layout section bbox to [0–1] format
=======
            # Normalize bounding box for layout.json
>>>>>>> 4ed58c0c644588fbc119144a75b322f8951810a1
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
