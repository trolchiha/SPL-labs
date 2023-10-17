def get_parameters_from_console():
    parameter1 = float(input("Enter the first number: "))
    parameter2 = float(input("Enter the second number: "))

    return parameter1, parameter2

def get_operator_from_console():
    operator = input("Enter the operator ['+', '-', '*', '/', '**', '//', '%']: ")
    while operator not in ['+', '-', '*', '/', '**', '//', '%']:
        print("Invalid operator! Try again.")
        operator = input("Enter the operator: ")
    return operator