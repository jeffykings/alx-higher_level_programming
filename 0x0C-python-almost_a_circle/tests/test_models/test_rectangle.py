#!/usr/bin/python3

"""test for rectangle"""

import unittest
from models.rectangle import Rectangle


class TestforRectangle(unittest.TestCase):
    """test for rectangle"""

    def test_id(self):
        r5 = Rectangle(10, 2)
        self.assertEqual(r5.id, 1)

        r2 = Rectangle(2, 2)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(10, 2, 0, 0, None)
        self.asserEqual(r4.id, 3)

        r5 = Rectangle(10, 2)
        r5.id = 14
        self.asserEqual(r5.id, 14)

    def test_width(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

        r4 = Rectangle(-10, 2)
        self.assertEqual(r4.width, -10)

        r2 = Rectangle(None, 2)
        self.assertEqual(r2.width, None)

        with self.assertRaises(TypeError):
            r3 = Rectangle()

        r5 = Rectangle(10, 2, 9, -5)
        r5.width = 6
        self.assertEqual(r5.width, 6)

    def test_height(self):

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(10, -2)
        self.assertEqual(r2.height, -2)

        r4 = Rectangle(-10, None)
        self.assertEqual(r4.height, None)

        with self.assertRaises(TypeError):
            r3 = Rectangle()

        r5 = Rectangle(10, 2, 9, -5)
        r5.height = 6
        self.assertEqual(r5.height, 6)

    def test_x(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)

        r2 = Rectangle(10, 2, 5)
        self.assertEqual(r2.x, 5)

        r4 = Rectangle(-10, 3, None)
        self.assertEqual(r4.x, None)

        r3 = Rectangle(10, 2, -5)
        self.assertEqual(r3.x, -5)

        r5 = Rectangle(10, 2, 9, -5)
        r5.x = 6
        self.assertEqual(r5.x, 6)

    def test_y(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(10, 2, 5, 6)
        self.assertEqual(r2.y, 6)

        r4 = Rectangle(-10, 3, 9, None)
        self.assertEqual(r4.y, None)

        r3 = Rectangle(10, 2, 9, -5)
        self.assertEqual(r3.y, -5)

        r5 = Rectangle(10, 2, 9, -5)
        r5.y = 6
        self.assertEqual(r5.y, 6)

if __name__ == "__main__":
    unittest.main()
