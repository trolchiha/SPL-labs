"""
InputHandler Module

This module provides a class for handling user input. The `InputHandler` class includes methods
for obtaining various types of input from the user, such as strings, integers, floats, single characters,
and input from a predefined list. It also supports input validation based on custom conditions.
"""
import logging

logger = logging.getLogger(__name__)

class InputHandler:
    """
    A class that handles user input.

    Attributes:
        input_data (str): The user's input data.

    Methods:
        get_str_input: Get a string input from the user.
        get_int_input: Get an integer input from the user.
        get_float_input: Get a float input from the user.
        get_one_char_input: Get a single character input from the user.
        get_one_of_list_input: Get an input from the user that must be one of the specified list items.
        get_one_of_list_input_ignore_case: Get an input from the user that must be one of the specified 
        list items, ignoring case.
        check_input_in_list_ignore_case: Check if the input is in the list, ignoring case.
        check_input_in_list: Check if the input is in the list.
        get_input_with_condition: Get an input from the user that satisfies the specified condition.
    """

    def __init__(self):
        """
        Initializes the InputHandler object.
        """
        self.input_data = None

    def get_str_input(self, message):
        """
        Get a string input from the user.

        Args:
            message (str): The message to display to the user.

        Returns:
            str: The user's input as a string.
        """
        input_data = input(f"{message}: ")
        self.input_data = input_data
        return input_data
    
    def get_int_input(self, message):
        """
        Get an integer input from the user.

        Args:
            message (str): The message to display to the user.

        Returns:
            int: The user's input as an integer.
        """
        input_data = input(f"{message}: ")
        while not input_data.isdigit():
            logger.warning("The input %s is not a number.", input_data)
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return int(input_data)
    
    def get_float_input(self, message):
        """
        Get a float input from the user.

        Args:
            message (str): The message to display to the user.

        Returns:
            float: The user's input as a float.
        """
        input_data = input(f"{message}: ")
        while not input_data.replace('.', '', 1).isdigit():
            logger.warning("The input %s is not a float number.", input_data)
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return float(input_data)
    
    def get_one_char_input(self, message):
        """
        Get a single character input from the user.

        Args:
            message (str): The message to display to the user.

        Returns:
            str: The user's input as a single character.
        """
        input_data = input(f"{message}: ")
        while len(input_data) != 1:
            logger.warning("The input %s is not one character.", input_data)
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return input_data
    
    def get_one_of_list_input(self, message, check_list):
        """
        Get an input from the user that must be one of the specified list items.

        Args:
            message (str): The message to display to the user.
            list (list): The list of valid input options.

        Returns:
            str: The user's input as one of the list items.
        """
        input_data = input(f"{message}: ")
        while not self.check_input_in_list(input_data, check_list):
            logger.warning("The input %s is not in the list.", input_data)
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return input_data
    
    def get_one_of_list_input_ignore_case(self, message, check_list):
        """
        Get an input from the user that must be one of the specified list items, ignoring case.

        Args:
            message (str): The message to display to the user.
            list (list): The list of valid input options.

        Returns:
            str: The user's input as one of the list items.
        """
        input_data = input(f"{message}: ")
        while not self.check_input_in_list_ignore_case(input_data, check_list):
            logger.warning("The input %s is not in the list.", input_data)
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return input_data
    
    def check_input_in_list_ignore_case(self, input_data, check_list):
        """
        Check if the input is in the list, ignoring case.

        Args:
            input_data (str): The input to check.
            list (list): The list of valid input options.

        Returns:
            bool: True if the input is in the list, False otherwise.
        """
        input_data = input_data.lower()
        for item in check_list:
            if input_data == item.lower():
                return True
        return False
    
    def check_input_in_list(self, input_data, check_list):   
        """
        Check if the input is in the list.

        Args:
            input_data (str): The input to check.
            list (list): The list of valid input options.

        Returns:
            bool: True if the input is in the list, False otherwise.
        """
        if input_data in check_list:
            return True
        return False
    
    def get_input_with_condition(self, message, condition):
        """
        Get an input from the user that satisfies the specified condition.

        Args:
            message (str): The message to display to the user.
            condition (function): The condition that the input must satisfy.

        Returns:
            str: The user's input that satisfies the condition.
        """
        input_data = input(f"{message}: ")
        while not condition(input_data):
            input_data = input(f"{message}: ")
        self.input_data = input_data
        return input_data
