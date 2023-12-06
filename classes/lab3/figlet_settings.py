from UI.menu import Menu
from UI.menu_item import Item
from .data_from_console import get_font_from_console, get_width_from_console, get_symbol_from_console, get_color_from_console
from .settings import DEFAULT_FONT, DEFAULT_WIDTH, DEFAULT_COLOR

class FigletSettings():
    def __init__(self):
        self._font = DEFAULT_FONT
        self._width = DEFAULT_WIDTH
        self._symbol = None
        self._color = DEFAULT_COLOR

    def set_font(self, font):
        self._font = font

    def set_width(self, width):
        self._width = width

    def set_symbol(self, symbol):
        self._symbol = symbol

    def set_color(self, color):
        self._color = color

    def get_font(self):
        return self.font
    
    def get_width(self):
        return self.width
    
    def get_symbol(self):
        return self.symbol
    
    def get_color(self):
        return self.color

    def get_settings(self):
        settings = {
            "font": self._font,
            "width": self._width,
            "symbol": self._symbol,
            "color": self._color,
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
        self._font = new_font
        print("\nFont was changed to", self._font)

    def change_width(self):
        new_width = get_width_from_console()
        print(new_width)
        self._width = new_width
        print("\nWidth was changed to", self._width)

    def change_symbol(self):
        new_symbol = get_symbol_from_console()
        self._symbol = new_symbol
        print("\nSymbol was changed to", self._symbol)

    def change_color(self):
        new_color = get_color_from_console()
        self._color = new_color
        print("\nColor was changed to", self._color)
