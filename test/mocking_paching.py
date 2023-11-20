import time
import unittest
from unittest.mock import patch


class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def perimeter(self):
        time.sleep(2)
        return 2 * self.l + 2 * self.w

    def area(self):
        time.sleep(2)
        return self.w * self.l

    def display(self):
        return [self.l, self.w, self.perimeter(), self.area()]


class Test(unittest.TestCase):
    @patch('test_func.Rectangle.area')
    @patch('test_func.Rectangle.perimeter')
    def test_function(self, mock_perimeter, mock_area):
        mock_perimeter.return_value = 10
        mock_area.return_value = 6
        my_obj = Rectangle(3, 2)
        result = my_obj.display()
        self.assertEqual(result, [3, 2, 10, 6])


if __name__ == '__main__':
    unittest.main()
