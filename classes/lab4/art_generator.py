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
        self.__text = None
        self.__settings = ArtSettings()
        self.__art = None

    # def menu(self):
    #     art_menu = Menu("\nArt Menu")
    #     art_menu.add_item(Item('1', 'Set Art Text', self.set_text))
    #     art_menu.add_item(Item('2', 'Change Settings', self.change_settings))
    #     art_menu.add_item(Item('3', 'View Art', self.view_art))
    #     art_menu.add_item(Item('4', 'Save Art to File', self.save_art_to_file))
    #     art_menu.add_item(Item('5', 'View Saved Art', self.view_saved_art))
    #     art_menu.add_item(Item('0', 'Exit'))

    #     art_menu.run()

    def set_text(self):
        self.__text = get_text_from_console()
        self.__settings._size.set_chars(self.__map_chars())

    def get_text(self):
        return self.__text
    
    def set_settings(self, settings):
        self.__settings = settings

    def get_settings(self):
        return self.__settings
    
    def get_art(self):
        return self.__art

    def __map_chars(self):
        text = self.__text.upper()
        chars = []
        for char in text:
            if char in font_dict:
                chars.append(font_dict[char])
            else:
                chars.append(" ")
        return chars
        
    def view_art(self):
        if self.__text is None:
            self.set_text()

        self.set_art_settings()
        print()
        print(colored(self.__art, self.__settings._color))

    def set_art_settings(self):
        console_width = get_console_width()
        art_len = self.__settings._size.get_width()*(len(self.__text) + 3)
        
        if art_len > console_width:
            print("Art is too big for console\nResizing...\n")
            self.__settings._size.set_width(console_width//(len(self.__text) + 3))
            self.__settings._size.set_height(console_width//(len(self.__text) + 3))
        
        chars = self.__settings._size.get_chars()
        if self.__settings._size.get_width() > 5 or self.__settings._size.get_height() > 5:
            chars = self.__settings._size.get_resized_chars()
        
        self.__art = self.__generate_art(chars)
        padding = self.__get_padding()
        art_lines = self.__art.split('\n')
        aligned_lines = [" " * padding + line for line in art_lines]
        self.__art = '\n'.join(aligned_lines)

    def __generate_art(self, chars):
        height = len(chars[0])
        width = len(chars[0][0])
        art = ""
        for row in range(height):
            for char in chars:
                for column in range(width):
                    if char[row][column] == 1:
                        art += self.__settings._symbol
                    else:
                        art += " "
                art += "   "    
            art += "\n"
        return art

    def __get_padding(self):
        console_width = get_console_width()
        art_len = round(len(self.__art)/self.__settings._size.get_height())
        if self.__settings._justify == "center":
            return (console_width - art_len) // 2
        elif self.__settings._justify == "right":
            return console_width - art_len
        else:
            return 0

    def change_settings(self):
        self.__settings.menu()

    def save_art_to_file(self):
        if self.__art is None:
            print("No art to save")
            return
        saved_file = FileHandler(ART_PATH)
        saved_file.write_to_file(self.__art)

    def view_saved_art(self):
        saved_file = FileHandler(ART_PATH)
        saved_file.read_from_file()
