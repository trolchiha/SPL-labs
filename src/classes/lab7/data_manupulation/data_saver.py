"""
Data Saving Module

This module provides a class, DataSaver, with methods to save data to different file formats such as JSON, CSV, and TXT.
"""
import json
import csv

from shared.file_handler import FileHandler
from shared.settings import get_lab_settings

settings = get_lab_settings("lab7")
HISTORY_FILE_PATH = settings["history_file_path"]
JSON_FILE_PATH = settings["json_file_path"]
CSV_FILE_PATH = settings["csv_file_path"]
TXT_FILE_PATH = settings["txt_file_path"]

class DataSaver:
    """
    A class that provides methods to save data to different file formats.

    Attributes:
    - data: The data to be saved.
    """

    def __init__(self, data):
        """
        Initializes a DataSaver object.

        Parameters:
        - data: The data to be saved.
        """
        self.data = data

    def save_to_json(self):
        """
        Saves the data to a JSON file.
        """
        json_file = FileHandler(JSON_FILE_PATH)
        json_file.write_to_file(json.dumps(self.data, indent=2))

    def save_to_csv(self):
        """
        Saves the data to a CSV file.
        """
        if isinstance(self.data, dict):
            self.data = [self.data]

        flat_list = [self.flatten_json(item) for item in self.data]
        fieldnames = flat_list[0].keys() if flat_list else []

        with open(CSV_FILE_PATH, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(flat_list)

    def save_to_txt(self):
        """
        Saves the data to a TXT file.
        """
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
        """
        Flattens a nested JSON object.

        Parameters:
        - data: The JSON object to be flattened.
        - parent_key: The parent key for the current level of the JSON object.
        - sep: The separator to be used between keys.

        Returns:
        - flat_data: The flattened JSON object.
        """
        flat_data = {}
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                flat_data.update(self.flatten_json(value, new_key, sep=sep))
            else:
                flat_data[new_key] = value
        return flat_data
    