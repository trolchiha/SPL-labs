import termcolor
import curses
from shared.input_handler import InputHandler

def get_console_width():
    stdscr = curses.initscr()
    rows, columns = stdscr.getmaxyx()
    curses.endwin()
    return columns


def get_text_from_console():
    text = InputHandler().get_str_input("Enter text")
    return text

def get_width_and_height_from_console():
    width = InputHandler().get_int_input("Enter width (min 5)")
    height = InputHandler().get_int_input("Enter height(min 5)")
    width, height = check_width_and_height(width, height)
    return width, height

def check_width_and_height(width, height):
    if width > get_console_width():
            print("Width is too big (min 5)!\n")
            return get_width_and_height_from_console()
    elif width < 5 or height < 5:
            print("Width and height should be at least 5!\n")
            return get_width_and_height_from_console()
    else:
        return width, height

def get_symbol_from_console():
    symbol = InputHandler().get_one_char_input("Enter one symbol (e.g. '@', '#', '*')")
    return symbol

def get_color_from_console():
    color = InputHandler().get_one_of_list_input("Enter color name [ red, green, blue, yellow, white ]", termcolor.COLORS)
    return color

def get_justify_from_console():
    justify_list = ["left", "center", "right"]
    justify = InputHandler().get_one_of_list_input("Enter justify (left, center, right)" , justify_list)
    return justify      
    
def get_size_from_console():
    size = InputHandler().get_int_input("Enter size (min 6)")
    size = check_size(size)
    return size

def check_size(size):
    if size > get_console_width():
            print("Size is too big (min 6)!\n")
            return get_size_from_console()
    elif size < 6:
            print("Size should be at least 6!\n")
            return get_size_from_console()
    else:
        return size
    