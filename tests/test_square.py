import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_area(self):
        side = 6
        expected_area = 36
        actual_area = area(side)
        self.assertEqual(actual_area, expected_area)

    def test_perimeter(self):
        side = 6
        expected_perimeter = 24
        actual_perimeter = perimeter(side)
        self.assertEqual(actual_perimeter, expected_perimeter)


if __name__ == "__main__":
    unittest.main()
