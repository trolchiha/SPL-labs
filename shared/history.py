class History:
    def __init__(self, file_name):
        self.file_name = file_name

    def add_event(self, event):
        with open(self.file_name, 'a') as file:
            file.write(event + '\n')

    def get_history(self):
        with open(self.file_name, 'r') as file:
            return file.readlines()

    def clear_history(self):
        with open(self.file_name, 'w') as file:
            file.truncate()
