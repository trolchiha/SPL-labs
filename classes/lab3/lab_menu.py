from UI.menu import Menu
from UI.menu_item import Item
from .figlet_generator import FigletGenerator

def lab_menu():
    figlet_generator = FigletGenerator()
    main_menu = Menu("\nMenu (Lab 3)")
    main_menu.set_color('grey')
    main_menu.add_item(Item('1', 'Generate art', figlet_generator.generate_art))
    main_menu.add_item(Item('2', 'Change settings', figlet_generator.change_settings))
    main_menu.add_item(Item('3', 'Preview', figlet_generator.view_art ))
    main_menu.add_item(Item('4', 'Save art', figlet_generator.save_art))
    main_menu.add_item(Item('5', 'View saved art', figlet_generator.view_saved_art))
    main_menu.add_item(Item('0', 'Exit'))
        
    main_menu.run()