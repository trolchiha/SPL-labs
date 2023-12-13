"""
Data Visualization Module

A module that defines the DataVisualization class for visualizing data as a table or a list. 
Contains the flatten_json_data function for flattening a nested JSON object.
"""
from tabulate import tabulate
from colorama import Fore, Style
from shared.settings import get_lab_settings
from .data_from_console import get_color

settings = get_lab_settings("lab7")
DEFAULT_DATA_VISUALIZATION_SETTINGS = settings["data_visualization_settings"]
DEFAULT_TABLE_FORMAT = DEFAULT_DATA_VISUALIZATION_SETTINGS["table"]
DEFAULT_COLOR = DEFAULT_DATA_VISUALIZATION_SETTINGS["color"]

class DataVisualization:
    """
    A class that provides methods for visualizing data as a table or a list.
    """

    def __init__(self):
        """
        Initializes an instance of the DataVisualization class.
        """
        self.data = None
        self.color = DEFAULT_COLOR

    def set_data(self, data):
        """
        Set the data to be visualized.

        Parameters:
        - data: The data to be visualized.
        """
        self.data = data

    def visualize_as_table(self):
        """
        Visualize the data as a table.
        """
        if isinstance(self.data, dict):
            self.data = [self.data]
        
        flat_list = [self.flatten_json_data(item) for item in self.data]
        headers = flat_list[0].keys()

        color = getattr(Fore, self.color, None)

        colored_headers = [f"{color}{header}{Style.RESET_ALL}" for header in headers]
        max_col_width = 90 // len(headers)
        
        table = []
        for item in flat_list:
            table.append(item.values())

        print(tabulate(table, colored_headers, tablefmt=DEFAULT_TABLE_FORMAT, maxcolwidths=max_col_width))


    def visualize_as_list(self):
        """
        Visualize the data as a list.
        """
        if isinstance(self.data, dict):
            self.data = [self.data]
            
        color = getattr(Fore, self.color, None)
        flat_list = [self.flatten_json_data(item) for item in self.data]
        
        for i, item in enumerate(flat_list):
            line = f"{i+1}. "
            for j, key in enumerate(item):
                if j == 0:
                    print(f"{line}{color}{key}{Style.RESET_ALL} - {item.get(key)}")
                else:
                    spaces = len(line)*" "
                    print(f"{spaces}{color}{key}{Style.RESET_ALL} - {item.get(key)}")
            print()

    def settings(self):
        """
        Set the color for data visualization.
        """
        color = get_color()
        self.color = color
        print(self.color)

    def view_settings(self):
        """
        View the current color setting for data visualization.
        """
        print("Color:", self.color)

    def flatten_json_data(self, data, parent_key='', sep='.'):
        """
        Flatten a nested JSON object.

        Parameters:
        - data: The JSON object to be flattened.
        - parent_key: The parent key of the current level of the JSON object (default: '').
        - sep: The separator to be used between keys (default: '.').

        Returns:
        - flat_data: The flattened JSON object.
        """
        flat_data = {}
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                flat_data.update(self.flatten_json_data(value, new_key, sep=sep))
            else:
                flat_data[new_key] = value
        return flat_data
