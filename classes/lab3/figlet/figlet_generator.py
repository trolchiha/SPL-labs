"""
Module: figlet_generator

This module contains the FigletGenerator class that generates figlet art based on provided text and settings.
"""
from pyfiglet import Figlet
from termcolor import colored
from UI.menu import Menu
from UI.menu_item import Item
from shared.settings import get_lab_settings
from shared.file_handler import FileHandler
from classes.lab3.figlet.figlet_settings import FigletSettings
from classes.lab3.console_reader.data_from_console import get_text_from_console

settings = get_lab_settings("lab3")
ART_PATH = settings["art_path"]

class FigletGenerator:
    """
    A class that generates figlet art based on the provided text and settings.
    """

    def __init__(self, text=None):
        """
        Initialize the FigletGenerator object.

        Args:
        - text: The text to generate art from (default: None)
        """
        self.__text = text
        self.__settings = FigletSettings()
        self.__figlet = None

    def menu(self):
            main_menu = Menu("\nMenu")
            main_menu.add_item(Item('1', 'Generate art', self.generate_art))
            main_menu.add_item(Item('2', 'Change settings', self.change_settings))
            main_menu.add_item(Item('3', 'Preview', self.view_art ))
            main_menu.add_item(Item('4', 'Save art', self.save_art))
            main_menu.add_item(Item('5', 'View saved art', self.view_saved_art))
            main_menu.add_item(Item('0', 'Exit'))
            
            main_menu.run()

    def get_text(self):
        """
        Get the current text.

        Returns:
        - The current text.
        """
        return self.__text
    
    def get_settings(self):
        """
        Get the current settings.

        Returns:
        - The current settings.
        """
        return self.__settings
    
    def get_figlet(self):
        """
        Get the current figlet art.

        Returns:
        - The current figlet art.
        """
        return self.__figlet
    
    def set_text(self, text):
        """
        Set the text.

        Args:
        - text: The text to set.
        """
        self.__text = text

    def set_settings(self, figlet_settings):
        """
        Set the settings.

        Args:
        - settings: The settings to set.
        """
        self.__settings = figlet_settings

    def set_figlet(self, figlet):
        """
        Set the figlet art.

        Args:
        - figlet: The figlet art to set.
        """
        self.__figlet = figlet

    def generate_art(self):
        """
        Generate the figlet art based on the current text and settings.
        """
        self.__text = get_text_from_console()
        self.__figlet = Figlet(font=self.__settings.get_font(), width=self.__settings.get_width())
        self.__figlet = self.__figlet.renderText(self.__text)

        if self.__settings.get_symbol() is not None:
            self.modify_symbols(self.__settings.get_symbol())

        print("\nArt is generated!")

    def modify_symbols(self, symbol):
        """
        Modify the symbols in the figlet art.

        Args:
        - symbol: The symbol to replace the existing symbols with.
        """
        for char in self.__figlet:
            if char != '\n' and char != ' ':
                self.__figlet = self.__figlet.replace(char, symbol)

    def change_settings(self):
        """
        Change the settings for generating the figlet art.
        """
        self.__settings.settings_menu()
          
    def view_art(self):
        """
        View the generated figlet art.
        """
        if self.__figlet is None:
            print("No art to preview")
        else:
            print(colored(self.__figlet, self.__settings.get_color()))

    def save_art(self):
        """
        Save the generated figlet art to a file.
        """
        if self.__figlet is None:
            print("No art to save")
            return
        saved_file = FileHandler(ART_PATH)
        saved_file.write_to_file(self.__figlet)

    def view_saved_art(self):
        """
        View the saved figlet art from a file.
        """
        saved_file = FileHandler(ART_PATH)
        saved_file.read_from_file()
