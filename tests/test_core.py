# tests/test_core.py

import unittest
from mypackage import my_function

class TestMyFunction(unittest.TestCase):

    def test_greeting(self):
        self.assertEqual(my_function("World"), "Hello, World!")
        
if __name__ == "__main__":
    unittest.main()
