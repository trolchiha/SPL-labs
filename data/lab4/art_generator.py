import sys

from termcolor import colored
from vars import home_path, art_path
sys.path.append(home_path)

from UI.menu import Menu
from UI.menu_item import Item
from art_settings import ArtSettings
from shared.file_handler import FileHandler
from data_from_console import get_text_from_console

from font import font_dict

class ArtGenerator:
    def __init__(self):
        self.text = None
        self.settings = ArtSettings()
        self.art = None

    def menu(self):
        art_menu = Menu("\nArt Menu")
        art_menu.set_color('grey')
        art_menu.add_item(Item('1', 'Create Art', self.create_art))
        art_menu.add_item(Item('2', 'Change Art Text', self.set_text))
        art_menu.add_item(Item('3', 'Change Settings', self.change_settings))
        art_menu.add_item(Item('4', 'View Art', self.view_art))
        art_menu.add_item(Item('5', 'Save Art to File', self.save_art_to_file))
        art_menu.add_item(Item('6', 'View Saved Art', self.view_saved_art))
        art_menu.add_item(Item('0', 'Back'))

        art_menu.run()

    def create_art(self):
        if self.text is None:
            self.set_text()
        resized_chars = self.settings.size.get_resized_chars()
        self.art = self._generate_art(resized_chars)

        print("\nArt created!\n")
        self.view_art()
        
    def _map_chars(self):
        text = self.text.upper()
        chars = []
        for char in text:
            if char in font_dict:
                chars.append(font_dict[char])
            else:
                chars.append(" ")
        return chars
    
    def _generate_art(self, chars):
        height = len(chars[0])
        width = len(chars[0][0])
        art = ""
        for row in range(height):
            for char in chars:
                for column in range(width):
                    if char[row][column] == 1:
                        art += self.settings.symbol
                    else:
                        art += " "
                art += "\t"    
            art += "\n"
        return art
    
    def set_text(self):
        self.text = get_text_from_console()
        self.settings.size.set_chars(self._map_chars())
    
    def view_art(self):
        if self.art is None:
            print("No art to view")
            return
        print()
        print(colored(self.art, self.settings.color))

    def change_settings(self):
        self.settings.menu()

    def save_art_to_file(self):
        if self.art is None:
            print("No art to save")
            return
        saved_file = FileHandler(art_path)
        saved_file.write_to_file(self.art)

    def view_saved_art(self):
        saved_file = FileHandler(art_path)
        saved_file.read_from_file()
