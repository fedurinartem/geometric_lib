import unittest
from calculate import calc
import square
import circle


class TestCalc(unittest.TestCase):
    def test_circle_area(self):
        radius = 5
        expected_area = circle.area(radius)
        result = calc("circle", "area", [radius])
        self.assertEqual(result, expected_area)

    def test_circle_perimeter(self):
        radius = 5
        expected_perimeter = circle.perimeter(radius)
        result = calc("circle", "perimeter", [radius])
        self.assertEqual(result, expected_perimeter)

    def test_square_area(self):
        side = 6
        expected_area = square.area(side)
        result = calc("square", "area", [side])
        self.assertEqual(result, expected_area)

    def test_square_perimeter(self):
        side = 6
        expected_perimeter = square.perimeter(side)
        result = calc("square", "perimeter", [side])
        self.assertEqual(result, expected_perimeter)

    def test_invalid_figure(self):
        invalid_figure = "triangle"
        with self.assertRaises(ValueError) as context:
            calc(invalid_figure, "area", [3])
        self.assertEqual(
            str(context.exception),
            "Invalid figure: triangle. Avaliable figures are: ['circle', 'square']",
        )

    def test_invalid_function(self):
        invalid_function = "volume"
        with self.assertRaises(ValueError) as context:
            calc("circle", invalid_function, [5])
        self.assertEqual(
            str(context.exception),
            "Invalid function: volume. Avaliable functions are: ['perimeter', 'area']",
        )

    def test_circle_negative(self):
        radius = -3
        with self.assertRaises(ValueError) as context:
            calc("circle", "area", [radius])
        self.assertEqual(
            str(context.exception), "Can't use negative values for figure dimensions."
        )

    def test_square_negative(self):
        side = -6
        with self.assertRaises(ValueError) as context:
            calc("square", "area", [side])
        self.assertEqual(
            str(context.exception), "Can't use negative values for figure dimensions."
        )


if __name__ == "__main__":
    unittest.main()
