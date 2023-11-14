from texttable import Texttable

class DataVisualization:
    def __init__(self, data):
        self.data = data

    def visualize_table(self, header, json):
        table = Texttable()
        table.header(header)
            
        for idx, key in enumerate(json):
            table.add_row([idx+1, key, json.get(key)])

        print(table.draw())

    def visualize_list(self):
        if isinstance(self.data, dict):
            self.data = [self.data]
            
        flat_list = [self.flatten_json(item) for item in self.data]
        print(flat_list)
        for idx, key in enumerate(flat_list):
            print(f"{idx+1}. - {key} - {flat_list.get(key)}")

    def flatten_json(self, data, parent_key='', sep='.'):
        flat_data = {}
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                flat_data.update(self.flatten_json(value, new_key, sep=sep))
            else:
                flat_data[new_key] = value
        return flat_data
