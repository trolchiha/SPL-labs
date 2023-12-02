import unittest

test_dir = "data/lab6/tests"

def __main__():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=test_dir, pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("All tests passed.")
    else:
        print("Some tests failed.")

if __name__ == '__main__':
    __main__()
