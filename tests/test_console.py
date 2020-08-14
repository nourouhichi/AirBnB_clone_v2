import console
import unittest
HBNBCommand = console.HBNBCommand


class TestConsole(unittest.TestCase):
    """" testing console docs"""
    def test_docstring(self):
        """docstring validation test"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")