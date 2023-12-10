"""
ArtGenerator Module

This module defines the ArtGenerator class, which generates ASCII 
art based on user input and settings. It includes methods for setting text, 
changing settings, viewing and saving generated art, and viewing saved art from a file.

Classes:
    ArtGenerator: A class that generates ASCII art based on user input and settings.

Usage:
    Import this module and create an instance of the ArtGenerator class to generate 
    ASCII art based on user input and settings. The class provides methods for interacting 
    with and modifying text, settings, and the generated art.

Example:
    # Import the module
    from your_module_name import ArtGenerator

    # Create an instance of ArtGenerator
    art_generator = ArtGenerator()

    # Use methods to generate art and interact with settings
    art_generator.set_text()
    art_generator.change_settings()
    art_generator.view_art()
    art_generator.save_art_to_file()
    art_generator.view_saved_art()
"""

from termcolor import colored
from classes.lab4.art_settings.art_settings import ArtSettings
from classes.lab4.console_reader.data_from_console import get_text_from_console, get_console_width
from classes.lab4.font.font import font_dict
from shared.file_handler import FileHandler
from shared.settings import get_lab_settings

settings = get_lab_settings("lab4")
ART_PATH = settings["art_path"]

class ArtGenerator:
    """
    A class that generates ASCII art based on user input and settings.

    Attributes:
    - __text: The text used to generate the art.
    - __settings: The settings for generating the art.
    - __art: The generated ASCII art.

    Methods:
    - set_text(): Sets the text used to generate the art.
    - get_text(): Returns the text used to generate the art.
    - set_settings(settings): Sets the settings for generating the art.
    - get_settings(): Returns the settings for generating the art.
    - get_art(): Returns the generated ASCII art.
    - view_art(): Displays the generated ASCII art.
    - set_art_settings(): Sets the settings for generating the art.
    - __map_chars(): Maps the characters in the text to the corresponding ASCII art characters.
    - __generate_art(chars): Generates the ASCII art based on the mapped characters.
    - __get_padding(): Calculates the padding for aligning the art.
    - change_settings(): Allows the user to change the settings for generating the art.
    - save_art_to_file(): Saves the generated ASCII art to a file.
    - view_saved_art(): Displays the saved ASCII art from a file.
    """
    def __init__(self):
        self.__text = None
        self.__settings = ArtSettings()
        self.__art = None

    def set_text(self):
        """
        Sets the text used to generate the art.
        """
        self.__text = get_text_from_console()
        self.__settings.get_size().set_chars(self.__map_chars())

    def get_text(self):
        """
        Returns the text used to generate the art.
        """
        return self.__text
    
    def set_settings(self, art_settings):
        """
        Sets the settings for generating the art.

        Parameters:
        - settings: The settings object.
        """
        self.__settings = art_settings

    def get_settings(self):
        """
        Returns the settings for generating the art.
        """
        return self.__settings
    
    def get_art(self):
        """
        Returns the generated ASCII art.
        """
        return self.__art

    def __map_chars(self):
        """
        Maps the characters in the text to the corresponding ASCII art characters.
        """
        text = self.__text.upper()
        chars = []
        for char in text:
            if char in font_dict:
                chars.append(font_dict[char])
            else:
                chars.append(" ")
        return chars
        
    def view_art(self):
        """
        Displays the generated ASCII art.
        """
        if self.__text is None:
            self.set_text()

        self.set_art_settings()
        print()
        print(colored(self.__art, self.__settings.get_color()))

    def set_art_settings(self):
        """
        Sets the settings for generating the art.
        """
        console_width = get_console_width()
        art_len = self.__settings.get_size().get_width()*(len(self.__text) + 3)
        
        if art_len > console_width:
            print("Art is too big for console\nResizing...\n")
            self.__settings.get_size().set_width(console_width//(len(self.__text) + 3))
            self.__settings.get_size().set_height(console_width//(len(self.__text) + 3))
        
        chars = self.__settings.get_size().get_chars()
        if self.__settings.get_size().get_width() > 5 or self.__settings.get_size().get_height() > 5:
            chars = self.__settings.get_size().get_resized_chars()
        
        self.__art = self.__generate_art(chars)
        padding = self.__get_padding()
        art_lines = self.__art.split('\n')
        aligned_lines = [" " * padding + line for line in art_lines]
        self.__art = '\n'.join(aligned_lines)

    def __generate_art(self, chars):
        """
        Generates the ASCII art based on the mapped characters.

        Parameters:
        - chars: The mapped characters.

        Returns:
        - The generated ASCII art.
        """
        height = len(chars[0])
        width = len(chars[0][0])
        art = ""
        for row in range(height):
            for char in chars:
                for column in range(width):
                    if char[row][column] == 1:
                        art += self.__settings.get_symbol()
                    else:
                        art += " "
                art += "   "    
            art += "\n"
        return art

    def __get_padding(self):
        """
        Calculates the padding for aligning the art.

        Returns:
        - The padding value.
        """
        console_width = get_console_width()
        art_len = round(len(self.__art)/self.__settings.get_size().get_height())
        if self.__settings.get_justify() == "center":
            return (console_width - art_len) // 2
        if self.__settings.get_justify() == "right":
            return console_width - art_len
        return 0

    def change_settings(self):
        """
        Allows the user to change the settings for generating the art.
        """
        self.__settings.menu()

    def save_art_to_file(self):
        """
        Saves the generated ASCII art to a file.
        """
        if self.__art is None:
            print("No art to save")
            return
        saved_file = FileHandler(ART_PATH)
        saved_file.write_to_file(self.__art)

    def view_saved_art(self):
        """
        Displays the saved ASCII art from a file.
        """
        saved_file = FileHandler(ART_PATH)
        saved_file.read_from_file()
