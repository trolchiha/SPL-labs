"""
Console reader Module

This module provides functions for handling user input from the console.
"""
import curses
import termcolor
from shared.input_handler import InputHandler

def get_console_width():
    """
    Get the width of the console.

    Returns:
        int: The width of the console.
    """
    stdscr = curses.initscr()
    rows, columns = stdscr.getmaxyx()
    curses.endwin()
    return columns


def get_text_from_console():
    """
    Get text input from the console.

    Returns:
        str: The text entered by the user.
    """
    text = InputHandler().get_str_input("Enter text")
    return text

def get_width_and_height_from_console():
    """
    Get width and height input from the console.

    Returns:
        tuple: A tuple containing the width and height entered by the user.
    """
    width = InputHandler().get_int_input("Enter width (min 5)")
    height = InputHandler().get_int_input("Enter height(min 5)")
    width, height = check_width_and_height(width, height)
    return width, height

def check_width_and_height(width, height):
    """
    Check if the width and height are valid.

    Args:
        width (int): The width entered by the user.
        height (int): The height entered by the user.

    Returns:
        tuple: A tuple containing the valid width and height.
    """
    if width > get_console_width():
        print("Width is too big (min 5)!\n")
        return get_width_and_height_from_console()
    if width < 5 or height < 5:
        print("Width and height should be at least 5!\n")
        return get_width_and_height_from_console()
    return width, height

def get_symbol_from_console():
    """
    Get a symbol input from the console.

    Returns:
        str: The symbol entered by the user.
    """
    symbol = InputHandler().get_one_char_input("Enter one symbol (e.g. '@', '#', '*')")
    return symbol

def get_color_from_console():
    """
    Get a color input from the console.

    Returns:
        str: The color entered by the user.
    """
    color = InputHandler().get_one_of_list_input("Enter color name [ red, green, blue, yellow, white ]", termcolor.COLORS)
    return color

def get_justify_from_console():
    """
    Get a justify input from the console.

    Returns:
        str: The justify entered by the user.
    """
    justify_list = ["left", "center", "right"]
    justify = InputHandler().get_one_of_list_input("Enter justify (left, center, right)" , justify_list)
    return justify      
    
def get_size_from_console():
    """
    Get a size input from the console.

    Returns:
        int: The size entered by the user.
    """
    size = InputHandler().get_int_input("Enter size (min 6)")
    size = check_size(size)
    return size

def check_size(size):
    """
    Check if the size is valid.

    Args:
        size (int): The size entered by the user.

    Returns:
        int: The valid size.
    """
    if size > get_console_width():
        print("Size is too big (min 6)!\n")
        return get_size_from_console()
    if size < 6:
        print("Size should be at least 6!\n")
        return get_size_from_console()
    return size
    