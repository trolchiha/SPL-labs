from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class History:
    def __init__(self, file_name):
        self.file_name = file_name

    def add_event(self, event):
        try:
            with open(self.file_name, 'a') as file:
                file.write(event + '\n')
        except FileNotFoundError:
            print(f"The file '{self.file_name}' does not exist.")
            logger.error("An error occurred: %s", str(e), exc_info=True)
        except Exception as e:
            print(f"An error occurred while writing to the file '{self.file_name}'.")
            logger.error("An error occurred: %s", str(e), exc_info=True)
            

    def print_history(self):
        try:
            path = Path(self.file_name)
            if path.exists():
                with open(self.file_name, 'r') as file:
                    file_contents = file.read()
                    print("\nHistory:")
                    print(file_contents)
            else:
                print(f"The file '{self.file_name}' does not exist.")
        except Exception as e:
            print(f"An error occurred while reading from the file '{self.file_name}'.")
            logger.error("An error occurred: %s", str(e), exc_info=True)


    def clear_history(self):
        try:
            with open(self.file_name, 'w') as file:
                file.truncate()
                print("\nHistory cleared!")
        except FileNotFoundError:
            print(f"The file '{self.file_name}' does not exist.")
            logger.error("An error occurred: %s", str(e), exc_info=True)
        except Exception as e:
            print(f"An error occurred while clearing the file '{self.file_name}'.")
            logger.error("An error occurred: %s", str(e), exc_info=True)
        