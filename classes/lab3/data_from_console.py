import pyfiglet
import termcolor
from shared.input_handler import InputHandler
from .settings import FIGLET_FONT_SIZES

def get_font_from_console():
    available_fonts = pyfiglet.FigletFont.getFonts()
    print("Font sizes: ", FIGLET_FONT_SIZES)
    font = InputHandler().get_one_of_list_input("Enter font name", available_fonts)
    return font

def get_width_from_console():
    width = InputHandler().get_int_input("Enter width")
    return width

def get_symbol_from_console():
    symbol = InputHandler().get_one_char_input("Enter symbol (e.g. '@', '#', '*')")
    return symbol

def get_color_from_console():
    color = InputHandler().get_one_of_list_input("Enter color name", termcolor.COLORS)
    return color

def get_text_from_console():
    text = InputHandler().get_str_input("Enter text")
    return text
