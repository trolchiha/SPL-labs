# facade.py

import importlib
import os
from UI.menu import Menu
from UI.menu_item import Item
from logger.logger import logger

class LabSystemFacade:
    def __init__(self):
        self.labs_menu = Menu("Labs Menu")
        self._initialize_labs_menu()

    def _initialize_labs_menu(self):
        labs = [f for f in os.listdir("classes") if os.path.isdir(os.path.join("classes", f))]
        labs.sort()

        for index, lab in enumerate(labs, start=1):
            try:
                module = importlib.import_module(f'classes.{lab}.runner')
                self.labs_menu.add_item(Item(str(index), f'Lab {index} ', module.run))
            except ImportError:
                pass

        self.labs_menu.add_item(Item(0, "Exit"))

    def run_program(self):
        logger.info("The program has started.")
        self.labs_menu.run()
        logger.info("The program has ended.")

if __name__ == "__main__":
    facade = LabSystemFacade()
    facade.run_program()
