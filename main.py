import importlib
import os

from UI.menu import Menu
from UI.menu_item import Item
import data.lab7.main as lab7

def main():
    labs = [f for f in os.listdir("data") if os.path.isdir(os.path.join("data", f))]
    labs.sort()

    labs_menu = Menu("Labs Menu")
    
    for index, lab in enumerate(labs, start=1):
        module = importlib.import_module(f'data.{lab}.main')
        labs_menu.add_item(Item(str(index), f'Lab {index} ', module.__main__))

    labs_menu.add_item(Item(0, "Exit"))
    labs_menu.run()

# if __name__ == "__main__":
    # main()
lab7.__main__()
