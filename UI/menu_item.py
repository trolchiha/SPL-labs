class Item:
    def __init__(self, id, name, function, args=None):
        self.id = id
        self.name = name
        self.function = function
        self.args = args

    def __str__(self):
        return f"{self.id} - {self.name}"