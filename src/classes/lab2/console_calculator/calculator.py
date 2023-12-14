"""
Calculator Module

This module defines the Calculator class, representing a calculator with methods for performing calculations,
changing decimal places, viewing history, and clearing history. It uses components from other modules, such as
the History class, math_operations module, and console_reader module.
"""
from UI.menu import Menu
from UI.menu_item import Item
from shared.history import History
from shared.settings import get_lab_settings
from classes.lab1.math_operations.math_operations import make_calculations
from classes.lab1.console_calculator.console_reader.data_from_console import get_parameters_from_console, get_operator_from_console

settings = get_lab_settings("lab2")

HISTORY_PATH = settings["history_path"]
DECIMAL_PLACES = settings["decimal_places"]


class Calculator:
    """
    A class representing a calculator.

    Attributes:
    - history (History): The history of calculations.
    - decimal_places (int): The number of decimal places to round the results to.
    """

    def __init__(self):
        """
        Initializes a new instance of the Calculator class.

        Parameters:
        - None
        """
        self.history = History(HISTORY_PATH)
        self.decimal_places = DECIMAL_PLACES

    def menu(self):
        """
        Displays a menu with options for the user to choose from.
        """
        self.terminal_menu = Menu("Menu")
        self.terminal_menu.add_item(Item("1", "Perform calculations", self.perform_calculations))
        self.terminal_menu.add_item(Item("2", "Change decimal places (default 2)", self.change_decimal_places))
        self.terminal_menu.add_item(Item("3", "View history", self.view_history))
        self.terminal_menu.add_item(Item("4", "Clear history", self.clear_history))
        self.terminal_menu.add_item(Item("0", "Exit"))
        self.terminal_menu.run()

    def get_history(self):
        """
        Returns the history of calculations.

        Parameters:
        - None

        Returns:
        - history (History): The history of calculations.
        """
        return self.history
    
    def get_decimal_places(self):
        """
        Returns the number of decimal places.

        Parameters:
        - None

        Returns:
        - decimal_places (int): The number of decimal places.
        """
        return self.decimal_places
    
    def set_decimal_places(self, decimal_places):
        """
        Sets the number of decimal places.

        Parameters:
        - decimal_places (int): The number of decimal places to set.

        Returns:
        - None
        """
        if decimal_places > 0:
            self.decimal_places = decimal_places
        else:
            print("The number of decimal places must be greater than 0.")

    def perform_calculations(self):
        """
        Performs calculations based on user input.

        Parameters:
        - None

        Returns:
        - None
        """
        parameter1, parameter2 = get_parameters_from_console()
        operator = get_operator_from_console()
        result = make_calculations(parameter1, parameter2, operator)
        formatted_result = self.__format_result(parameter1, parameter2, operator, result)
        self.print_calculation_result(formatted_result)
    
    def change_decimal_places(self):
        """
        Changes the number of decimal places.

        Parameters:
        - None

        Returns:
        - None
        """
        decimal_places = int(input("Enter the number of decimal places: "))
        self.set_decimal_places(decimal_places)
        
    def __format_result(self, parameter1, parameter2, operator, calculation_result):
        """
        Formats the calculation result.

        Parameters:
        - parameter1 (float): The first parameter of the calculation.
        - parameter2 (float): The second parameter of the calculation.
        - operator (str): The operator used in the calculation.
        - calculation_result (float or tuple): The result of the calculation.

        Returns:
        - result (str): The formatted calculation result.
        """
        if operator == "//":
            formatted_calculation_result1 = f"{calculation_result[0]:.{self.get_decimal_places()}f}"
            formatted_calculation_result2 = f"{calculation_result[1]:.{self.get_decimal_places()}f}"
            result = f"Square root of {parameter1} = {formatted_calculation_result1}, Square root of {parameter2} = {formatted_calculation_result2}"
        else:
            formatted_calculation_result = f"{calculation_result:.{self.get_decimal_places()}f}"
            result = f"{parameter1} {operator} {parameter2} = {formatted_calculation_result}"
        return result

    def print_calculation_result(self, result):
        """
        Prints the calculation result and saves it to history if requested.

        Parameters:
        - result (str): The calculation result to print.

        Returns:
        - None
        """
        print(result)
        sub_choice = str(input("Do you want to save the result? [Y/n] "))
        if sub_choice.upper() == "Y":
            self.history.add_event(result)

    def view_history(self):
        """
        Prints the calculation history.

        Parameters:
        - None

        Returns:
        - None
        """
        self.get_history().print_history()

    def clear_history(self):
        """
        Clears the calculation history.

        Parameters:
        - None

        Returns:
        - None
        """
        self.get_history().clear_history()
            