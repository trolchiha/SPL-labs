from UI.menu import Menu
from UI.menu_item import Item
from shared.file_handler import FileHandler

from classes.lab5.shapes.cube import Cube
from classes.lab5.shapes.pyramid import Pyramid
from classes.lab5.settings import ART_2D_PATH, ART_3D_PATH

class ArtMenu:
    def __init__(self):
        self.__shape = None

    # def main_menu(self):
    #     art_menu = Menu("\nArt Menu")
    #     art_menu.add_item(Item('1', 'Choose shape', self.set_shape))
    #     art_menu.add_item(Item('0', 'Exit'))

    #     art_menu.run()

    def set_shape(self):
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
        return self.__shape

    def sub_menu(self):
        sub_menu = Menu("\nArt Menu")
        sub_menu.add_item(Item('1', 'View 2D', self.view_art_2D))
        sub_menu.add_item(Item('2', 'View 3D', self.view_art_3D))
        sub_menu.add_item(Item('3', 'Change Settings', self.change_settings))
        sub_menu.add_item(Item('4', 'Save Art', self.save_menu))
        sub_menu.add_item(Item('0', 'Back'))

        sub_menu.run()

    def view_art_2D(self):
        self.__shape.print_art_2D()

    def view_art_3D(self):
        self.__shape.print_art_3D()

    def change_settings(self):
        self.__shape._settings.settings_menu()
        self.__shape.set_settings(self.__shape._settings.get_settings_obj())

    def save_menu(self):
        save_menu = Menu("\nSave Menu")
        save_menu.add_item(Item('1', 'Save 2D to File', self._save_to_file_2D))
        save_menu.add_item(Item('2', 'Save 3D to File', self._save_to_file_3D))
        save_menu.add_item(Item('3', 'View Saved 2D', self._view_saved_2D))
        save_menu.add_item(Item('4', 'View Saved 3D', self._view_saved_3D))
        save_menu.add_item(Item('0', 'Back'))

        save_menu.run()

    def _save_to_file_2D(self):
        saved_file = FileHandler(ART_2D_PATH)
        saved_file.write_to_file(self.shape.art_2D)

    def _save_to_file_3D(self):
        saved_file = FileHandler(ART_3D_PATH)
        saved_file.write_to_file(self.shape.art_3D)

    def _view_saved_2D(self):
        saved_file = FileHandler(ART_2D_PATH)
        saved_file.read_from_file()

    def _view_saved_3D(self):
        saved_file = FileHandler(ART_3D_PATH)
        saved_file.read_from_file()
