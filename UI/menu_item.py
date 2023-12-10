"""
Represents a menu item.

"""
class Item:
    """
    Represents a menu item.

    Attributes:
        id (int): The ID of the item.
        name (str): The name of the item.
        function (function, optional): The function to be executed when the item is selected.
        args (list, optional): The arguments to be passed to the function.

    Methods:
        __str__(): Returns a string representation of the item.
    """
    def __init__(self, item_id, name, function=None, args=None):
        """
        Initialize a MenuItem object.

        Args:
            id (int): The ID of the menu item.
            name (str): The name of the menu item.
            function (callable, optional): The function to be executed when the menu item is selected.
            args (tuple, optional): The arguments to be passed to the function.

        """
        self.item_id = item_id
        self.name = name
        self.function = function
        self.args = args

    def __str__(self):
        """
        Returns a string representation of the menu item.
        
        The string representation includes the item's ID and name.
        
        Returns:
            str: The string representation of the menu item.
        """
        return f"{self.item_id} - {self.name}"
    