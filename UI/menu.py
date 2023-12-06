import termcolor
from termcolor import colored
import logging

logger = logging.getLogger(__name__)

class Menu:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.option = None
        self.exit_option = '0'
        self.color = 'white'

    def add_item(self, item):
        self.items.append(item)

    def print_menu(self):
        print(colored((f"{self.name}:"), self.color))
        for item in self.items:
            print(colored(item, self.color))

    def set_menu_option(self):
        self.option = input(colored("Enter your choice: ", "white"))
        
    def run_function(self, option):
        for item in self.items:
            if item.id == option:
                item.function()
                logger.info("The function %s has been called.", item.function.__name__)
                break

    def run(self):
        while True:
            logger.info("The menu %s has been called.", self.name.replace("\n", ""))
            self.print_menu()
            self.set_menu_option()
            if self.option == self.exit_option:
                break
            self.run_function(self.option)
            
    def change_exit_option(self, option):
        self.exit_option = option

    def set_color(self, color):
        if color in termcolor.COLORS:
            self.color = color
