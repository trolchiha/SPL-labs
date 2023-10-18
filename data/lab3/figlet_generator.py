import sys
from figlet_settings import FigletSettings
from vars import home_path, art_path
sys.path.append(home_path)

from pyfiglet import Figlet
from termcolor import colored

from UI.menu import Menu
from UI.menu_item import Item
from shared.file_handler import FileHandler
from data_from_console import get_text_from_console

class FigletGenerator:
    def __init__(self, text=None):
        self.text = text
        self.settings = FigletSettings()
        self.figlet = None

    def menu(self):
        main_menu = Menu("\nMenu")
        main_menu.set_color('grey')
        main_menu.add_item(Item('1', 'Generate art', self.generate_art))
        main_menu.add_item(Item('2', 'Change settings', self.change_settings))
        main_menu.add_item(Item('3', 'Preview', self.view_art ))
        main_menu.add_item(Item('4', 'Save art', self.save_art))
        main_menu.add_item(Item('5', 'View saved art', self.view_saved_art))
        main_menu.add_item(Item('0', 'Exit', self.exit_program))
        
        main_menu.run()

    def generate_art(self):
        self.text = get_text_from_console()
        self.figlet = Figlet(font=self.settings.font, width=self.settings.width)
        self.figlet = self.figlet.renderText(self.text)

        if self.settings.symbol is not None:
            self.modify_symbols(self.settings.symbol)

        print("\nArt is generated!\n")
        

    def modify_symbols(self, symbol):
        for char in self.figlet:
            if char != '\n' and char != ' ':
                self.figlet = self.figlet.replace(char, symbol)

    def change_settings(self):
        self.settings.settings_menu()
          
    def view_art(self):
        if self.figlet is None:
            print("No art to preview")
        else:
            print(colored(self.figlet, self.settings.color))

    def save_art(self):
        if self.figlet is None:
            print("No art to save")
            return
        saved_file = FileHandler(art_path)
        saved_file.write_to_file(self.figlet)

    def view_saved_art(self):
        saved_file = FileHandler(art_path)
        saved_file.read_from_file()

    def exit_program(self):
        print("Exiting...")
        sys.exit(0)
