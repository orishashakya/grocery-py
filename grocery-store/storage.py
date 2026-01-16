import json
from pathlib import Path

def load_data(file_path):
    path = Path(file_path)
    if not path.exists():
        # return empty dict for inventory, empty list for sales
        return {} if "inventory" in file_path else []
    with open(path, "r") as file:
        return json.load(file)

def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
