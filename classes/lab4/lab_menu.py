from UI.menu import Menu
from UI.menu_item import Item
from .art_generator import ArtGenerator

def lab_menu():
    art_generator = ArtGenerator()
    art_menu = Menu("\nArt Menu (Lab 4)")
    art_menu.add_item(Item('1', 'Set Art Text', art_generator.set_text))
    art_menu.add_item(Item('2', 'Change Settings', art_generator.change_settings))
    art_menu.add_item(Item('3', 'View Art', art_generator.view_art))
    art_menu.add_item(Item('4', 'Save Art to File', art_generator.save_art_to_file))
    art_menu.add_item(Item('5', 'View Saved Art', art_generator.view_saved_art))
    art_menu.add_item(Item('0', 'Exit'))

    art_menu.run()