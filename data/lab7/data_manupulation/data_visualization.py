from texttable import Texttable
from tabulate import tabulate
from colorama import Fore, Style


class DataVisualization:
    def __init__(self, data):
        self.data = data


    def visualize_as_table(self):
        if isinstance(self.data, dict):
            self.data = [self.data]
        
        flat_list = [self.flatten_json(item) for item in self.data]
        headers = flat_list[0].keys()

        colored_headers = [f"{Fore.GREEN}{header}{Style.RESET_ALL}" for header in headers]
        column_width = 100 // len(colored_headers)
        
        table = []
        for item in flat_list:
            table.append(item.values())

        print(tabulate(table, colored_headers, tablefmt="grid", maxcolwidths=column_width))


    def visualize_as_list(self):
        if isinstance(self.data, dict):
            self.data = [self.data]
            
        flat_list = [self.flatten_json(item) for item in self.data]
        
        for i, item in enumerate(flat_list):
            line = f"{i+1}. "
            for j, key in enumerate(item):
                if j == 0:
                    print(f"{line}{Fore.GREEN}{key}{Style.RESET_ALL} - {item.get(key)}")
                else:
                    spaces = len(line)*" "
                    print(f"{spaces}{Fore.GREEN}{key}{Style.RESET_ALL} - {item.get(key)}")
            print()


    def flatten_json(self, data, parent_key='', sep='.'):
        flat_data = {}
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                flat_data.update(self.flatten_json(value, new_key, sep=sep))
            else:
                flat_data[new_key] = value
        return flat_data
