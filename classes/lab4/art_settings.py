from UI.menu import Menu
from UI.menu_item import Item
from .art_size import ArtSize
from .data_from_console import *
from .settings import DEFAULT_SYMBOL, DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_JUSTIFY, DEFAULT_COLOR

class ArtSettings:
    def __init__(self, symbol=DEFAULT_SYMBOL, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, justify=DEFAULT_JUSTIFY, color=DEFAULT_COLOR):
        self._symbol = symbol
        self._size = ArtSize(width, height)
        self._justify = justify
        self._color = color

    def __str__(self):
        return f"Symbol: {self._symbol} \n{self._size} \nJustify: {self._justify} \nColor: {self._color}"

    def get_symbol(self):
        return self._symbol
    
    def get_size(self):
        return self._size
    
    def get_justify(self):
        return self._justify
    
    def get_color(self):
        return self._color
    
    def set_symbol(self, symbol):
        self._symbol = symbol

    def set_size(self, size):
        self._size = size

    def set_justify(self, justify):
        self._justify = justify

    def set_color(self, color):
        self._color = color

    def change_size(self):
        width, height = get_width_and_height_from_console()
        self._size.set_width(width)
        self._size.set_height(height)

    def change_symbol(self):
        self._symbol = get_symbol_from_console()
        
    def change_justify(self):
        self._justify = get_justify_from_console()

    def change_color(self):
        self._color = get_color_from_console()

    def view_settings(self):
        print(self.__str__())
    
    def menu(self):
        settings_menu = Menu("\nSettings Menu")
        settings_menu.add_item(Item('1', 'Change Symbol', self.change_symbol))
        settings_menu.add_item(Item('2', 'Change Size', self.change_size))
        settings_menu.add_item(Item('3', 'Change Justify', self.change_justify))
        settings_menu.add_item(Item('4', 'Change Color', self.change_color))
        settings_menu.add_item(Item('5', 'View Settings', self.view_settings))
        settings_menu.add_item(Item('0', 'Back'))

        settings_menu.run()
