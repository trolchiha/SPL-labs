from .shape import Shape
import sys

from vars import art_path
sys.path.append(art_path)

from art_settings import ArtSettings
from print_art import PrintArt

main = "|"
back = "-"

class Pyramid(Shape, PrintArt):
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
        art = ""
        counter = 1
        size = self.settings.get_size()

        for i in range(1, size+1):
            space = " " * (size - i)
            art += space + main * counter + "\n"
            counter += 2

        return art

    def generate_3D(self):
        art = ""
        counter = 1
        size = self.settings.get_size()
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



    

    

      #x
     ###xx
    #####xxx 
   ######xxxxx 
  ########xxx 
 #########x 

      ##x
     ####xx
    ######xxx
   ########xxxx
  ##########xx
 ###########x

          ##
         ####x
        ######xx
       ########xxx
      ##########xxxx
     ############xxxxx
    ##############xxxxxx
   ################xxxxxxx
  ##################xxxxx
 ####################xx

    ##x
   ####xx
  ######xxx
 ########x