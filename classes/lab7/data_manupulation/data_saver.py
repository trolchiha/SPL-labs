import json
import csv

from shared.file_handler import FileHandler
from classes.lab7.settings import JSON_FILE_PATH, CSV_FILE_PATH, TXT_FILE_PATH

class DataSaver:
    def __init__(self, data):
        self.data = data

    def save_to_json(self):
        json_file = FileHandler(JSON_FILE_PATH)
        json_file.write_to_file(json.dumps(self.data, indent=2))

    def save_to_csv(self):
        if isinstance(self.data, dict):
            self.data = [self.data]

        flat_list = [self.flatten_json(item) for item in self.data]
        fieldnames = flat_list[0].keys() if flat_list else []

        with open(CSV_FILE_PATH, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(flat_list)

    def save_to_txt(self):
        txt_file = FileHandler(TXT_FILE_PATH)
        txt_file.write_to_file("")
        
        if isinstance(self.data, dict):
            self.data = [self.data]
            
        flat_list = [self.flatten_json(item) for item in self.data]
        for item in flat_list:
            for key, value in item.items():
                txt_file.append_to_file(f"{key}: {value}\n")
            txt_file.append_to_file('\n')

    def flatten_json(self, data, parent_key='', sep='.'):
        flat_data = {}
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                flat_data.update(self.flatten_json(value, new_key, sep=sep))
            else:
                flat_data[new_key] = value
        return flat_data