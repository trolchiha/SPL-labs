import unittest
from UI.menu import Menu
from UI.menu_item import Item
from .settings import TEST_DIR

def lab_menu():
    menu = Menu("\nMenu (Lab 6)")
    menu.add_item(Item("1", "Run Tests", run_tests))
    menu.add_item(Item("0", "Exit"))
    menu.run()

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=TEST_DIR, pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("All tests passed.")
    else:
        print("Some tests failed.")

