#!/usr/bin/python3

"""test for rectangle"""

import unittest
from models.rectangle import Rectangle


class TestforRectangle(unittest.TestCase):
    """test for rectangle"""

    def test_id(self):
        r11 = Rectangle(10, 2)
        self.assertEqual(r11.id, 1)

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

        r5 = Rectangle(10, 2, 9, 5)
        r5.width = 6
        self.assertEqual(r5.width, 6)

        with self.assertRaises(TypeError):
            r3 = Rectangle()

    def test_height(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)

        r5 = Rectangle(10, 2, 9, 5)
        r5.height = 6
        self.assertEqual(r5.height, 6)

        with self.assertRaises(TypeError):
            r3 = Rectangle()

    def test_x(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)

        r2 = Rectangle(10, 2, 5)
        self.assertEqual(r2.x, 5)

        r5 = Rectangle(10, 2, 9, 5)
        r5.x = 6
        self.assertEqual(r5.x, 6)

    def test_y(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(10, 2, 5, 6)
        self.assertEqual(r2.y, 6)

        r5 = Rectangle(10, 2, 9, 5)
        r5.y = 6
        self.assertEqual(r5.y, 6)


class TestRaisedexceptions(unittest.TestCase):
    """test for raised exceptions"""

    def test_widthTypeerror(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hello", 2, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({}, 2, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 5, 6], 2, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 3, 5, 7}, 2, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"1": 1, "2": 2, "3": 3}, 2, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 4), 2, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 2, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([], 2, 4)

        r = Rectangle(2, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = "hello"

    def test_widthvalueError(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2, 4)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2, 4)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1.5, 2, 4)

        r = Rectangle(1, 2, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -1

    def test_heightTypeerror(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None, 4)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "hello", 4)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {}, 4)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [1, 2, 5, 6], 4)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1, 3, 5, 7}, 4)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"1": 1, "2": 2, "3": 3}, 4)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (1, 2, 4), 4)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 2.5, 4)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [], 4)

        r = Rectangle(2, 4, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.height = "hello"

    def test_heightvalueError(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0, 4)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2, 4)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1.2, 4)

        r = Rectangle(1, 2, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = -1

    def test_xTypeerror(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, None)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, "hello")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, {})

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, [1, 2, 5, 6])

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, {1, 3, 5, 7})

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, {"1": 1, "2": 2, "3": 3}, 4)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, (1, 2, 4), 4)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, 2.5, 4)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, [], 4)

        r = Rectangle(2, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = "hello"

    def test_xvalueError(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 4, -2, 4)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 4, -1.2, 4)

        r = Rectangle(1, 4, 1, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.x = -1

    def test_yTypeerror(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 4, None)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 4, "hello")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 4, {})

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 4, [1, 2, 5, 6])

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, {1, 3, 5, 7})

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 4, {"1": 1, "2": 2, "3": 3})

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, (1, 2, 4))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 4,  2.5, 4)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 4, [])

        r = Rectangle(2, 4, 4, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.y = "hello"

    def test_yvalueError(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 4, 4, -2)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 4, 2, -1.4)

        r = Rectangle(1, 4, 1.2, 4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.y = -1

class TestArea(unittest.TestCase):
    """Test for arear"""

    def test_twoArguements(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

    def test_allArguements(self):
        r1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 56)


    def test_threerguements(self):
        r1 = Rectangle(8, 7, 0)
        self.assertEqual(r1.area(), 56)


    def test_FourArguements(self):
        r1 = Rectangle(8, 7, 0, 0)
        self.assertEqual(r1.area(), 56)


class Testdisplay(unittest.TestCase):
    """tests display"""
    def test_dispaly(self):
        output1 = f"##\n##"

        r2 = Rectangle(2, 2)
        self.assertEqual(r2.display(), output1)

        output2 = f"

        ##\n  ##\n  ##"
        r3 = Rectangle(2, 3, 2, 2)
        self.assertEqual(r3.display(), output2)

        output3 = " ###\n ###"
        r4 = Rectangle(3, 2, 1, 0)
        self.assertEqual(r4.display(), output3)

class Teststr(unittest.TestCase):
    """test for str"""

    def test_str(self):
        output1 = "[Rectangle] (12) 2/1 - 4/6"
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1, output1)

        output2 = "[Rectangle] (1) 1/0 - 5/5"
        r2 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r2, output2)

class Testupdate(unittest.TestCase):
        def test_update(self):
            
            output1 = "[Rectangle] (10) 10/10 - 10/10"
            r1 = Rectangle(10, 10, 10, 10)
            self.assertEqual(r1, output1)

            output1 = "[Rectangle] (89) 10/10 - 10/10"
            r1.update(89)
            self.assertEqual(r1, output1)

            output1 = "[Rectangle] (89) 10/10 - 2/10"
            r1.update(89, 2)
            self.assertEqual(r1, output1)

            output1 = "[Rectangle] (89) 10/10 - 2/3"
            r1.update(89, 2, 3)
            self.assertEqual(r1, output1)

            output1 = "[Rectangle] (89) 4/10 - 2/3"
            r1.update(89, 2, 3, 4)
            self.assertEqual(r1, output1)

            output1 = "[Rectangle] (89) 4/5 - 2/3"
            r1.update(89, 2, 3, 4, 5)
            self.assertEqual(r1, output1)

if __name__ == "__main__":
    unittest.main()
