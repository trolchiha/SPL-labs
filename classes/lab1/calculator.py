import re
from shared.history import History
from .math_operations import *
from .data_from_console import get_parameters_from_console, get_operator_from_console
from .settings import HISTORY_PATH, DECIMAL_PLACES

history = History(HISTORY_PATH)

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
    if choice == "y" or choice == "Y":
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
        with open(HISTORY_PATH, 'r') as file:
            lines = file.readlines()
        if lines:
            lines[0] = f'Decimal places: {decimal_places}\n'
        with open(HISTORY_PATH, 'w') as file:
            file.writelines(lines)
    else:
        with open(HISTORY_PATH, 'r') as file:
            history.add_event(f'Decimal places: {decimal_places}\n')

def get_decimal_places_from_history():
    """
    Retrieves the number of decimal places from the history file.

    Returns:
        int: The number of decimal places.
    """
    with open(HISTORY_PATH, 'r') as file:
        file_content = file.read()

        pattern = r'\d+'
        decimal_places = re.findall(pattern, file_content)

    if not decimal_places:
        return DECIMAL_PLACES
    return decimal_places[0]

def crate_history_file():
    """
    Creates a history file with default decimal places.
    """
    with open(HISTORY_PATH, 'w') as file:
        file.write("Decimal places: 2\n")

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
