import json
import os

LAYOUT_JSON_PATH = "output/layout.json"
WORD_JSON_PATH = "output/wordjson.json"

def save_layout_json(layout_data):
    os.makedirs("output", exist_ok=True)
    with open(LAYOUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(layout_data, f, indent=2)

def load_layout_json():
    with open(LAYOUT_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_word_json(word_data):
    os.makedirs("output", exist_ok=True)
    with open(WORD_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(word_data, f, indent=2)

def load_word_json():
    with open(WORD_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
