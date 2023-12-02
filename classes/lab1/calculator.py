import re
from shared.history import History
from .math_operations import *
from .data_from_console import get_parameters_from_console, get_operator_from_console
from .settings import HISTORY_PATH, DECIMAL_PLACES

history = History(HISTORY_PATH)

def make_calculation():
    parameter1, parameter2 = get_parameters_from_console()
    operator = get_operator_from_console()
    calculation_result = make_calculations(parameter1, parameter2, operator)
    if calculation_result is None:
        print("Calculations were not made due to the error!")
        return
    formated_result = format_result(parameter1, parameter2, operator, calculation_result)
    print_calculation_result(formated_result)

def format_result(parameter1, parameter2, operator, calculation_result):
    if operator == "//":
        formatted_calculation_result1 = f"{calculation_result[0]:.{get_decimal_places()}f}"
        formatted_calculation_result2 = f"{calculation_result[1]:.{get_decimal_places()}f}"
        result = f"Square root of {parameter1} = {formatted_calculation_result1}, Square root of {parameter2} = {formatted_calculation_result2}"
    else:
        formatted_calculation_result = f"{calculation_result:.{get_decimal_places()}f}"
        result = f"{parameter1} {operator} {parameter2} = {formatted_calculation_result}"
    return result

def print_calculation_result(result):
    print(result)
    choice = str(input("Do you want to save the result? [Y/n] "))
    if choice == "y" or choice == "Y":
        history.add_event(result)

def change_decimal_places():
    decimal_places = int(input("Enter the number of decimal places: "))
    write_decimal_places_to_file(decimal_places)

def write_decimal_places_to_file(decimal_places=DECIMAL_PLACES):
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

def get_decimal_places():
    with open(HISTORY_PATH, 'r') as file:
        file_content = file.read()

        pattern = r'\d+'
        decimal_places = re.findall(pattern, file_content)

    return decimal_places[0]

def crate_history_file():
    with open(HISTORY_PATH, 'w') as file:
        file.write("Decimal places: 2\n")

def view_history():
    history.print_history()

def clear_history():
    history.clear_history()
