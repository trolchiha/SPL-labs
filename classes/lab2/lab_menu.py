from UI.menu import Menu
from UI.menu_item import Item
from .calculator import Calculator

def lab_menu():
    calculator = Calculator()
    terminal_menu = Menu("Menu")
    terminal_menu.add_item(Item("1", "Perform calculations", calculator.perform_calculations))
    terminal_menu.add_item(Item("2", "Change decimal places (default 2)", calculator.change_decimal_places))
    terminal_menu.add_item(Item("3", "View history", calculator.view_history))
    terminal_menu.add_item(Item("4", "Clear history", calculator.clear_history))
    terminal_menu.add_item(Item("0", "Exit"))
    terminal_menu.run()
