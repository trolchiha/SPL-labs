def get_parameters_from_console():
    try:
        parameter1 = float(input("Enter the first number: "))
        parameter2 = float(input("Enter the second number: "))
    except ValueError as e:
        print(f'Error message: {str(e)}')
        return get_parameters_from_console()
    else:
        return parameter1, parameter2
    

def get_operator_from_console():
    try:
        operator = input("Enter the operator ['+', '-', '*', '/', '**', '//', '%']: ")
        if operator not in ['+', '-', '*', '/', '**', '//', '%']:
            raise ValueError("invalid operator")
    except ValueError as e:
        print(f'Error message: {str(e)}')
        return get_operator_from_console()
    else:
        return operator