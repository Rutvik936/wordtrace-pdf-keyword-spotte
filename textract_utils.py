import numpy as np
from PIL import Image
import easyocr

reader = easyocr.Reader(['en'])

def process_pdf_with_textract(pages):
    layout_json = {}
    word_json = {}

    for i, page in enumerate(pages):
        page_num = str(i)
        width, height = page.size

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
            np_img = np.array(cropped)

            results = reader.readtext(np_img)
            text_buffer = []

            for (bbox, text, conf) in results:
                if conf < 0.3:
                    continue

                x1, y1 = map(int, bbox[0])
                x2, y2 = map(int, bbox[2])

                word_json[page_num].append({
                    "text": text,
                    "bbox": [x1 + region_box[0], y1 + region_box[1], x2 + region_box[0], y2 + region_box[1]]
                })

                text_buffer.append(text)

            norm = [region_box[0]/width, region_box[1]/height,
                    region_box[2]/width, region_box[3]/height]

            layout_json[page_num]["sections"].append({
                "bbox": norm,
                "class": region_class,
                "score": 0.85,
                "text": " ".join(text_buffer)
            })

    return layout_json, word_json
