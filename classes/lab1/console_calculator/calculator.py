"""
Calculator Module

This module provides functions for making calculations, formatting results,
changing decimal places, and managing calculation history.
"""

import re
from UI.menu import Menu
from UI.menu_item import Item
from shared.history import History
from shared.settings import get_lab_settings
from classes.lab1.math_operations.math_operations import make_calculations
from classes.lab1.console_calculator.console_reader.data_from_console import get_parameters_from_console, get_operator_from_console

settings = get_lab_settings("lab1")
HISTORY_PATH = settings["history_path"]
DECIMAL_PLACES = settings["decimal_places"]

history = History(HISTORY_PATH)


def lab_menu():
    """
    This function creates and runs a menu for Lab 1.
    The menu allows the user to perform calculations, change decimal places,
    view history, clear history, and exit the program.
    """
    main_menu = Menu("\nMenu (Lab 1)")
    main_menu.add_item(Item('1', 'Make Calculations', make_calculation))
    main_menu.add_item(Item('2', 'Change Decimal Places (default 2)', change_decimal_places))
    main_menu.add_item(Item('3', 'View History', view_history))
    main_menu.add_item(Item('4', 'Clear History', clear_history))
    main_menu.add_item(Item('0', 'Exit'))
    crate_history_file()
    
    main_menu.run()

def make_calculation():
    """
    Makes a calculation based on user input.

    This function prompts the user to enter two parameters and an operator.
    It then performs the calculation using the `make_calculations` function.
    If the calculation is successful, it formats the result and prints it.
    The user is given the option to save the result to the history.
    """
    parameter1, parameter2 = get_parameters_from_console()
    operator = get_operator_from_console()
    calculation_result = make_calculations(parameter1, parameter2, operator)
    if calculation_result is None:
        print("Calculations were not made due to the error!")
        return
    formated_result = format_result(parameter1, parameter2, operator, calculation_result)
    print_calculation_result(formated_result)

def format_result(parameter1, parameter2, operator, calculation_result):
    """
    Formats the calculation result based on the operator.

    Args:
        parameter1 (float): The first parameter of the calculation.
        parameter2 (float): The second parameter of the calculation.
        operator (str): The operator used in the calculation.
        calculation_result (float or tuple): The result of the calculation.

    Returns:
        str: The formatted calculation result.
    """
    if operator == "//":
        formatted_calculation_result1 = f"{calculation_result[0]:.{get_decimal_places_from_history()}f}"
        formatted_calculation_result2 = f"{calculation_result[1]:.{get_decimal_places_from_history()}f}"
        result = f"Square root of {parameter1} = {formatted_calculation_result1}, Square root of {parameter2} = {formatted_calculation_result2}"
    else:
        formatted_calculation_result = f"{calculation_result:.{get_decimal_places_from_history()}f}"
        result = f"{parameter1} {operator} {parameter2} = {formatted_calculation_result}"
    return result

def print_calculation_result(result):
    """
    Prints the calculation result and prompts the user to save it to the history.

    Args:
        result (str): The formatted calculation result.
    """
    print(result)
    choice = str(input("Do you want to save the result? [Y/n] "))
    if choice.upper() == "Y":
        history.add_event(result)

def change_decimal_places():
    """
    Prompts the user to enter the number of decimal places and writes it to the history file.
    """
    decimal_places = int(input("Enter the number of decimal places: "))
    write_decimal_places_to_file(decimal_places)

def write_decimal_places_to_file(decimal_places=DECIMAL_PLACES):
    """
    Writes the number of decimal places to the history file.

    Args:
        decimal_places (int): The number of decimal places to be written.
    """
    
    if HISTORY_PATH:
        try:
            with open(HISTORY_PATH, 'r', encoding="utf-8") as file:
                lines = file.readlines()
            if lines:
                lines[0] = f'Decimal places: {decimal_places}\n'
            with open(HISTORY_PATH, 'w', encoding="utf-8") as file:
                file.writelines(lines)
        except FileNotFoundError:
            print("History file not found!")
        else:
            try:
                with open(HISTORY_PATH, 'r', encoding="utf-8") as file:
                    history.add_event(f'Decimal places: {decimal_places}\n')
            except Exception as exception:
                print(f"An error occurred: {exception}")
    

def get_decimal_places_from_history():
    """
    Retrieves the number of decimal places from the history file.

    Returns:
        int: The number of decimal places.
    """
    try:
        with open(HISTORY_PATH, 'r', encoding="utf-8") as file:
            file_content = file.read()

            pattern = r'\d+'
            decimal_places = re.findall(pattern, file_content)

        if not decimal_places:
            return DECIMAL_PLACES
        return decimal_places[0]
    except FileNotFoundError:
        print("History file not found!")
    except Exception as exception:
        print(f"An error occurred: {exception}")

def crate_history_file():
    """
    Creates a history file with default decimal places.
    """
    try:
        with open(HISTORY_PATH, 'w', encoding='utf-8') as file:
            file.write("Decimal places: 2\n")
    except Exception as exception:
        print(f"An error occurred: {exception}")

def view_history():
    """
    Prints the history of calculations.
    """
    history.print_history()

def clear_history():
    """
    Clears the history of calculations.
    """
    history.clear_history()
