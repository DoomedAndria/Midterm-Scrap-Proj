import json
import os.path

from config import ROOT_DIR


def save_json(name, data):
    with open(f"{os.path.join(ROOT_DIR, 'data/')}{name}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4,ensure_ascii=False)
