from termcolor import colored
from classes.lab4.data_from_console import get_console_width

class PrintArt:
    def __init__(self, Shape):
        self._shape = Shape

    def get_shape(self):
        return self._shape
    
    def set_shape(self, shape):
        self._shape = shape

    def print_art_2D(self):
        art = self.__justify_art(self._shape._art_2D)
        print(colored("\nArt 2D\n"))
        print(colored(art, self._shape._settings.get_color()))

    def print_art_3D(self):
        art = self.__justify_art(self._shape._art_3D)
        print(colored("\nArt 3D\n"))
        print(colored(art, self._shape._settings.get_color()))

    def __justify_art(self, art):
        padding = self.__get_padding(art)
        art_lines = art.split('\n')
        aligned_lines = [" " * padding + line for line in art_lines]
        art = '\n'.join(aligned_lines)
        return art

    def __get_padding(self, art):
        console_width = get_console_width()
        art_len = len(art)//self._shape._settings.get_size()
        justify = self._shape._settings.get_justify()
        
        if justify == "center":
            return (console_width - art_len) // 2
        elif justify == "right":
            return console_width - art_len
        else:
            return 0

        