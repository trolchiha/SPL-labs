"""
data_from_console Module

This module provides functions for getting parameters and an operator from the console.
"""

from shared.input_handler import InputHandler

def get_parameters_from_console():
    """
    Get two float numbers from the console.

    Returns:
        tuple: A tuple containing the two float numbers entered by the user.
    """
    parameter1 = InputHandler().get_float_input("Enter the first number")
    parameter2 = InputHandler().get_float_input("Enter the second number")
    return parameter1, parameter2

def get_operator_from_console():
    """
    Get an operator from the console.

    Returns:
        str: The operator entered by the user.
    """
    available_operators = ['+', '-', '*', '/', '**', '//', '%']
    operator = InputHandler().get_one_of_list_input(f"Enter the operator {available_operators}", available_operators)
    return operator
