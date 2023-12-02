from shared.input_handler import InputHandler

def get_parameters_from_console():
    parameter1 = InputHandler().get_float_input("Enter the first number")
    parameter2 = InputHandler().get_float_input("Enter the second number")
    return parameter1, parameter2

def get_operator_from_console():
    available_operators = ['+', '-', '*', '/', '**', '//', '%']
    operator = InputHandler().get_one_of_list_input(f"Enter the operator {available_operators}", available_operators)
    return operator