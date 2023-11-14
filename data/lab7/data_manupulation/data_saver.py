import json
import csv
import sys
sys.path.append('/home/olena/NULP/3 курс/SPL/labs')

from shared.file_handler import FileHandler
home_path = "/home/olena/NULP/3 курс/SPL/labs/data/lab7/saved_data/"
class DataSaver:
    def __init__(self, data):
        self.data = data

    def save_to_json(self):
        json_file = FileHandler(home_path + "data.json")
        json_file.write_to_file(json.dumps(self.data, indent=2))

    def save_to_csv(self):
        file_path = home_path + "data.csv"

        if isinstance(self.data, dict):
            self.data = [self.data]

        flat_list = [self.flatten_json(item) for item in self.data]
        fieldnames = flat_list[0].keys() if flat_list else []
        

        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(flat_list)

    def save_to_txt(self):
        txt_file = (home_path + "data.txt")

        if isinstance(self.data, dict):
            self.data = [self.data]
            
        flat_list = [self.flatten_json(item) for item in self.data]
        with open(txt_file, 'w', encoding='utf-8') as txt_file:
            for item in flat_list:
                for key, value in item.items():
                    txt_file.write(f"{key}: {value}\n")
                txt_file.write('\n')

    def flatten_json(self, data, parent_key='', sep='.'):
        flat_data = {}
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                flat_data.update(self.flatten_json(value, new_key, sep=sep))
            else:
                flat_data[new_key] = value
        return flat_data