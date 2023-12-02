class InputHandler:
    def __init__(self):
        input_data = None

    def get_str_input(self, message):
        input_data = input(f"{message}: ")
        self.input_data = input_data
        return input_data
    
    def get_int_input(self, message):
        input_data = input(f"{message}: ")
        while not input_data.isdigit():
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return int(input_data)
    
    def get_float_input(self, message):
        input_data = input(f"{message}: ")
        while not input_data.replace('.', '', 1).isdigit():
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return float(input_data)
    
    def get_one_char_input(self, message):
        input_data = input(f"{message}: ")
        while len(input_data) != 1:
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return input_data
    
    def get_one_of_list_input(self, message, list):
        input_data = input(f"{message}: ")
        while not self.check_input_in_list(input_data, list):
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return input_data
    
    def check_input_in_list(self, input_data, list):   
        if input_data in list:
            return True
        else:
            return False
    
    def get_input_with_condition(self, message, condition):
        input_data = input(f"{message}: ")
        while not condition(input_data):
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return input_data
