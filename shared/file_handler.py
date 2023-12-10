"""
File_handler module
"""
import os
import logging

logger = logging.getLogger(__name__)

class FileHandler:
    """
    A class for handling file operations.
    """

    def __init__(self, file_name):
        """
        Initializes a FileHandler object.

        Args:
            file_name (str): The name of the file to be handled.
        """
        self.file_name = file_name

    def write_to_file(self, data):
        """
        Writes data to the file.

        Args:
            data (str): The data to be written to the file.
        """
        try:
            with open(self.file_name, "w", encoding='utf-8') as file:
                file.write(data)
            print(f"Data has been written to {self.file_name}")
        except Exception as exception:
            print(f"Error writing to {self.file_name}: {exception}")
            logger.error("An error occurred: %s", str(exception), exc_info=True)

    def append_to_file(self, data):
        """
        Appends data to the file.

        Args:
            data (str): The data to be appended to the file.
        """
        try:
            with open(self.file_name, "a", encoding='utf-8') as file:
                file.write(data)
        except Exception as exception:
            print(f"Error writing to {self.file_name}: {exception}")
            logger.error("An error occurred: %s", str(exception), exc_info=True)

    def read_from_file(self):
        """
        Reads data from the file.

        Returns:
            str: The data read from the file.
        """
        try:
            with open(self.file_name, "r", encoding='utf-8') as file:
                data = file.read()
                print(f"Data read from {self.file_name}:")
                print(data)
                return data
        except FileNotFoundError as exception:
            print(f"The file {self.file_name} does not exist.")
            logger.error("An error occurred: %s", str(exception), exc_info=True)
        except Exception as exception:
            print(f"Error reading from {self.file_name}: {exception}")
            logger.error("An error occurred: %s", str(exception), exc_info=True)

    def delete_file(self):
        """
        Deletes the file if it exists.
        """
        if os.path.exists(self.file_name):
            try:
                os.remove(self.file_name)
                print(f"The file {self.file_name} has been deleted.")
            except Exception as exception:
                print(f"Error deleting {self.file_name}: {exception}")
                logger.error("An error occurred: %s", str(exception), exc_info=True)
        else:
            print(f"The file {self.file_name} does not exist or has already been deleted.")
            logger.warning("The file %s does not exist.", self.file_name)
