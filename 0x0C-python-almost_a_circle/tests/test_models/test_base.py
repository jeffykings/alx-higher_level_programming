#!/usr/bin/python3

"""test for base class"""
import unittest
from models.base import Base


class TestforBaseClass(unittest.TestCase):
    """ testing the base class"""

    def test_NoArguement(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_ArguementNone(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 1)

    def test_ArguementNone(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_Arguementstr(self):
        b1 = Base("jk7")
        self.assertEqual(b1.id, "jk7")


if __name__ == ' __main__':
    unittest.main()
