"""
ArtSettings Module

This module defines the ArtSettings class, which represents the settings for creating art. 
It includes methods for initializing settings, getting and setting individual settings, 
changing settings interactively through the console, and viewing the current settings.

Classes:
    ArtSettings: Represents the settings for creating art.

Usage:
    Import this module and create an instance of the ArtSettings class to manage art creation settings. 
    The class provides methods for interacting with and modifying various settings.

Example:
    # Import the module
    from your_module_name import ArtSettings

    # Create an instance of ArtSettings
    art_settings = ArtSettings()

    # Use methods to modify and interact with settings
    art_settings.change_symbol()
    art_settings.change_size()
    art_settings.view_settings()
    art_settings.menu()
"""
from UI.menu import Menu
from UI.menu_item import Item
from shared.settings import get_lab_settings
from classes.lab4.art_settings.art_size import ArtSize
from classes.lab4.console_reader.data_from_console import get_width_and_height_from_console, get_symbol_from_console, get_justify_from_console, get_color_from_console

settings = get_lab_settings("lab4")
DEFAULT_ART_SETTINGS = settings["default_art_settings"]
DEFAULT_WIDTH = DEFAULT_ART_SETTINGS["width"]
DEFAULT_HEIGHT = DEFAULT_ART_SETTINGS["height"]
DEFAULT_JUSTIFY = DEFAULT_ART_SETTINGS["justify"]
DEFAULT_COLOR = DEFAULT_ART_SETTINGS["color"]
DEFAULT_SYMBOL = DEFAULT_ART_SETTINGS["symbol"]

class ArtSettings:
    """
    Represents the settings for creating art.

    Attributes:
        _symbol (str): The symbol used for the art.
        _size (ArtSize): The size of the art.
        _justify (str): The justification of the art.
        _color (str): The color of the art.
    """

    def __init__(self, symbol=DEFAULT_SYMBOL, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, justify=DEFAULT_JUSTIFY, color=DEFAULT_COLOR):
        """
        Initialize the ArtSettings object.

        Args:
            symbol (str): The symbol used for the art.
            width (int): The width of the art.
            height (int): The height of the art.
            justify (str): The justification of the art.
            color (str): The color of the art.
        """
        self._symbol = symbol
        self._size = ArtSize(width, height)
        self._justify = justify
        self._color = color

    def __str__(self):
        """
        Return a string representation of the ArtSettings object.

        Returns:
            str: The string representation of the ArtSettings object.
        """
        return f"Symbol: {self._symbol} \n{self._size} \nJustify: {self._justify} \nColor: {self._color}"

    def get_symbol(self):
        """
        Get the symbol used for the art.

        Returns:
            str: The symbol used for the art.
        """
        return self._symbol
    
    def get_size(self):
        """
        Get the size of the art.

        Returns:
            ArtSize: The size of the art.
        """
        return self._size
    
    def get_justify(self):
        """
        Get the justification of the art.

        Returns:
            str: The justification of the art.
        """
        return self._justify
    
    def get_color(self):
        """
        Get the color of the art.

        Returns:
            str: The color of the art.
        """
        return self._color
    
    def set_symbol(self, symbol):
        """
        Set the symbol used for the art.

        Args:
            symbol (str): The symbol used for the art.
        """
        self._symbol = symbol

    def set_size(self, size):
        """
        Set the size of the art.

        Args:
            size (ArtSize): The size of the art.
        """
        self._size = size

    def set_justify(self, justify):
        """
        Set the justification of the art.

        Args:
            justify (str): The justification of the art.
        """
        self._justify = justify

    def set_color(self, color):
        """
        Set the color of the art.

        Args:
            color (str): The color of the art.
        """
        self._color = color

    def change_size(self):
        """
        Change the size of the art by getting the width and height from the console.
        """
        width, height = get_width_and_height_from_console()
        self._size.set_width(width)
        self._size.set_height(height)

    def change_symbol(self):
        """
        Change the symbol used for the art by getting it from the console.
        """
        self._symbol = get_symbol_from_console()
        
    def change_justify(self):
        """
        Change the justification of the art by getting it from the console.
        """
        self._justify = get_justify_from_console()

    def change_color(self):
        """
        Change the color of the art by getting it from the console.
        """
        self._color = get_color_from_console()

    def view_settings(self):
        """
        Print the current settings of the art.
        """
        print(str(self))
    
    def menu(self):
        """
        Create and run the settings menu.
        """
        settings_menu = Menu("\nSettings Menu")
        settings_menu.add_item(Item('1', 'Change Symbol', self.change_symbol))
        settings_menu.add_item(Item('2', 'Change Size', self.change_size))
        settings_menu.add_item(Item('3', 'Change Justify', self.change_justify))
        settings_menu.add_item(Item('4', 'Change Color', self.change_color))
        settings_menu.add_item(Item('5', 'View Settings', self.view_settings))
        settings_menu.add_item(Item('0', 'Back'))

        settings_menu.run()
