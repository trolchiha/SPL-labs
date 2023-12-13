"""
Input Handling Module

This module provides functions for getting user input related to object names, colors, and recommendations.
"""
import re
from shared.input_handler import InputHandler

def get_name(obj):
    """
    Get the name of an object from the user.

    Parameters:
    obj (str): The name of the object.

    Returns:
    str: The name entered by the user.
    """
    obj = InputHandler().get_str_input(f"Enter {obj} name")
    return obj

def get_color():
    """
    Get a color from the user.

    Returns:
    str: The color entered by the user.
    """
    list_of_colors = ['RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']
    print("Available colors: red, green, yellow, blue, magenta, cyan, white")
    input_color = InputHandler().get_one_of_list_input_ignore_case("Enter color", list_of_colors)
    color_name = input_color.upper() 
    return color_name

def get_user_input_recommendations():
    """
    Get user input for recommendations.

    Returns:
    dict: A dictionary containing user input for genre, artist, and track recommendations.
    """
    user_input = InputHandler().get_str_input("Enter parameters for recommendations\ne.g. genre=pop, rock; track=blinding lights; artist=the weeknd, metallica\n")
    pattern = re.compile(r'\b(genre|artist|track)\s*=\s*([^;]+)(?:;|$)')

    user_recommendations = {'genre': [], 'artist': [], 'track': []}

    matches = pattern.finditer(user_input)

    if not matches:
        print("No matches")
        return None

    for match in matches:
        category, values = match.groups()
        user_recommendations[category].extend([value.strip() for value in values.split(',')])

    return user_recommendations
