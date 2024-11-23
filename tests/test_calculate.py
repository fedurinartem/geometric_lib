import unittest
from calculate import calc
import circle
import square


class TestCalc(unittest.TestCase):

    def test_circle_area(self):
        # Arrange
        radius = 5
        expected = circle.area(radius)

        # Act
        result = calc('circle', 'area', [radius])

        # Assert
        self.assertEqual(result, expected)

    def test_circle_perimeter(self):
        # Arrange
        radius = 5
        expected = circle.perimeter(radius)

        # Act
        result = calc('circle', 'perimeter', [radius])

        # Assert
        self.assertEqual(result, expected)

    def test_square_area(self):
        # Arrange
        side = 4
        expected = square.area(side)

        # Act
        result = calc('square', 'area', [side])

        # Assert
        self.assertEqual(result, expected)

    def test_square_perimeter(self):
        # Arrange
        side = 5
        expected = square.perimeter(side)

        # Act
        result = calc('square', 'perimeter', [side])

        # Assert
        self.assertEqual(result, expected)

    def test_invalid_figure(self):
        # Arrange
        invalid_figure = 'triangle'

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calc(invalid_figure, 'area', [3])

        self.assertEqual(
            str(context.exception),
            "Invalid figure: triangle. Available figures are: "
            "['circle', 'square']"
        )

    def test_invalid_function(self):
        # Arrange
        invalid_function = 'volume'

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calc('circle', invalid_function, [5])

        self.assertEqual(
            str(context.exception),
            "Invalid function: volume. Available functions are: "
            "['perimeter', 'area']"
        )

    def test_circle_negative_radius(self):
        # Arrange
        negative_radius = -5

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calc('circle', 'area', [negative_radius])

        self.assertEqual(
            str(context.exception),
            "Can't use negative values for figure dimensions."
        )

    def test_square_negative_side(self):
        # Arrange
        negative_side = -4

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calc('square', 'area', [negative_side])

        self.assertEqual(
            str(context.exception),
            "Can't use negative values for figure dimensions."
        )


if __name__ == '__main__':
    unittest.main()
