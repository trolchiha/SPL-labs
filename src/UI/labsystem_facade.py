"""
Module: lab_system_facade

This module provides the Lab System Facade, which initializes and runs a menu for executing different lab modules.
"""
import importlib
import os
from UI.menu import Menu
from UI.menu_item import Item
from logger.logger import logger

class LabSystemFacade:
    """
    A class representing the Lab System Facade.

    Attributes:
    - labs_menu (Menu): The main menu for navigating through different lab modules.
    """

    def __init__(self):
        """
        Initializes a LabSystemFacade object.
        """
        self.labs_menu = Menu("Labs Menu")
        self._initialize_labs_menu()

    def _initialize_labs_menu(self):
        """
        Initializes the labs menu dynamically based on available lab modules.
        """
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
        """
        Runs the Lab System Facade, logging the start and end of the program.
        """
        logger.info("The program has started.")
        self.labs_menu.run()
        logger.info("The program has ended.")
        