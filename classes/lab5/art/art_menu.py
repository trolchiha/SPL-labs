"""
A module that defines the ArtMenu class for creating and manipulating shapes.
"""
from UI.menu import Menu
from UI.menu_item import Item
from shared.file_handler import FileHandler
from shared.settings import get_lab_settings
from classes.lab5.shapes.cube import Cube
from classes.lab5.shapes.pyramid import Pyramid

settings = get_lab_settings("lab5")
ART_2D_PATH = settings["art_2D_path"]
ART_3D_PATH = settings["art_3D_path"]

class ArtMenu:
    """
    A class representing an art menu for creating and manipulating shapes.

    Attributes:
    - __shape: The currently selected shape.

    Methods:
    - __init__(self): Initializes an instance of the ArtMenu class.
    - set_shape(self): Sets the shape based on user input.
    - get_shape(self): Returns the currently selected shape.
    - sub_menu(self): Displays a sub-menu for viewing and manipulating the shape.
    - view_art_2D(self): Prints the 2D representation of the shape.
    - view_art_3D(self): Prints the 3D representation of the shape.
    - change_settings(self): Displays a menu for changing the settings of the shape.
    - save_menu(self): Displays a menu for saving and viewing the saved art.
    - _save_to_file_2D(self): Saves the 2D representation of the shape to a file.
    - _save_to_file_3D(self): Saves the 3D representation of the shape to a file.
    - _view_saved_2D(self): Reads and displays the saved 2D art from a file.
    - _view_saved_3D(self): Reads and displays the saved 3D art from a file.
    """
    def __init__(self):
        self.__shape = None

    def main_menu(self):
            art_menu = Menu("\nArt Menu")
            art_menu.add_item(Item('1', 'Choose shape', self.set_shape))
            art_menu.add_item(Item('0', 'Exit'))

            art_menu.run()

    def set_shape(self):
        """
        Sets the shape based on user input.
        """
        shape = input("Choose shape [ cube, pyramid ]: ")
        if shape not in ['cube', 'pyramid']:
            print("Invalid shape")
            return
        
        if shape == 'cube':
            self.__shape = Cube()
        
        if shape == 'pyramid':
            self.__shape = Pyramid()

        self.sub_menu()

    def get_shape(self):
        """
        Returns the currently selected shape.
        """
        return self.__shape

    def sub_menu(self):
        """
        Displays a sub-menu for viewing and manipulating the shape.
        """
        sub_menu = Menu("\nArt Menu")
        sub_menu.add_item(Item('1', 'View 2D', self.view_art_2D))
        sub_menu.add_item(Item('2', 'View 3D', self.view_art_3D))
        sub_menu.add_item(Item('3', 'Change Settings', self.change_settings))
        sub_menu.add_item(Item('4', 'Save Art', self.save_menu))
        sub_menu.add_item(Item('0', 'Back'))

        sub_menu.run()

    def view_art_2D(self):
        """
        Prints the 2D representation of the shape.
        """
        self.__shape.print_art_2D()

    def view_art_3D(self):
        """
        Prints the 3D representation of the shape.
        """
        self.__shape.print_art_3D()

    def change_settings(self):
        """
        Displays a menu for changing the settings of the shape.
        """
        self.__shape.get_settings().settings_menu()
        self.__shape.set_settings(self.__shape.get_settings().get_settings_obj())

    def save_menu(self):
        """
        Displays a menu for saving and viewing the saved art.
        """
        save_menu = Menu("\nSave Menu")
        save_menu.add_item(Item('1', 'Save 2D to File', self._save_to_file_2D))
        save_menu.add_item(Item('2', 'Save 3D to File', self._save_to_file_3D))
        save_menu.add_item(Item('3', 'View Saved 2D', self._view_saved_2D))
        save_menu.add_item(Item('4', 'View Saved 3D', self._view_saved_3D))
        save_menu.add_item(Item('0', 'Back'))

        save_menu.run()

    def _save_to_file_2D(self):
        """
        Saves the 2D representation of the shape to a file.
        """
        saved_file = FileHandler(ART_2D_PATH)
        saved_file.write_to_file(self.__shape.get_2D())

    def _save_to_file_3D(self):
        """
        Saves the 3D representation of the shape to a file.
        """
        saved_file = FileHandler(ART_3D_PATH)
        saved_file.write_to_file(self.__shape.get_3D())

    def _view_saved_2D(self):
        """
        Reads and displays the saved 2D art from a file.
        """
        saved_file = FileHandler(ART_2D_PATH)
        saved_file.read_from_file()

    def _view_saved_3D(self):
        """
        Reads and displays the saved 3D art from a file.
        """
        saved_file = FileHandler(ART_3D_PATH)
        saved_file.read_from_file()
