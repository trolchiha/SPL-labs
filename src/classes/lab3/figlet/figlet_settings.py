"""
A module that defines the FigletSettings class representing the settings for a Figlet program.
"""
from UI.menu import Menu
from UI.menu_item import Item
from classes.lab3.console_reader.data_from_console import get_font_from_console, get_width_from_console, get_symbol_from_console, get_color_from_console
from shared.settings import get_lab_settings

settings = get_lab_settings("lab3")
DEFAULT_FIGLET_SETTINGS = settings["default_figlet_settings"]
DEFAULT_FONT = DEFAULT_FIGLET_SETTINGS["font"]
DEFAULT_WIDTH = DEFAULT_FIGLET_SETTINGS["width"]
DEFAULT_COLOR = DEFAULT_FIGLET_SETTINGS["color"]

class FigletSettings():
    """
    Class representing the settings for a Figlet program.
    """

    def __init__(self):
        """
        Initialize the FigletSettings object with default settings.
        """
        self._font = DEFAULT_FONT
        self._width = DEFAULT_WIDTH
        self._symbol = None
        self._color = DEFAULT_COLOR

    def set_font(self, font):
        """
        Set the font for the Figlet program.

        Args:
            font (str): The font to set.
        """
        self._font = font

    def set_width(self, width):
        """
        Set the width for the Figlet program.

        Args:
            width (int): The width to set.
        """
        self._width = width

    def set_symbol(self, symbol):
        """
        Set the symbol for the Figlet program.

        Args:
            symbol (str): The symbol to set.
        """
        self._symbol = symbol

    def set_color(self, color):
        """
        Set the color for the Figlet program.

        Args:
            color (str): The color to set.
        """
        self._color = color

    def get_font(self):
        """
        Get the current font for the Figlet program.

        Returns:
            str: The current font.
        """
        return self._font
    
    def get_width(self):
        """
        Get the current width for the Figlet program.

        Returns:
            int: The current width.
        """
        return self._width
    
    def get_symbol(self):
        """
        Get the current symbol for the Figlet program.

        Returns:
            str: The current symbol.
        """
        return self._symbol
    
    def get_color(self):
        """
        Get the current color for the Figlet program.

        Returns:
            str: The current color.
        """
        return self._color

    def get_settings(self):
        """
        Get the current settings for the Figlet program.

        Returns:
            dict: A dictionary containing the current settings.
        """
        figlet_settings = {
            "font": self._font,
            "width": self._width,
            "symbol": self._symbol,
            "color": self._color,
        }
        return figlet_settings
    
    def print_settings(self):
        """
        Print the current settings for the Figlet program.
        """
        print("\nSettings:")
        for key, value in self.get_settings().items():
            print(f"{key}: {value}")

    def settings_menu(self):
        """
        Display the settings menu for the Figlet program.
        """
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
        """
        Change the font for the Figlet program.
        """
        new_font = get_font_from_console()
        self._font = new_font
        print("\nFont was changed to", self._font)

    def change_width(self):
        """
        Change the width for the Figlet program.
        """
        new_width = get_width_from_console()
        print(new_width)
        self._width = new_width
        print("\nWidth was changed to", self._width)

    def change_symbol(self):
        """
        Change the symbol for the Figlet program.
        """
        new_symbol = get_symbol_from_console()
        self._symbol = new_symbol
        print("\nSymbol was changed to", self._symbol)

    def change_color(self):
        """
        Change the color for the Figlet program.
        """
        new_color = get_color_from_console()
        self._color = new_color
        print("\nColor was changed to", self._color)
