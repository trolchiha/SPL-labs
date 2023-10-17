class Menu:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.option = None

    def add_item(self, item):
        self.items.append(item)

    def print_menu(self):
        print(f"{self.name}:")
        for item in self.items:
            print(item)

    def set_menu_option(self):
        self.option = input("Enter your choice: ")
        
        
    def run_function(self, option):
        for item in self.items:
            if item.id == option:
                item.function()
                break

    def run(self):
        while True:
            self.print_menu()
            self.set_menu_option()
            self.run_function(self.option)
        
    