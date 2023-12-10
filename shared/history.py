"""
History module
"""
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class History:
    """
    A class that represents a history of events.

    Attributes:
        file_name (str): The name of the file to store the history.
    """

    def __init__(self, file_name):
        """
        Initialize a History object.

        Args:
            file_name (str): The name of the file to store the history.

        Returns:
            None
        """
        self.file_name = file_name

    def add_event(self, event):
        """
        Adds an event to the history.

        Args:
            event (str): The event to be added.
        """
        try:
            with open(self.file_name, 'a', encoding='utf-8') as file:
                file.write(event + '\n')
        except Exception as exception:
            print(f"Error writing to {self.file_name}: {exception}")
            logger.error("An error occurred: %s", str(exception), exc_info=True)

    def print_history(self):
        """
        Prints the contents of the history file.
        """
        try:
            path = Path(self.file_name)
            if path.exists():
                with open(self.file_name, 'r', encoding='utf-8') as file:
                    file_contents = file.read()
                    print("\nHistory:")
                    print(file_contents)
            else:
                print(f"The file '{self.file_name}' does not exist.")
        except Exception as exception:
            print(f"Error reading from {self.file_name}: {exception}")
            logger.error("An error occurred: %s", str(exception), exc_info=True)

    def clear_history(self):
        """
        Clears the history file.
        """
        try:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                file.truncate()
            print("\nHistory cleared!")
        except Exception as exception:
            print(f"Error writing to {self.file_name}: {exception}")
            logger.error("An error occurred: %s", str(exception), exc_info=True)
        