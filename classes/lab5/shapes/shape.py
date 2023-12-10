"""
A module that defines the Shape abstract base class for shapes.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class for shapes.
    """

    @abstractmethod
    def generate_2D(self):
        """
        Abstract method to generate a 2D representation of the shape.
        """
        
    @abstractmethod
    def generate_3D(self):
        """
        Abstract method to generate a 3D representation of the shape.
        """

    @abstractmethod
    def set_settings(self):
        """
        Abstract method to set the settings of the shape.
        """
