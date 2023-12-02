from termcolor import colored

from UI.menu import Menu
from UI.menu_item import Item
from shared.file_handler import FileHandler
from .art_settings import ArtSettings
from .data_from_console import get_text_from_console, get_console_width
from .font import font_dict
from .settings import ART_PATH

class ArtGenerator:
    def __init__(self):
        self.text = None
        self.settings = ArtSettings()
        self.art = None

    def menu(self):
        art_menu = Menu("\nArt Menu")
        art_menu.add_item(Item('1', 'Set Art Text', self.set_text))
        art_menu.add_item(Item('2', 'Change Settings', self.change_settings))
        art_menu.add_item(Item('3', 'View Art', self.view_art))
        art_menu.add_item(Item('4', 'Save Art to File', self.save_art_to_file))
        art_menu.add_item(Item('5', 'View Saved Art', self.view_saved_art))
        art_menu.add_item(Item('0', 'Exit'))

        art_menu.run()

    def set_text(self):
        self.text = get_text_from_console()
        self.settings.size.set_chars(self._map_chars())

    def _map_chars(self):
        text = self.text.upper()
        chars = []
        for char in text:
            if char in font_dict:
                chars.append(font_dict[char])
            else:
                chars.append(" ")
        return chars
        
    def view_art(self):
        if self.text is None:
            self.set_text()

        self.set_art_settings()
        print()
        print(colored(self.art, self.settings.color))

    def set_art_settings(self):
        console_width = get_console_width()
        art_len = self.settings.size._width*(len(self.text) + 3)
        
        if art_len > console_width:
            print("Art is too big for console\nResizing...\n")
            self.settings.size.set_width(console_width//(len(self.text) + 3))
            self.settings.size.set_height(console_width//(len(self.text) + 3))
        
        chars = self.settings.size.get_chars()
        if self.settings.size._width > 5 or self.settings.size._height > 5:
            chars = self.settings.size.get_resized_chars()
        
        self.art = self._generate_art(chars)
        padding = self._get_padding()
        art_lines = self.art.split('\n')
        aligned_lines = [" " * padding + line for line in art_lines]
        self.art = '\n'.join(aligned_lines)

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
                art += "   "    
            art += "\n"
        return art

    def _get_padding(self):
        console_width = get_console_width()
        art_len = round(len(self.art)/self.settings.size._height)
        if self.settings.justify == "center":
            return (console_width - art_len) // 2
        elif self.settings.justify == "right":
            return console_width - art_len
        else:
            return 0

    def change_settings(self):
        self.settings.menu()

    def save_art_to_file(self):
        if self.art is None:
            print("No art to save")
            return
        saved_file = FileHandler(ART_PATH)
        saved_file.write_to_file(self.art)

    def view_saved_art(self):
        saved_file = FileHandler(ART_PATH)
        saved_file.read_from_file()
