import importlib
import os

from UI.menu import Menu
from UI.menu_item import Item
import classes.lab8.main as lab

def main():
    labs = [f for f in os.listdir("classes") if os.path.isdir(os.path.join("data", f))]
    labs.sort()

    labs_menu = Menu("Labs Menu")
    
    for index, lab in enumerate(labs, start=1):
        module = importlib.import_module(f'data.{lab}.main')
        labs_menu.add_item(Item(str(index), f'Lab {index} ', module.__main__))

    labs_menu.add_item(Item(0, "Exit"))
    labs_menu.run()

if __name__ == "__main__":
    lab.__main__()
    # main()
