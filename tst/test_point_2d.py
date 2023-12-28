import unittest

from src.point_2d import Point2D


class TestsPoint2D(unittest.TestCase):
    def test_01_properties(self):
        # Arrange
        expected_x = 3
        expected_y = 5
        out = Point2D(3, 5)

        # Act
        actual_x = out.x
        actual_y = out.y

        # Assert
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_02_setters(self):
        # Arrange
        out = Point2D(3, 5)
        expected_x = 4
        expected_y = 6

        # Act
        out.x = expected_x
        out.y = expected_y

        actual_x = out.x
        actual_y = out.y

        # Assert
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_04_str(self):
        # Arrange
        x, y = (3, 5)
        out = Point2D(x, y)
        expected = f'({x}, {y})'

        # Act
        actual = str(out)

        # Assert
        self.assertEqual(expected, actual)

    def test_05_repr(self):
        # Arrange
        x, y = (3, 5)
        out = Point2D(x, y)
        expected = f'Point2D({x}, {y})'

        # Act
        actual = repr(out)

        # Assert
        self.assertEqual(expected, actual)

    def test_06_hash(self):
        # Arrange
        out = Point2D(3, 5)

        # Act
        hash(out)

        # Nothing to assert - hash() should pass

    def test_07_eq(self):
        # Arrange
        p1 = Point2D(3, 4)
        p2 = Point2D(4, 5)
        p3 = Point2D(3, 5)
        p4 = Point2D(3, 4)

        # Act
        is_p1_p2_equal = p1 == p2
        is_p1_p3_equal = p1 == p3
        is_p1_p4_equal = p1 == p4
        is_p1_p1_equal = p1 == p1

        # Assert
        self.assertFalse(is_p1_p2_equal)
        self.assertFalse(is_p1_p3_equal)
        self.assertTrue(is_p1_p4_equal)
        self.assertTrue(is_p1_p1_equal)

    def test_08_add(self):
        # Arrange
        x1, y1 = (3, 5)
        x2, y2 = (4, 6)

        p1 = Point2D(x1, y1)
        p2 = Point2D(x2, y2)

        expected_x = x1 + x2
        expected_y = y1 + y2

        expected_point = Point2D(expected_x, expected_y)

        # Act
        actual_point = p1 + p2

        # Assert
        self.assertEqual(expected_point, actual_point)

    def test_09_sub(self):
        # Arrange
        x1, y1 = (3, 5)
        x2, y2 = (4, 6)

        p1 = Point2D(x1, y1)
        p2 = Point2D(x2, y2)

        expected_x = x1 - x2
        expected_y = y1 - y2

        expected_point = Point2D(expected_x, expected_y)

        # Act
        actual_point = p1 - p2

        # Assert
        self.assertEqual(expected_point, actual_point)

    def test_10_mul(self):
        # Arrange
        x1, y1 = (3, 5)
        x2, y2 = (4, 6)

        p1 = Point2D(x1, y1)
        p2 = Point2D(x2, y2)

        expected_x = x1 * x2
        expected_y = y1 * y2

        expected_point = Point2D(expected_x, expected_y)

        # Act
        actual_point = p1 * p2

        # Assert
        self.assertEqual(expected_point, actual_point)

    def test_11_floordiv(self):
        # Arrange
        x1, y1 = (6, 12)
        x2, y2 = (4, 6)

        p1 = Point2D(x1, y1)
        p2 = Point2D(x2, y2)

        expected_x = x1 // x2
        expected_y = y1 // y2

        expected_point = Point2D(expected_x, expected_y)

        # Act
        actual_point = p1 // p2

        # Assert
        self.assertEqual(expected_point, actual_point)

    def test_12_distance(self):
        # Arrange
        a = Point2D(0, 0)
        b = Point2D(3, 4)

        expected_distance = 5.0

        # Act
        actual_distance = a.distance_to(b)

        # Assert
        self.assertAlmostEqual(expected_distance, actual_distance)
