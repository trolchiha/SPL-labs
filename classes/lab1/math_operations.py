def count_sum(parameter1, parameter2):
    """
    This function takes two parameters and returns their sum.

    Args:
        parameter1 (int): The first parameter.
        parameter2 (int): The second parameter.

    Returns:
        int: The sum of the two parameters.
    """
    return parameter1 + parameter2

def count_difference(parameter1, parameter2):
    """
    This function takes two parameters and returns their difference.

    Args:
        parameter1 (int): The first parameter.
        parameter2 (int): The second parameter.

    Returns:
        int: The difference between the two parameters.
    """
    return parameter1 - parameter2

def count_product(parameter1, parameter2):
    """
    This function takes two parameters and returns their product.

    Args:
        parameter1 (int): The first parameter.
        parameter2 (int): The second parameter.

    Returns:
        int: The product of the two parameters.
    """
    return parameter1 * parameter2

def count_quotient(parameter1, parameter2):
    """
    This function takes two parameters and returns their quotient.

    Args:
        parameter1 (int): The first parameter.
        parameter2 (int): The second parameter.

    Returns:
        float: The quotient of the two parameters.

    Raises:
        ZeroDivisionError: If the second parameter is zero.
    """
    if parameter2 == 0:
        raise ZeroDivisionError("division by zero is not allowed")
    return parameter1 / parameter2

def count_power(parameter1, parameter2):
    """
    This function takes two parameters and returns the first parameter raised to the power of the second parameter.

    Args:
        parameter1 (int): The base.
        parameter2 (int): The exponent.

    Returns:
        int: The result of raising the base to the power of the exponent.
    """
    return parameter1 ** parameter2

def count_square_root(parameter1, parameter2):
    """
    This function takes two parameters and returns the square root of each parameter.

    Args:
        parameter1 (int): The first parameter.
        parameter2 (int): The second parameter.

    Returns:
        tuple: A tuple containing the square root of each parameter.

    Raises:
        ValueError: If either parameter is negative.
    """
    if parameter1 < 0 or parameter2 < 0:
        raise ValueError("square root of negative number is not allowed")
    return parameter1 ** 0.5, parameter2 ** 0.5

def count_remainder(parameter1, parameter2):
    """
    This function takes two parameters and returns the remainder of dividing the first parameter by the second parameter.

    Args:
        parameter1 (int): The dividend.
        parameter2 (int): The divisor.

    Returns:
        int: The remainder of the division.

    Raises:
        ZeroDivisionError: If the second parameter is zero.
    """
    if parameter2 == 0:
        raise ZeroDivisionError("division by zero is not allowed")
    return parameter1 % parameter2
 
def make_calculations(parameter1, parameter2, operator):
    """
    This function takes two parameters and an operator, and performs the corresponding mathematical operation.

    Args:
        parameter1 (int): The first parameter.
        parameter2 (int): The second parameter.
        operator (str): The operator to perform the calculation.

    Returns:
        int or float: The result of the calculation.

    Raises:
        Exception: If an error occurs during the calculation.
    """
    try:
        match operator:
            case "+":            
                return count_sum(parameter1, parameter2)
            case "-":
                return count_difference(parameter1, parameter2)
            case "*":
                return count_product(parameter1, parameter2)
            case "/": 
                return count_quotient(parameter1, parameter2)
            case "**":
                return count_power(parameter1, parameter2)  
            case "//":
                return count_square_root(parameter1, parameter2)
            case "%":
                return count_remainder(parameter1, parameter2)
    except Exception as e:
        print(f'Error message: {e}')
        