import sys

from vars import home_path
sys.path.append(home_path)

from UI.menu import Menu
from UI.menu_item import Item
from data.lab4.art.data_from_console import get_size_from_console, get_color_from_console, get_justify_from_console


class ArtSettings:
    def __init__(self, size=5, justify="left", color="white"):
        self.__size = size
        self.__justify = justify
        self.__color = color

    def __str__(self):
       return f"Size: {self.__size}\nColor: {self.__color}\nJustify: {self.__justify}"
   
    def settings_menu(self):
        settings_menu = Menu("\nSettings Menu")
        settings_menu.add_item(Item('1', 'Change Size', self.change_size))
        settings_menu.add_item(Item('2', 'Change Color', self.change_color))
        settings_menu.add_item(Item('3', 'Change Justify', self.change_justify))
        settings_menu.add_item(Item('4', 'View Settings', self.print_settings))
        settings_menu.add_item(Item('0', 'Back'))

        settings_menu.run()
    
    def change_size(self):
        self.__size = get_size_from_console()
   
    def change_color(self):
        self.__color = get_color_from_console()

    def change_justify(self):
        self.__justify = get_justify_from_console()

    def set_size(self, size):
        self.__size = size

    def set_color(self, color):
        self.__color = color

    def set_justify(self, justify):
        self.__justify = justify

    def get_size(self):
        return self.__size
    
    def get_color(self):
        return self.__color
    
    def get_justify(self):
        return self.__justify
    
    def get_settings_obj(self):
        return self
    
    def print_settings(self):
        print(self.__str__())
