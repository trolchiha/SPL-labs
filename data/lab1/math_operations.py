def count_sum(parameter1, parameter2):
    return parameter1 + parameter2

def count_difference(parameter1, parameter2):
    return parameter1 - parameter2

def count_product(parameter1, parameter2):
    return parameter1 * parameter2

def count_quotient(parameter1, parameter2):
    if parameter2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return parameter1 / parameter2

def count_power(parameter1, parameter2):
    return parameter1 ** parameter2

def count_square_root(parameter1, parameter2):
    if parameter1 < 0 or parameter2 < 0:
        raise ValueError("Square root of negative number is not allowed.")
    return parameter1 ** 0.5, parameter2 ** 0.5

def count_remainder(parameter1, parameter2):
    if parameter2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return parameter1 % parameter2
 
def make_calculations(parameter1, parameter2, operator):
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
        