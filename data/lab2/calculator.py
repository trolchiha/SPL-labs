from shared.history import History
from UI.menu import Menu
from UI.menu_item import Item

from data.lab1.math_operations import make_calculations
from data.lab1.data_from_console import get_parameters_from_console, get_operator_from_console

history_path = "data/lab2/history.txt"

class Calculator:
    def __init__(self):
        self.history = History(history_path)
        self.terminal_menu = Menu("Menu")
        self.decimal_places = 2

    def menu(self):
        self.terminal_menu.add_item(Item("1", "Perform calculations", self.perform_calculations))
        self.terminal_menu.add_item(Item("2", "Change decimal places (default 2)", self.change_decimal_places))
        self.terminal_menu.add_item(Item("3", "View history", self.view_history))
        self.terminal_menu.add_item(Item("4", "Clear history", self.clear_history))
        self.terminal_menu.add_item(Item("0", "Exit", self.exit))
        self.terminal_menu.run()

    def perform_calculations(self):
        parameter1, parameter2 = get_parameters_from_console()
        operator = get_operator_from_console()
        result = make_calculations(parameter1, parameter2, operator)
        formatted_result = self.format_result(parameter1, parameter2, operator, result)
        self.print_calculation_result(formatted_result)
    
    def change_decimal_places(self):
        self.decimal_places = int(input("Enter the number of decimal places: "))
        
    def format_result(self, parameter1, parameter2, operator, calculation_result):
        if operator == "//":
            formatted_calculation_result1 = f"{calculation_result[0]:.{self.decimal_places}f}"
            formatted_calculation_result2 = f"{calculation_result[1]:.{self.decimal_places}f}"
            result = f"Square root of {parameter1} = {formatted_calculation_result1}, Square root of {parameter2} = {formatted_calculation_result2}"
        else:
            formatted_calculation_result = f"{calculation_result:.{self.decimal_places}f}"
            result = f"{parameter1} {operator} {parameter2} = {formatted_calculation_result}"
        return result

    def print_calculation_result(self, result):
        print(result)
        sub_choice = str(input("Do you want to save the result? [Y/n] "))
        if sub_choice == "y" or sub_choice == "Y":
            self.history.add_event(result)

    def view_history(self):
        self.history.print_history()

    def clear_history(self):
        self.history.clear_history()

    def exit(self):
        print("Exiting...")
        sys.exit()
            