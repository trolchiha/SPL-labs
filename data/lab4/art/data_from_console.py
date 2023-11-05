import termcolor
import curses

def get_console_width():
    stdscr = curses.initscr()
    rows, columns = stdscr.getmaxyx()
    curses.endwin()
    return columns


def get_text_from_console():
    text = input("Enter text: ")
    return text


def get_width_and_height_from_console():
    try:
        width = int(input("Enter width (min 5): "))
        height = int(input("Enter heigh (min 5): "))
    except ValueError:
        print("Not a Digit!\n")
        return get_width_and_height_from_console()

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
    symbol = input("Enter symbol (e.g. '@', '#', '*'): ")
    symbol = check_symbol(symbol)
    return symbol

def check_symbol(symbol):
    if len(symbol) == 1:
        return symbol
    else:
        print("You should enter only one symbol!\n")
        return get_symbol_from_console()


def get_color_from_console():
    color = input("Enter color name [ red, green, blue, yellow, white ]: ")
    color = check_color(color)
    return color

def check_color(color):
    if color in termcolor.COLORS:
        return color
    else:
        print("No such color!\n")
        return get_color_from_console()


def get_justify_from_console():
    justify = input("Enter justify (left, center, right): ")
    justify = check_justify(justify)
    return justify      

def check_justify(justify): 
    if justify in ['left', 'center', 'right']:
        return justify
    else:
        print("No such justify!\n")
        return get_justify_from_console()
    
def get_size_from_console():
    try:
        size = int(input("Enter size (min 5): "))
    except ValueError:
        print("Not a Digit!\n")
        return get_size_from_console()

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