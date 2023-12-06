import logging

logger = logging.getLogger(__name__)

class InputHandler:
    def __init__(self):
        self.input_data = None

    def get_str_input(self, message):
        input_data = input(f"{message}: ")
        self.input_data = input_data
        return input_data
    
    def get_int_input(self, message):
        input_data = input(f"{message}: ")
        while not input_data.isdigit():
            logger.warning("The input %s is not a number.", input_data)
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return int(input_data)
    
    def get_float_input(self, message):
        input_data = input(f"{message}: ")
        while not input_data.replace('.', '', 1).isdigit():
            logger.warning("The input %s is not a float number.", input_data)
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return float(input_data)
    
    def get_one_char_input(self, message):
        input_data = input(f"{message}: ")
        while len(input_data) != 1:
            logger.warning("The input %s is not one character.", input_data)
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return input_data
    
    def get_one_of_list_input(self, message, list):
        input_data = input(f"{message}: ")
        while not self.check_input_in_list(input_data, list):
            logger.warning("The input %s is not in the list.", input_data)
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return input_data
    
    def get_one_of_list_input_ignore_case(self, message, list):
        input_data = input(f"{message}: ")
        while not self.check_input_in_list_ignore_case(input_data, list):
            logger.warning("The input %s is not in the list.", input_data)
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return input_data
    
    def check_input_in_list_ignore_case(self, input_data, list):
        input_data = input_data.lower()
        for item in list:
            if input_data == item.lower():
                return True
        return False
    
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
