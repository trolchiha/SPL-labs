from pathlib import Path

class History:
    def __init__(self, file_name):
        self.file_name = file_name

    def add_event(self, event):
        with open(self.file_name, 'a') as file:
            file.write(event + '\n')

    def print_history(self):
        path = Path(self.file_name)
        if path.exists():
            with open(self.file_name, 'r') as file:
                file_contents = file.read()
                print("\nHistory:")
                print(file_contents)
        else:
            print(f"The file '{self.file_name}' does not exist.")


    def clear_history(self):
        with open(self.file_name, 'w') as file:
            file.truncate()
        print("\nHistory cleared!")
        