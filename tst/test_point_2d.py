"""
Module containing the unittests for the Point2D class
"""
import unittest

from src.point_2d import Point2D


class TestsPoint2D(unittest.TestCase):
    """
    Test cases for the Point2D class
    """
    def test_01_properties(self):
        """
        Verify that the properties are working
        """
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
        """
        Verify that the setters are working
        """
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
        """
        Verify __str__ works
        """
        # Arrange
        x, y = (3, 5)
        out = Point2D(x, y)
        expected = f'({x}, {y})'

        # Act
        actual = str(out)

        # Assert
        self.assertEqual(expected, actual)

    def test_05_repr(self):
        """
        Verify __repr__ works
        """
        # Arrange
        x, y = (3, 5)
        out = Point2D(x, y)
        expected = f'Point2D({x}, {y})'

        # Act
        actual = repr(out)

        # Assert
        self.assertEqual(expected, actual)

    def test_06_hash(self):
        """
        Verify hash() works
        """
        # Arrange
        out = Point2D(3, 5)

        # Act
        hash(out)

        # Nothing to assert - hash() should pass

    def test_07_eq(self):
        """
        Verify __eq__ works as expected
        """
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
        """
        Verify `+` works correctly
        """
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
        """
        Verify `-` works correctly
        """
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
        """
        Verify `*` works correctly
        """
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
        """
        Verify `//` works correctly
        """
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
        """
        Verify that distance calculations work correctly
        """
        # Arrange
        a = Point2D(0, 0)
        b = Point2D(3, 4)

        expected_distance = 5.0

        # Act
        actual_distance = a.distance_to(b)

        # Assert
        self.assertAlmostEqual(expected_distance, actual_distance)

    def test_13_within_upper_bound(self):
        """
        Verify the functionality of `is_within` with only a upper bound
        Each coordinate can have the following states:
            - outside lower bounds (1)
            - on lower bounds (2)
            - inside bounds (3)
            - on upper bounds (4)
            - outside upper bounds (5)

        However, if any of the coordinates is outside of left bounds
        or on the upper bound, the method should return False.

        This will lower the amount of tests to the following:
        (1, y) => False
        (2, 2) => True
        (2, 3) => True
        (3, 2) => True
        (3, 3) => True
        (4, y) => False
        (5, y) => False
        (x, 1) => False
        (x, 4) => False
        (x, 5) => False
        """

        # Arrange
        upper_bounds = Point2D(4, 5)
        random_x = 3
        random_y = 3

        x_outside_left = Point2D(-1, random_y)
        x_and_y_on_left = Point2D(0, 0)
        x_on_left_y_inside = Point2D(0, 4)
        x_inside_y_on_left = Point2D(3, 0)
        x_and_y_inside = Point2D(3, 4)
        x_on_right = Point2D(4, random_y)
        x_outside_right = Point2D(5, random_y)

        y_outside_left = Point2D(random_x, -1)
        y_on_right = Point2D(random_x, 5)
        y_outside_right = Point2D(random_x, 6)

        # Act
        is_x_outside_left_within = x_outside_left.is_within(upper_bounds)
        is_x_and_y_on_left_within = x_and_y_on_left.is_within(upper_bounds)
        is_x_on_left_y_inside_within = x_on_left_y_inside.is_within(upper_bounds)
        is_x_inside_y_on_left_within = x_inside_y_on_left.is_within(upper_bounds)
        is_x_and_y_inside_within = x_and_y_inside.is_within(upper_bounds)
        is_x_on_right_within = x_on_right.is_within(upper_bounds)
        is_x_outside_right_within = x_outside_right.is_within(upper_bounds)

        is_y_outside_left_within = y_outside_left.is_within(upper_bounds)
        is_y_on_right_within = y_on_right.is_within(upper_bounds)
        is_y_outside_right_within = y_outside_right.is_within(upper_bounds)

        # Assert
        self.assertFalse(is_x_outside_left_within)
        self.assertTrue(is_x_and_y_on_left_within)
        self.assertTrue(is_x_on_left_y_inside_within)
        self.assertTrue(is_x_inside_y_on_left_within)
        self.assertTrue(is_x_and_y_inside_within)
        self.assertFalse(is_x_on_right_within)
        self.assertFalse(is_x_outside_right_within)

        self.assertFalse(is_y_outside_left_within)
        self.assertFalse(is_y_on_right_within)
        self.assertFalse(is_y_outside_right_within)

    def test_14_within_upper_bound(self):
        """
        Verify the functionality of `is_within` with lower and upper bound
        Each coordinate can have the following states:
            - outside lower bounds (1)
            - on lower bounds (2)
            - inside bounds (3)
            - on upper bounds (4)
            - outside upper bounds (5)

        However, if any of the coordinates is outside of left bounds
        or on the upper bound, the method should return False.

        This will lower the amount of tests to the following:
        (1, y) => False
        (2, 2) => True
        (2, 3) => True
        (3, 2) => True
        (3, 3) => True
        (4, y) => False
        (5, y) => False
        (x, 1) => False
        (x, 4) => False
        (x, 5) => False
        """

        # Arrange
        upper_bounds = Point2D(4, 5)
        lower_bounds = Point2D(1, 2)
        random_x = 3
        random_y = 3

        x_outside_left = Point2D(-1, random_y)
        x_and_y_on_left = Point2D(1, 2)
        x_on_left_y_inside = Point2D(1, 4)
        x_inside_y_on_left = Point2D(3, 2)
        x_and_y_inside = Point2D(3, 4)
        x_on_right = Point2D(4, random_y)
        x_outside_right = Point2D(5, random_y)

        y_outside_left = Point2D(random_x, -1)
        y_on_right = Point2D(random_x, 5)
        y_outside_right = Point2D(random_x, 6)

        # Act
        is_x_outside_left_within = x_outside_left.is_within(upper_bounds, lower_bounds)
        is_x_and_y_on_left_within = x_and_y_on_left.is_within(upper_bounds, lower_bounds)
        is_x_on_left_y_inside_within = x_on_left_y_inside.is_within(upper_bounds, lower_bounds)
        is_x_inside_y_on_left_within = x_inside_y_on_left.is_within(upper_bounds, lower_bounds)
        is_x_and_y_inside_within = x_and_y_inside.is_within(upper_bounds, lower_bounds)
        is_x_on_right_within = x_on_right.is_within(upper_bounds, lower_bounds)
        is_x_outside_right_within = x_outside_right.is_within(upper_bounds, lower_bounds)

        is_y_outside_left_within = y_outside_left.is_within(upper_bounds, lower_bounds)
        is_y_on_right_within = y_on_right.is_within(upper_bounds, lower_bounds)
        is_y_outside_right_within = y_outside_right.is_within(upper_bounds, lower_bounds)

        # Assert
        self.assertFalse(is_x_outside_left_within)
        self.assertTrue(is_x_and_y_on_left_within)
        self.assertTrue(is_x_on_left_y_inside_within)
        self.assertTrue(is_x_inside_y_on_left_within)
        self.assertTrue(is_x_and_y_inside_within)
        self.assertFalse(is_x_on_right_within)
        self.assertFalse(is_x_outside_right_within)

        self.assertFalse(is_y_outside_left_within)
        self.assertFalse(is_y_on_right_within)
        self.assertFalse(is_y_outside_right_within)
