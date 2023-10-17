import sys
from vars import home_path 
sys.path.append(home_path)

from UI.menu import Menu
from UI.menu_item import Item
from calculator import *

def menu():
    main_menu = Menu("Menu")
    main_menu.add_item(Item('1', 'Make Calculations', make_calculation))
    main_menu.add_item(Item('2', 'Change Decimal Places (default 2)', change_decimal_places))
    main_menu.add_item(Item('3', 'View History', view_history))
    main_menu.add_item(Item('4', 'Clear History', clear_history))
    main_menu.add_item(Item('0', 'Exit', exit_calculator))
    crate_history_file()
    
    while True:
        main_menu.print_menu()
        main_menu.select_menu_option()

