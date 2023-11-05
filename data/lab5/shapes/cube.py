import sys

from vars import art_path
sys.path.append(art_path)

from art_settings import ArtSettings
from print_art import PrintArt
from .shape import Shape


class Cube(Shape, PrintArt):
    def __init__(self, size=6, justify="left", color="white"):
        self.settings = ArtSettings(size, justify, color)
        self.art_2D = self.generate_2D()
        self.art_3D = self.generate_3D()
        PrintArt.__init__(self, self)


    def set_settings(self, settings):
        self.settings = settings
        self.art_2D = self.generate_2D()
        self.art_3D = self.generate_3D()

    def generate_2D(self):
        size = self.settings.get_size()
        array_3d = self.set_coordinates(self.init_3d_array())
        layers = self.get_layers(array_3d)
        art_len = size - 1
        
        art = ""
        art += layers[art_len] + "\n"
        for i in range(art_len):
            art += layers[-(size+1)].replace("—", " ") + "\n"

        art += layers[-1] + "\n"
        
        return art

    def generate_3D(self):
        array_3d = self.set_coordinates(self.init_3d_array())
        layers = self.get_layers(array_3d)

        size = self.settings.get_size()
        num_of_layers = len(layers)
        art_len = size - 1

        index_1 = 1
        index_2 = size
        # print(layers)

        art = layers[0] + "\n"

        for i in range(art_len):
            art += self.unite_str(layers[index_1 + i], layers[index_2]) + "\n"

        index_2 = index_2 + index_2 - 1
        index_1 = num_of_layers - size 

        for i in range(art_len):
            art += self.unite_str(layers[index_1 + i], layers[index_2]) + "\n"

        art += layers[num_of_layers-1]

        return art


    def init_3d_array(self):
        size = self.settings.get_size()
        array_3d = [[[0 for col in range(size)]for row in range(size)] for x in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    array_3d[i][j][k] = '0'
        return array_3d


    def set_coordinates(self, array_3d):
        N = self.settings.get_size() - 1
        array_3d[0][0][0] = "A"
        array_3d[N][0][0] = "B"
        array_3d[N][0][N] = "C"
        array_3d[0][0][N] = "D"
        array_3d[0][N][0] = "E"
        array_3d[N][N][0] = "F"
        array_3d[N][N][N] = "G"
        array_3d[0][N][N] = "H"

        return array_3d

    def get_layers(self, array_3d):
        N = self.settings.get_size() - 1
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


    def unite_str(self, str1, str2):
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




