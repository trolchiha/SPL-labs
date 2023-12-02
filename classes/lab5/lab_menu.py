from UI.menu import Menu
from UI.menu_item import Item
from .art.art_menu import ArtMenu

def lab_menu():
    art = ArtMenu()
    art_menu = Menu("\nArt Menu")
    art_menu.add_item(Item('1', 'Choose shape', art.set_shape))
    art_menu.add_item(Item('0', 'Exit'))

    art_menu.run()
