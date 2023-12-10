"""
main Module

This module contains the main function of the program.
It initializes the labs menu, imports lab modules, and runs the menu.

"""
import importlib
import os

from UI.menu import Menu
from UI.menu_item import Item
from logger.logger import logger

def main():
    """
    The main function of the program.
    It initializes the labs menu, imports lab modules, and runs the menu.
    """
    logger.info("The program has started.")
    labs = [f for f in os.listdir("classes") if os.path.isdir(os.path.join("classes", f))]
    labs.sort()

    labs_menu = Menu("Labs Menu")
    for index, lab in enumerate(labs, start=1):
        module = importlib.import_module(f'classes.{lab}.lab_menu')
        labs_menu.add_item(Item(str(index), f'Lab {index} ', module.lab_menu))

    labs_menu.add_item(Item(0, "Exit"))
    labs_menu.run()
    logger.info("The program has ended.")

if __name__ == "__main__":
    main()
