"""
Print Art Module

A module that defines the PrintArt class for printing 2D and 3D art.
"""
from termcolor import colored
from classes.lab4.console_reader.data_from_console import get_console_width

class PrintArt:
    """
    A class that represents the printing of art.

    Attributes:
    - _shape: The Shape object to be printed.
    """

    def __init__(self, Shape):
        """
        Initialize the PrintArt object.

        Parameters:
        - Shape: The Shape object to be printed.
        """
        self._shape = Shape

    def get_shape(self):
        """
        Get the Shape object associated with the PrintArt object.

        Returns:
        - The Shape object.
        """
        return self._shape
    
    def set_shape(self, shape):
        """
        Set the Shape object associated with the PrintArt object.

        Parameters:
        - shape: The new Shape object.
        """
        self._shape = shape

    def print_art_2D(self):
        """
        Print the 2D art of the Shape object.
        """
        art = self.__justify_art(self._shape.get_2D())
        print(colored("\nArt 2D\n"))
        print(colored(art, self._shape.get_settings().get_color()))

    def print_art_3D(self):
        """
        Print the 3D art of the Shape object.
        """
        art = self.__justify_art(self._shape.get_3D())
        print(colored("\nArt 3D\n"))
        print(colored(art, self._shape.get_settings().get_color()))

    def __justify_art(self, art):
        """
        Justify the art by adding padding based on the justification settings.

        Parameters:
        - art: The art to be justified.

        Returns:
        - The justified art.
        """
        padding = self.__get_padding(art)
        art_lines = art.split('\n')
        aligned_lines = [" " * padding + line for line in art_lines]
        art = '\n'.join(aligned_lines)
        return art

    def __get_padding(self, art):
        """
        Calculate the padding based on the console width and justification settings.

        Parameters:
        - art: The art to be justified.

        Returns:
        - The padding value.
        """
        console_width = get_console_width()
        art_len = len(art)//self._shape.get_settings().get_size()
        justify = self._shape.get_settings().get_justify()
        
        if justify == "center":
            return (console_width - art_len) // 2
        if justify == "right":
            return console_width - art_len
        return 0
        