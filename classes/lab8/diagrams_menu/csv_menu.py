"""
Module: csv_menu

This module contains the CSVMenu class, which represents a CSV menu for displaying extreme values and diagrams.
"""
from UI.menu import Menu
from UI.menu_item import Item
from classes.lab8.diagrams_saver.diagrams import Diagrams
from shared.settings import get_lab_settings

settings = get_lab_settings("lab8")
CSV_FILE_PATH = settings["csv_file_path"]

class CSVMenu:
    """
    A class representing a CSV menu.

    Attributes:
    - csv_file_path (str): The path to the CSV file.
    - diagrams (Diagrams): An instance of the Diagrams class.
    """

    def __init__(self) :
        self.csv_file_path = CSV_FILE_PATH
        self.diagrams = Diagrams(self.csv_file_path)

    def main_menu(self):
        """
        Displays the main menu.
        """
        main_menu = Menu("\nMenu (Lab 8)")
        main_menu.set_color("red")
        main_menu.add_item(Item("1", "Extreme values", self.values_menu))
        main_menu.add_item(Item("2", "Diagrams", self.diagram_menu))
        main_menu.add_item(Item("0", "Exit"))
        main_menu.run()

    def values_menu(self):
        """
        Displays the values menu.
        """
        values_menu = Menu("\nExtreme values")
        values_menu.set_color("red")
        values_menu.add_item(Item("1", "Min values", self.diagrams.print_min_values))
        values_menu.add_item(Item("2", "Max values", self.diagrams.print_max_values))
        values_menu.add_item(Item("0", "Back"))
        values_menu.run()

    def diagram_menu(self):
        """
        Displays the diagram menu.
        """
        diagram_menu = Menu("\nDiagrams")
        diagram_menu.set_color("red")
        diagram_menu.add_item(Item("1", "Visualize people by country (histogram)", self.diagrams.visualize_histogram))
        diagram_menu.add_item(Item("2", "Visualize percentage of people born after (some year) by country (pie chart)", self.visuzlize_pie_chart_with_input))
        diagram_menu.add_item(Item("3", "Visualize average age of people by country (column diagram)", self.diagrams.visualize_column_diagram))
        diagram_menu.add_item(Item("4", "Visualize average age of people born in (some month) by country (linear diagram and sector diagram)", self.visuzlize_line_plot_and_sector_with_input))
        diagram_menu.add_item(Item("0", "Back"))
        diagram_menu.run()

    def visuzlize_pie_chart_with_input(self):
        """
        Visualizes a pie chart based on user input.
        """
        year = input("Enter year (1950-2005): ")
        if year.isdigit():
            year = int(year)
            if 1950 <= year <= 2005:
                self.diagrams.visualize_sector_diagram(year)
                return
        
        print("Invalid input.")
        self.diagrams.visualize_sector_diagram()

    def visuzlize_line_plot_and_sector_with_input(self):
        """
        Visualizes a line plot and sector diagram based on user input.
        """
        month = input("Enter month (1-12): ")
        if month.isdigit():
            month = int(month)
            if 1 <= month <= 12:
                self.diagrams.visualize_line_plot_and_sector(month)
                return
            
        print("Invalid input.")
        self.diagrams.visualize_line_plot_and_sector()
        