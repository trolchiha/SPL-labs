from pyfiglet import Figlet
from termcolor import colored

from UI.menu import Menu
from UI.menu_item import Item
from shared.file_handler import FileHandler
from .data_from_console import get_text_from_console
from .figlet_settings import FigletSettings

from .settings import ART_PATH

class FigletGenerator:
    def __init__(self, text=None):
        self.__text = text
        self.__settings = FigletSettings()
        self.__figlet = None

    # def menu(self):
    #     main_menu = Menu("\nMenu")
    #     main_menu.set_color('grey')
    #     main_menu.add_item(Item('1', 'Generate art', self.generate_art))
    #     main_menu.add_item(Item('2', 'Change settings', self.change_settings))
    #     main_menu.add_item(Item('3', 'Preview', self.view_art ))
    #     main_menu.add_item(Item('4', 'Save art', self.save_art))
    #     main_menu.add_item(Item('5', 'View saved art', self.view_saved_art))
    #     main_menu.add_item(Item('0', 'Exit'))
        
        # main_menu.run()

    def get_text(self):
        return self.__text
    
    def get_settings(self):
        return self.__settings
    
    def get_figlet(self):
        return self.__figlet
    
    def set_text(self, text):
        self.__text = text

    def set_settings(self, settings):
        self.__settings = settings

    def set_figlet(self, figlet):
        self.__figlet = figlet

    def generate_art(self):
        self.__text = get_text_from_console()
        self.__figlet = Figlet(font=self.__settings._font, width=self.__settings._width)
        self.__figlet = self.__figlet.renderText(self.__text)

        if self.__settings._symbol is not None:
            self.modify_symbols(self.__settings._symbol)

        print("\nArt is generated!")
        

    def modify_symbols(self, symbol):
        for char in self.__figlet:
            if char != '\n' and char != ' ':
                self.__figlet = self.__figlet.replace(char, symbol)

    def change_settings(self):
        self.__settings.settings_menu()
          
    def view_art(self):
        if self.__figlet is None:
            print("No art to preview")
        else:
            print(colored(self.__figlet, self.__settings._color))

    def save_art(self):
        if self.__figlet is None:
            print("No art to save")
            return
        saved_file = FileHandler(ART_PATH)
        saved_file.write_to_file(self.__figlet)

    def view_saved_art(self):
        saved_file = FileHandler(ART_PATH)
        saved_file.read_from_file()
