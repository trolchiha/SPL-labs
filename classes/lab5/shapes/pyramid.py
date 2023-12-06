from .shape import Shape

from classes.lab5.art.art_settings import ArtSettings
from classes.lab5.art.print_art import PrintArt
from classes.lab5.settings import DEFAULT_SIZE, DEFAULT_JUSTIFY, DEFAULT_COLOR

main = "|"
back = "-"

class Pyramid(Shape, PrintArt):
    def __init__(self, size=DEFAULT_SIZE, justify=DEFAULT_JUSTIFY, color=DEFAULT_COLOR):
        self._settings = ArtSettings(size, justify, color)
        self._art_2D = self.generate_2D()
        self._art_3D = self.generate_3D()
        PrintArt.__init__(self, self)

    def set_settings(self, settings):
        self._settings = settings
        self._art_2D = self.generate_2D()
        self._art_3D = self.generate_3D()

    def get_settings(self):
        return self._settings

    def generate_2D(self):
        art = ""
        counter = 1
        size = self._settings.get_size()

        for i in range(1, size+1):
            space = " " * (size - i)
            art += space + main * counter + "\n"
            counter += 2

        return art

    def generate_3D(self):
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