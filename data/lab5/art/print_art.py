from termcolor import colored
from data.lab4.art.data_from_console import get_console_width

class PrintArt:
    def __init__(self, Shape):
        self.shape = Shape

    def print_art_2D(self):
        art = self.justify_art(self.shape.art_2D)
        print(colored("\nArt 2D\n"))
        print(colored(art, self.shape.settings.get_color()))

    def print_art_3D(self):
        art = self.justify_art(self.shape.art_3D)
        print(colored("\nArt 3D\n"))
        print(colored(art, self.shape.settings.get_color()))

    def justify_art(self, art):
        padding = self.get_padding(art)
        art_lines = art.split('\n')
        aligned_lines = [" " * padding + line for line in art_lines]
        art = '\n'.join(aligned_lines)
        return art

    def get_padding(self, art):
        console_width = get_console_width()
        art_len = len(art)//self.shape.settings.get_size()
        justify = self.shape.settings.get_justify()
        
        if justify == "center":
            return (console_width - art_len) // 2
        elif justify == "right":
            return console_width - art_len
        else:
            return 0

        