"""
A module that defines the ArtSettings class representing the settings for creating art.
"""
from UI.menu import Menu
from UI.menu_item import Item
from classes.lab4.console_reader.data_from_console import get_size_from_console, get_color_from_console, get_justify_from_console

class ArtSettings:
    """
    A class that represents the settings for creating art.

    Attributes:
        __size (int): The size of the art.
        __justify (str): The justification of the art.
        __color (str): The color of the art.

    Methods:
        __init__(self, size=5, justify="left", color="white"): Initializes a new instance of the ArtSettings class.
        __str__(self): Returns a string representation of the ArtSettings object.
        settings_menu(self): Displays the settings menu.
        change_size(self): Changes the size of the art.
        change_color(self): Changes the color of the art.
        change_justify(self): Changes the justification of the art.
        set_size(self, size): Sets the size of the art.
        set_color(self, color): Sets the color of the art.
        set_justify(self, justify): Sets the justification of the art.
        get_size(self): Returns the size of the art.
        get_color(self): Returns the color of the art.
        get_justify(self): Returns the justification of the art.
        get_settings_obj(self): Returns the ArtSettings object.
        print_settings(self): Prints the current settings of the art.
    """
    def __init__(self, size=5, justify="left", color="white"):
        self.__size = size
        self.__justify = justify
        self.__color = color

    def __str__(self):
        return f"Size: {self.__size}\nColor: {self.__color}\nJustify: {self.__justify}"
   
    def settings_menu(self):
        """
        Displays the settings menu.
        """
        settings_menu = Menu("\nSettings Menu")
        settings_menu.add_item(Item('1', 'Change Size', self.change_size))
        settings_menu.add_item(Item('2', 'Change Color', self.change_color))
        settings_menu.add_item(Item('3', 'Change Justify', self.change_justify))
        settings_menu.add_item(Item('4', 'View Settings', self.print_settings))
        settings_menu.add_item(Item('0', 'Back'))

        settings_menu.run()
    
    def change_size(self):
        """
        Changes the size of the art.
        """
        self.__size = get_size_from_console()
   
    def change_color(self):
        """
        Changes the color of the art.
        """
        self.__color = get_color_from_console()

    def change_justify(self):
        """
        Changes the justification of the art.
        """
        self.__justify = get_justify_from_console()

    def set_size(self, size):
        """
        Sets the size of the art.

        Parameters:
            size (int): The size of the art.
        """
        self.__size = size

    def set_color(self, color):
        """
        Sets the color of the art.

        Parameters:
            color (str): The color of the art.
        """
        self.__color = color

    def set_justify(self, justify):
        """
        Sets the justification of the art.

        Parameters:
            justify (str): The justification of the art.
        """
        self.__justify = justify

    def get_size(self):
        """
        Returns the size of the art.

        Returns:
            int: The size of the art.
        """
        return self.__size
    
    def get_color(self):
        """
        Returns the color of the art.

        Returns:
            str: The color of the art.
        """
        return self.__color
    
    def get_justify(self):
        """
        Returns the justification of the art.

        Returns:
            str: The justification of the art.
        """
        return self.__justify
    
    def get_settings_obj(self):
        """
        Returns the ArtSettings object.

        Returns:
            ArtSettings: The ArtSettings object.
        """
        return self
    
    def print_settings(self):
        """
        Prints the current settings of the art.
        """
        print(str(self))
