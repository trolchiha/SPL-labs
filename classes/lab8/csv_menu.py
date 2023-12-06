from UI.menu import Menu
from UI.menu_item import Item
from .diagrams import Diagrams
from .settings import CSV_FILE_PATH

class CSVMenu:
    def __init__(self) :
        self.csv_file_path = CSV_FILE_PATH
        self.diagrams = Diagrams(self.csv_file_path)

    def main_menu(self):
        main_menu = Menu("\nMenu (Lab 8)")
        main_menu.set_color("red")
        main_menu.add_item(Item("1", "Extreme values", self.values_menu))
        main_menu.add_item(Item("2", "Diagrams", self.diagram_menu))
        main_menu.add_item(Item("0", "Exit"))
        main_menu.run()

    def values_menu(self):
        values_menu = Menu("\nExtreme values")
        values_menu.set_color("red")
        values_menu.add_item(Item("1", "Min values", self.diagrams.print_min_values))
        values_menu.add_item(Item("2", "Max values", self.diagrams.print_max_values))
        values_menu.add_item(Item("0", "Back"))
        values_menu.run()

    def diagram_menu(self):
        diagram_menu = Menu("\nDiagrams")
        diagram_menu.set_color("red")
        diagram_menu.add_item(Item("1", "Visualize people by country (histogram)", self.diagrams.visualize_histogram))
        diagram_menu.add_item(Item("2", "Visualize percentage of people born after (some year) by country (pie chart)", self.visuzlize_pie_chart_with_input))
        diagram_menu.add_item(Item("3", "Visualize average age of people by country (column diagram)", self.diagrams.visualize_column_diagram))
        diagram_menu.add_item(Item("4", "Visualize average age of people born in (some month) by country (linear diagram and sector diagram)", self.visuzlize_line_plot_and_sector_with_input))
        diagram_menu.add_item(Item("0", "Back"))
        diagram_menu.run()

    def visuzlize_pie_chart_with_input(self):
        year = input("Enter year (1950-2005): ")
        if year.isdigit():
            year = int(year)
            if year >= 1950 and year <= 2005:
                self.diagrams.visualize_sector_diagram(year)
                return
        
        print("Invalid input.")
        self.diagrams.visualize_sector_diagram()

    def visuzlize_line_plot_and_sector_with_input(self):
        month = input("Enter month (1-12): ")
        if month.isdigit():
            month = int(month)
            if month >= 1 and month <= 12:
                self.diagrams.visualize_line_plot_and_sector(month)
                return
            
        print("Invalid input.")
        self.diagrams.visualize_line_plot_and_sector()
        