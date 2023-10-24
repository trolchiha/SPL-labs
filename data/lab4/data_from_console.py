import termcolor
import curses

def get_console_width():
    stdscr = curses.initscr()
    rows, columns = stdscr.getmaxyx()
    curses.endwin()
    return columns

def get_size_from_console():
    width = int(input("Enter width (min 5): "))
    if width > get_console_width():
        print("Width is too big (min 5)")
        return get_size_from_console()
    
    height = int(input("Enter height: "))

    if width < 5 or height < 5:
        print("Width and height should be at least 5")
        return get_size_from_console()
    return width, height

def get_symbol_from_console():
    symbol = input("Enter symbol (e.g. '@', '#', '*'): ")
    if check_symbol(symbol):
        return symbol
    print("You should enter only one symbol")
    return get_color_from_console()

def check_symbol(symbol):
    if len(symbol) == 1:
        return True
    else:
        return False

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

def get_justify_from_console():
    justify = input("Enter justify (left, center, right): ")
    if check_justify(justify):
        return justify
    print("No such justify")
    return get_justify_from_console()

def check_justify(justify): 
    if justify in ['left', 'center', 'right']:
        return True
    else:
        return False