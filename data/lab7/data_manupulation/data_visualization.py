from tabulate import tabulate
from colorama import Fore, Style
from data.lab7.data_manupulation.data_from_console import get_color

class DataVisualization:
    def __init__(self, data):
        self.data = data
        self.color = Fore.WHITE

    def visualize_as_table(self):
        if isinstance(self.data, dict):
            self.data = [self.data]
        
        flat_list = [self.flatten_json(item) for item in self.data]
        headers = flat_list[0].keys()

        colored_headers = [f"{self.color}{header}{Style.RESET_ALL}" for header in headers]
        max_col_width = 100 // len(headers)
        
        table = []
        for item in flat_list:
            table.append(item.values())

        print(tabulate(table, colored_headers, tablefmt="fancy_grid", maxcolwidths=max_col_width))


    def visualize_as_list(self):
        if isinstance(self.data, dict):
            self.data = [self.data]
            
        flat_list = [self.flatten_json(item) for item in self.data]
        
        for i, item in enumerate(flat_list):
            line = f"{i+1}. "
            for j, key in enumerate(item):
                if j == 0:
                    print(f"{line}{self.color}{key}{Style.RESET_ALL} - {item.get(key)}")
                else:
                    spaces = len(line)*" "
                    print(f"{spaces}{self.color}{key}{Style.RESET_ALL} - {item.get(key)}")
            print()

    def settings(self):
        self.color = get_color()

    def view_settings(self):
        print("Color:", self.color)

    def flatten_json(self, data, parent_key='', sep='.'):
        flat_data = {}
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                flat_data.update(self.flatten_json(value, new_key, sep=sep))
            else:
                flat_data[new_key] = value
        return flat_data
