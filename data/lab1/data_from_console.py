def get_parameters_from_console():
    try:
        parameter1 = float(input("Enter the first number: "))
        parameter2 = float(input("Enter the second number: "))
    except Exception as e:
        print(f'Error message: {str(e)}')
        return get_parameters_from_console()
    else:
        return parameter1, parameter2
    

def get_operator_from_console():
    operator = input("Enter the operator ['+', '-', '*', '/', '**', '//', '%']: ")
    while operator not in ['+', '-', '*', '/', '**', '//', '%']:
        print("Invalid operator! Try again.")
        operator = input("Enter the operator: ")
    return operator