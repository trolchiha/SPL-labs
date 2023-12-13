"""
Cube Module

This module defines the Cube class, representing a cube shape. 
The Cube class is a subclass of the Shape and PrintArt classes. 
It provides methods for generating 2D and 3D representations of a cube, 
initializing a 3D array, setting coordinates in the array, and more.
"""
from shared.settings import get_lab_settings
from classes.lab5.art.art_settings import ArtSettings
from classes.lab5.art.print_art import PrintArt
from classes.lab5.shapes.shape import Shape

settings = get_lab_settings("lab5")
DEFAULT_SHAPE_SETTINGS = settings["default_shape_settings"]
DEFAULT_COLOR = DEFAULT_SHAPE_SETTINGS["color"]
DEFAULT_SIZE = DEFAULT_SHAPE_SETTINGS["size"]
DEFAULT_JUSTIFY = DEFAULT_SHAPE_SETTINGS["justify"]


class Cube(Shape, PrintArt):
    """
    Represents a cube shape.

    Attributes:
    - size: The size of the cube
    - justify: The justification of the cube
    - color: The color of the cube
    """

    def __init__(self, size=DEFAULT_SIZE, justify=DEFAULT_JUSTIFY, color=DEFAULT_COLOR):
        """
        Initializes a new instance of the Cube class.

        Parameters:
        - size: The size of the cube (default: DEFAULT_SIZE)
        - justify: The justification of the cube (default: DEFAULT_JUSTIFY)
        - color: The color of the cube (default: DEFAULT_COLOR)
        """
        self._settings = ArtSettings(size, justify, color)
        self._art_2D = self.generate_2D()
        self._art_3D = self.generate_3D()
        PrintArt.__init__(self, self)


    def set_settings(self, cube_settings):
        """
        Sets the settings of the cube.

        Parameters:
        - settings: The settings object to be set
        """
        self._settings = cube_settings
        self._art_2D = self.generate_2D()
        self._art_3D = self.generate_3D()

        
    def get_settings(self):
        """
        Returns the settings of the cube.

        Returns:
        - The settings of the cube
        """
        return self._settings

    def generate_2D(self):
        """
        Generates the 2D representation of the cube.

        Returns:
        - The 2D representation of the cube as a string
        """
        size = self._settings.get_size()
        array_3d = self.__set_coordinates(self.__init_3d_array())
        layers = self.__get_layers(array_3d)
        art_len = size - 1
        
        art = ""
        art += layers[art_len] + "\n"
        for i in range(art_len):
            art += layers[-(size+1)].replace("—", " ") + "\n"

        art += layers[-1] + "\n"
        
        return art

    def generate_3D(self):
        """
        Generates the 3D representation of the cube.

        Returns:
        - The 3D representation of the cube as a string
        """
        array_3d = self.__set_coordinates(self.__init_3d_array())
        layers = self.__get_layers(array_3d)

        size = self._settings.get_size()
        num_of_layers = len(layers)
        art_len = size - 1

        index_1 = 1
        index_2 = size
        # print(layers)

        art = layers[0] + "\n"

        for i in range(art_len):
            art += self.__unite_str(layers[index_1 + i], layers[index_2]) + "\n"

        index_2 = index_2 + index_2 - 1
        index_1 = num_of_layers - size 

        for i in range(art_len):
            art += self.__unite_str(layers[index_1 + i], layers[index_2]) + "\n"

        art += layers[num_of_layers-1]

        return art


    def __init_3d_array(self):
        """
        Initializes a 3D array for the cube.

        Returns:
        - The initialized 3D array
        """
        size = self._settings.get_size()
        array_3d = [[[0 for col in range(size)]for row in range(size)] for x in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    array_3d[i][j][k] = '0'
        return array_3d


    def __set_coordinates(self, array_3d):
        """
        Sets the coordinates of the cube in the 3D array.

        Parameters:
        - array_3d: The 3D array to set the coordinates in

        Returns:
        - The updated 3D array with coordinates set
        """
        N = self._settings.get_size() - 1
        array_3d[0][0][0] = "A"
        array_3d[N][0][0] = "B"
        array_3d[N][0][N] = "C"
        array_3d[0][0][N] = "D"
        array_3d[0][N][0] = "E"
        array_3d[N][N][0] = "F"
        array_3d[N][N][N] = "G"
        array_3d[0][N][N] = "H"

        return array_3d

    def __get_layers(self, array_3d):
        """
        Gets the layers of the cube from the 3D array.

        Parameters:
        - array_3d: The 3D array representing the cube

        Returns:
        - The layers of the cube as a list of strings
        """
        N = self._settings.get_size() - 1
        layers = []
        for y in range(N, -1, -1):
            for z in range(N, -1, -1):
                layer = " "*(z)
                for x in range(N+1):
                    if array_3d[x][y][z]  == '0':
                        if (y != 0 or y != N) and (x == 0 or x == N) and (z == 0 or z == N):
                            layer += "|"
                        elif  x == 0 or x == N:
                            layer += "/"
                        elif z == 0 or z == N:
                            layer += " — "
                        else:
                            layer += "   "
                    else:
                        layer += array_3d[x][y][z]
                layers.append(layer)
            # print(layer, end=" ")
            # print()    
        return layers


    def __unite_str(self, str1, str2):
        """
        Unites two strings by replacing spaces in the first string with non-space characters from the second string.

        Parameters:
        - str1: The first string
        - str2: The second string

        Returns:
        - The united string
        """
        result = ""
        if len(str1) < len(str2):
            str1 += " " * (len(str2) - len(str1))
        else:
            str2 += " " * (len(str1) - len(str2))

        for i in range(len(str1)):
            if str1[i] != " " :
                result += str1[i]
            elif str2[i] != " " and str2[i] != "—":
                result += str2[i]
            else:
                result += " "
        return result

    def get_2D(self):
        """
        Returns the 2D representation of the cube.

        Returns:
        - The 2D representation of the cube as a string
        """
        return self._art_2D
    
    def get_3D(self):
        """
        Returns the 3D representation of the cube.

        Returns:
        - The 3D representation of the cube as a string
        """
        return self._art_3D
