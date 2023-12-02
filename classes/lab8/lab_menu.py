from UI.menu import Menu
from UI.menu_item import Item
from .csv_menu import CSVMenu

def lab_menu():
    csv_menu = CSVMenu()
    main_menu = Menu("\nMenu")
    main_menu.set_color("red")
    main_menu.add_item(Item("1", "Extreme values", csv_menu.values_menu))
    main_menu.add_item(Item("2", "Diagrams", csv_menu.diagram_menu))
    main_menu.add_item(Item("0", "Exit"))
    main_menu.run()
