from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def generate_2D(self):
        pass

    @abstractmethod
    def generate_3D(self):
        pass

    @abstractmethod
    def set_settings(self):
        pass
