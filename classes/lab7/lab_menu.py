from UI.menu import Menu
from UI.menu_item import Item
from .api_menu import APIMenu
import classes.lab7.tests.main as tests

def lab_menu():
    api = APIMenu()
    menu = Menu("\nSpotify API Menu (Lab 7)")
    menu.set_color("green")
    menu.add_item(Item("1", "Search Menu", api.search_menu))
    menu.add_item(Item("2", "Artist Menu", api.player_menu))
    menu.add_item(Item("3", "History Menu", api.history_menu))
    menu.add_item(Item("4", "Tests", tests.__main__))
    menu.add_item(Item("0", "Exit", ))
    menu.run()
    