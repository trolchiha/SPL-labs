"""
Module: run_art_generator

Module provides a simple script to run the Art Generator for Lab 4.

"""
from classes.lab4.art_generator.art_generator import ArtGenerator

def run():
    """
    Initializes and runs the Art Generator.
    """
    art_generator = ArtGenerator()
    art_generator.menu()
