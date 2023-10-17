class Item:
    def __init__(self, name, function, parent=None):
        self.name = name
        self.function = function
        self.parent = parent
        if parent:
            parent.add_item(self) # use add_item instead of append, since who
                                  # knows what kind of complex code you'll have
                                  # in add_item() later on.

    def draw(self):
        # might be more complex later, better use a method.
        print("    " + self.name)