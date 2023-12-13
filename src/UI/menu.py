"""
Represents a menu.

"""
import logging
import termcolor
from termcolor import colored

logger = logging.getLogger(__name__)

class Menu:
    """
    Represents a menu with various options.

    Attributes:
    - name (str): The name of the menu.
    - items (list): The list of menu items.
    - option (str): The selected menu option.
    - exit_option (str): The option to exit the menu.
    - color (str): The color of the menu text.
    """

    def __init__(self, name):
        """
        Initialize a Menu object.

        Args:
        - name (str): The name of the menu.
        """
        self.name = name
        self.items = []
        self.option = None
        self.exit_option = '0'
        self.color = 'white'

    def add_item(self, item):
        """
        Add an item to the menu.

        Args:
        - item (str): The item to be added to the menu.
        """
        self.items.append(item)

    def print_menu(self):
        """
        Print the menu with colored text.
        """
        print(colored((f"{self.name}:"), self.color))
        for item in self.items:
            print(colored(item, self.color))

    def set_menu_option(self):
        """
        Set the selected menu option.
        """
        self.option = input(colored("Enter your choice: ", "white"))
        
    def run_function(self, option):
        """
        Run the function associated with the selected menu option.

        Args:
        - option (str): The selected menu option.
        """
        for item in self.items:
            if item.item_id == option:
                item.function()
                logger.info("The function %s has been called.", item.function.__name__)
                break

    def run(self):
        """
        Run the menu until the exit option is selected.
        """
        while True:
            logger.info("The menu %s has been called.", self.name.replace("\n", ""))
            self.print_menu()
            self.set_menu_option()
            if self.option == self.exit_option:
                break
            self.run_function(self.option)
            
    def change_exit_option(self, option):
        """
        Change the exit option of the menu.

        Args:
        - option (str): The new exit option.
        """
        self.exit_option = option

    def set_color(self, color):
        """
        Set the color of the menu text.

        Args:
        - color (str): The color to be set.
        """
        if color in termcolor.COLORS:
            self.color = color
