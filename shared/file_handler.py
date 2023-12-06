import os
import logging

logger = logging.getLogger(__name__)

class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_file(self, data):
        try:
            with open(self.file_name, "w") as file:
                file.write(data)
            print(f"Data has been written to {self.file_name}")
        except Exception as e:
            print(f"Error writing to {self.file_name}: {e}")
            logger.error("An error occurred: %s", str(e), exc_info=True)


    def append_to_file(self, data):
        try:
            with open(self.file_name, "a") as file:
                file.write(data)
        except Exception as e:
            print(f"Error writing to {self.file_name}: {e}")
            logger.error("An error occurred: %s", str(e), exc_info=True)


    def read_from_file(self):
        try:
            with open(self.file_name, "r") as file:
                data = file.read()
                print(f"Data read from {self.file_name}:")
                print(data)
                return data
        except FileNotFoundError:
            print(f"The file {self.file_name} does not exist.")
            logger.error("An error occurred: %s", str(e), exc_info=True)
        except Exception as e:
            print(f"Error reading from {self.file_name}: {e}")
            logger.error("An error occurred: %s", str(e), exc_info=True)

    def delete_file(self):
        if os.path.exists(self.file_name):
            try:
                os.remove(self.file_name)
                print(f"The file {self.file_name} has been deleted.")
            except Exception as e:
                print(f"Error deleting {self.file_name}: {e}")
                logger.error("An error occurred: %s", str(e), exc_info=True)
        else:
            print(f"The file {self.file_name} does not exist or has already been deleted.")
            logger.warning("The file %s does not exist.", self.file_name)


