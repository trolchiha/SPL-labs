from vars import figlet_fonts, figlet_colors
import pyfiglet
import termcolor

available_fonts = pyfiglet.FigletFont.getFonts()

def get_font_from_console():
    font = input("Enter font name: ")
    if check_font(font):
        return font
    print("No such font")
    return get_font_from_console()

def check_font(font):  
    if font in available_fonts:
        return True
    else:
        return False

def get_width_from_console():
    width = int(input("Enter width: "))
    return width

def get_symbol_from_console():
    symbol = input("Enter symbol (e.g. '@', '#', '*'): ")
    return symbol

def get_color_from_console():
    color = input("Enter color name: ")
    if check_color(color):
        return color
    print("No such color")
    return get_color_from_console()

def check_color(color):
    if color in termcolor.COLORS:
        return True
    else:
        return False

def get_text_from_console():
    text = input("Enter text: ")
    return text