import json


def save_json(name, data):
    with open(f"{name}.json", "w") as file:
        json.dump(data, file, indent=4)
