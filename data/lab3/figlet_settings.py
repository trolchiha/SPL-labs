import sys
from vars import home_path 
sys.path.append(home_path)

from UI.menu import Menu
from UI.menu_item import Item
from data_from_console import get_font_from_console, get_width_from_console, get_symbol_from_console, get_color_from_console

class FigletSettings():
    def __init__(self):
        self.font = 'standard'
        self.width = 80
        self.symbol = None
        self.color = None

    def set_font(self, font):
        self.font = font

    def set_width(self, width):
        self.size = width

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_color(self, color):
        self.color = color

    def get_settings(self):
        settings = {
            "font": self.font,
            "width": self.width,
            "symbol": self.symbol,
            "color": self.color,
        }
        return settings
    
    def print_settings(self):
        print("\nSettings:")
        for key, value in self.get_settings().items():
            print(f"{key}: {value}")

    def settings_menu(self):
        settings_menu = Menu("\nSettings Menu")
        settings_menu.set_color('grey')
        settings_menu.add_item(Item('1', 'View Settings', self.print_settings))
        settings_menu.add_item(Item('2', 'Change Font', self.change_font))
        settings_menu.add_item(Item('3', 'Change Width', self.change_width))
        settings_menu.add_item(Item('4', 'Change Symbol', self.change_symbol))
        settings_menu.add_item(Item('5', 'Change Color', self.change_color))
        settings_menu.add_item(Item('0', 'Back'))

        settings_menu.run()

    def change_font(self):
        new_font = get_font_from_console()
        self.set_font(new_font)
        print("\nFont was changed to", self.font)

    def change_width(self):
        new_width = get_width_from_console()
        self.set_width(new_width)
        print("\nWidth was changed to", self.width)


    def change_symbol(self):
        new_symbol = get_symbol_from_console()
        self.set_symbol(new_symbol)
        print("\nSymbol was changed to", self.symbol)

    def change_color(self):
        new_color = get_color_from_console()
        self.set_color(new_color)
        print("\nColor was changed to", self.color)
