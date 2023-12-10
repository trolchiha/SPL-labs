"""
Module: data_from_console

This module contains functions that prompt the user to enter various parameters from the console.

Functions:
    - get_font_from_console(): Prompts the user to enter a font name from the available fonts.
    - get_width_from_console(): Prompts the user to enter the width.
    - get_symbol_from_console(): Prompts the user to enter a symbol.
    - get_color_from_console(): Prompts the user to enter a color name from the available colors.
    - get_text_from_console(): Prompts the user to enter a text.
"""
import pyfiglet
import termcolor
from shared.input_handler import InputHandler
from shared.settings import get_lab_settings

settings = get_lab_settings("lab3")
FIGLET_FONT_SIZES = settings["figlet_font_sizes"]

def get_font_from_console():
    """
    Prompts the user to enter a font name from the available fonts.

    Returns:
        str: The selected font name.
    """
    available_fonts = pyfiglet.FigletFont.getFonts()
    print("Font sizes: ", FIGLET_FONT_SIZES)
    font = InputHandler().get_one_of_list_input("Enter font name", available_fonts)
    return font

def get_width_from_console():
    """
    Prompts the user to enter the width.

    Returns:
        int: The entered width.
    """
    width = InputHandler().get_int_input("Enter width")
    return width

def get_symbol_from_console():
    """
    Prompts the user to enter a symbol.

    Returns:
        str: The entered symbol.
    """
    symbol = InputHandler().get_one_char_input("Enter symbol (e.g. '@', '#', '*')")
    return symbol

def get_color_from_console():
    """
    Prompts the user to enter a color name from the available colors.

    Returns:
        str: The selected color name.
    """
    color = InputHandler().get_one_of_list_input("Enter color name", termcolor.COLORS)
    return color

def get_text_from_console():
    """
    Prompts the user to enter a text.

    Returns:
        str: The entered text.
    """
    text = InputHandler().get_str_input("Enter text")
    return text
