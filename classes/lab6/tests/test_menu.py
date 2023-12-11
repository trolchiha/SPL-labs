import unittest
from UI.menu import Menu
from UI.menu_item import Item
from shared.settings import get_lab_settings

settings = get_lab_settings("lab6")
TEST_DIR = settings["test_dir"]

class TestMenu:
    def __init__(self):
        self.test_dir = TEST_DIR

    def menu(self):
        menu = Menu("\nTest Menu(Lab 6)")
        menu.add_item(Item("1", "Run Tests", self.run_tests))
        menu.add_item(Item("0", "Exit"))
        menu.run()

    def run_tests(self):
        """
        Run the unit tests for the project.

        Returns:
            None
        """
        loader = unittest.TestLoader()
        suite = loader.discover(start_dir=self.test_dir, pattern="test_*.py")
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)

        if result.wasSuccessful():
            print("All tests passed.")
        else:
            print("Some tests failed.")
