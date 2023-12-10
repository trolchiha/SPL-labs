"""
Module: art_size

This module defines the ArtSize class, which represents the size of an art.

Attributes:
    DEFAULT_WIDTH (int): Default width for the art.
    DEFAULT_HEIGHT (int): Default height for the art.

Classes:
    ArtSize:
        A class representing the size of an art.

Methods:
    - __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT): 
    Initializes the ArtSize object.
    - __str__(self): Returns a string representation of the ArtSize object.
    - set_width(self, width): Sets the width of the art.
    - set_height(self, height): Sets the height of the art.
    - set_chars(self, chars): Sets the characters representing the art.
    - get_width(self): Returns the width of the art.
    - get_height(self): Returns the height of the art.
    - get_chars(self): Returns the characters representing the art.
    - get_resized_chars(self): Returns the resized characters representing the art.
    - __change_char_size(self, matrix): Changes the size of a character matrix.
    - __change_width(self, matrix): Changes the width of a character matrix.
    - __change_height(self, matrix): Changes the height of a character matrix.
"""
import numpy as np
from shared.settings import get_lab_settings

settings = get_lab_settings("lab4")
DEFAULT_ART_SETTINGS = settings["default_art_settings"]
DEFAULT_WIDTH = DEFAULT_ART_SETTINGS["width"]
DEFAULT_HEIGHT = DEFAULT_ART_SETTINGS["height"]

class ArtSize:
    """
    A class representing the size of an art.

    Attributes:
        _width (int): The width of the art.
        _height (int): The height of the art.
        _chars (list): The characters representing the art.

    Methods:
        __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT): Initializes the ArtSize object.
        __str__(self): Returns a string representation of the ArtSize object.
        set_width(self, width): Sets the width of the art.
        set_height(self, height): Sets the height of the art.
        set_chars(self, chars): Sets the characters representing the art.
        get_width(self): Returns the width of the art.
        get_height(self): Returns the height of the art.
        get_chars(self): Returns the characters representing the art.
        get_resized_chars(self): Returns the resized characters representing the art.
    """

    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        """
        Initializes the ArtSize object.

        Args:
            width (int): The width of the art. Defaults to DEFAULT_WIDTH.
            height (int): The height of the art. Defaults to DEFAULT_HEIGHT.
        """
        self._width = width
        self._height = height
        self._chars = None

    def __str__(self):
        """
        Returns a string representation of the ArtSize object.

        Returns:
            str: The string representation of the ArtSize object.
        """
        return f"Width: {self._width} \nHeight: {self._height}"

    def set_width(self, width):
        """
        Sets the width of the art.

        Args:
            width (int): The width of the art.
        """
        self._width = width

    def set_height(self, height):
        """
        Sets the height of the art.

        Args:
            height (int): The height of the art.
        """
        self._height = height

    def set_chars(self, chars):
        """
        Sets the characters representing the art.

        Args:
            chars (list): The characters representing the art.
        """
        self._chars = chars

    def get_width(self):
        """
        Returns the width of the art.

        Returns:
            int: The width of the art.
        """
        return self._width
    
    def get_height(self):
        """
        Returns the height of the art.

        Returns:
            int: The height of the art.
        """
        return self._height
    
    def get_chars(self):
        """
        Returns the characters representing the art.

        Returns:
            list: The characters representing the art.
        """
        return self._chars

    def get_resized_chars(self):
        """
        Returns the resized characters representing the art.

        Returns:
            list: The resized characters representing the art.
        """
        resized_chars = []
        if self._chars is None:
            return "No chars to resize"
        for char in self._chars:
            resized_chars.append(self.__change_char_size(char))
        
        self._chars = resized_chars
        return resized_chars

    def __change_char_size(self, matrix):
        """
        Changes the size of a character matrix.

        Args:
            matrix (list): The character matrix to resize.

        Returns:
            list: The resized character matrix.
        """
        matrix = self.__change_height(matrix)
        matrix = self.__change_width(matrix)
        return matrix

    def __change_width(self, matrix):
        """
        Changes the width of a character matrix.

        Args:
            matrix (list): The character matrix to resize.

        Returns:
            list: The resized character matrix.
        """
        if self._width <= 5:
            return matrix
        
        columns_to_add = self._width-5
        column_index = round(len(matrix[0])/2)
        column_to_add = [row[column_index] for row in matrix]
        np_matrix = np.array(matrix)
        
        for i in range(columns_to_add):
            np_matrix = np.insert(np_matrix, column_index, column_to_add, axis=1)

        matrix = np_matrix.tolist()
        return matrix

    def __change_height(self, matrix):
        """
        Changes the height of a character matrix.

        Args:
            matrix (list): The character matrix to resize.

        Returns:
            list: The resized character matrix.
        """
        if self._height <= 5:
            return matrix
        
        lines_to_add = round((self._height-5)/2)
        top_line = matrix[1]
        bottom_line = matrix[len(matrix) - 2]

        np_matrix = np.array(matrix)

        for i in range(lines_to_add):
            top_row_index = 1
            bottom_row_index = np_matrix.shape[0] - 1
            np_matrix = np.insert(np_matrix, top_row_index, top_line, axis=0)
            np_matrix = np.insert(np_matrix, bottom_row_index, bottom_line, axis=0)

        matrix = np_matrix.tolist()
        return matrix
    