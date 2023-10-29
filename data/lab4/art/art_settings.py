import sys
from vars import home_path 
sys.path.append(home_path)

from UI.menu import Menu
from UI.menu_item import Item
from data.lab4.art.art_size import ArtSize
from data.lab4.art.data_from_console import *

class ArtSettings:
    def __init__(self, symbol="#", width=5, height=5, justify="left", color="white"):
        self.symbol = symbol
        self.size = ArtSize(width, height)
        self.justify = justify
        self.color = color

    def __str__(self):
        return f"Symbol: {self.symbol} \n{self.size} \nJustify: {self.justify} \nColor: {self.color}"

    def change_size(self):
        width, height = get_size_from_console()
        self.size.set_width(width)
        self.size.set_height(height)

    def change_symbol(self):
        self.symbol = get_symbol_from_console()
        
    def change_justify(self):
        self.justify = get_justify_from_console()

    def change_color(self):
        self.color = get_color_from_console()

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
