"""
Module: main

This module provides a simple script to run the Lab System Facade.
"""
from UI.labsystem_facade import LabSystemFacade

if __name__ == "__main__":
    """
    Initializes and runs the Lab System Facade.
    """
    facade = LabSystemFacade()
    facade.run_program()
