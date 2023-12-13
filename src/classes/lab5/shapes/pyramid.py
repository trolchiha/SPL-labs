"""
Pyramid Module

This module defines the Pyramid class, representing a pyramid shape. 
The Pyramid class is a subclass of the Shape and PrintArt classes. 
It provides methods for generating 2D and 3D representations of a pyramid, 
initializing a 3D array, setting coordinates in the array, and more.
"""
from classes.lab5.art.art_settings import ArtSettings
from classes.lab5.art.print_art import PrintArt
from shared.settings import get_lab_settings
from .shape import Shape

settings = get_lab_settings("lab5")
DEFAULT_SHAPE_SETTINGS = settings["default_shape_settings"]
DEFAULT_SIZE = DEFAULT_SHAPE_SETTINGS["size"]
DEFAULT_JUSTIFY = DEFAULT_SHAPE_SETTINGS["justify"]
DEFAULT_COLOR = DEFAULT_SHAPE_SETTINGS["color"]

main = "|"
back = "-"

class Pyramid(Shape, PrintArt):
    """
    Represents a pyramid shape.

    Attributes:
        _settings (ArtSettings): The settings of the pyramid.
        _art_2D (str): The 2D representation of the pyramid.
        _art_3D (str): The 3D representation of the pyramid.
    """

    def __init__(self, size=DEFAULT_SIZE, justify=DEFAULT_JUSTIFY, color=DEFAULT_COLOR):
        """
        Initializes a Pyramid object.

        Args:
            size (int): The size of the pyramid.
            justify (str): The justification of the pyramid.
            color (str): The color of the pyramid.
        """
        self._settings = ArtSettings(size, justify, color)
        self._art_2D = self.generate_2D()
        self._art_3D = self.generate_3D()
        PrintArt.__init__(self, self)

    def set_settings(self, pyramid_settings):
        """
        Sets the settings of the pyramid.

        Args:
            settings (ArtSettings): The settings to be set.
        """
        self._settings = pyramid_settings
        self._art_2D = self.generate_2D()
        self._art_3D = self.generate_3D()

    def get_settings(self):
        """
        Returns the settings of the pyramid.

        Returns:
            ArtSettings: The settings of the pyramid.
        """
        return self._settings

    def generate_2D(self):
        """
        Generates the 2D representation of the pyramid.

        Returns:
            str: The 2D representation of the pyramid.
        """
        art = ""
        counter = 1
        size = self._settings.get_size()

        for i in range(1, size+1):
            space = " " * (size - i)
            art += space + main * counter + "\n"
            counter += 2

        return art

    def generate_3D(self):
        """
        Generates the 3D representation of the pyramid.

        Returns:
            str: The 3D representation of the pyramid.
        """
        art = ""
        counter = 1
        size = self._settings.get_size()
        stop = size - round(size/5)
        step = round(stop/(size - stop+2))
        num = step

        for i in range(1, size+1):
            space = " " * (size - i)

            if i >= stop:
                art += space + main * counter + back * (i-num) + "\n"
                num += step+1
            else:
                art += space + main * counter + back * i + "\n"
            
            counter += 2

        return art

    def get_2D(self):
        """
        Returns the 2D representation of the pyramid.

        Returns:
            str: The 2D representation of the pyramid.
        """
        return self._art_2D
    
    def get_3D(self):
        """
        Returns the 3D representation of the pyramid.

        Returns:
            str: The 3D representation of the pyramid.
        """
        return self._art_3D
    