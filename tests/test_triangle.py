import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_area(self):
        first_side = 5
        second_side = 6
        third_side = 4
        expected_area = 7.5
        actual_area = area(first_side, second_side, third_side)
        self.assertEqual(actual_area, expected_area)

    def test_perimeter(self):
        first_side = 12
        second_side = 10
        third_side = 7
        expected_perimeter = 29
        actual_perimeter = perimeter(first_side, second_side, third_side)
        self.assertEqual(actual_perimeter, expected_perimeter)


if __name__ == "__main__":
    unittest.main()
