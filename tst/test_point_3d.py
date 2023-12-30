"""
Module containing the unittests for the Point3D class
"""
import unittest

from math import sqrt

from src.grid_points.point_3d import Point3D


class TestsPoint3D(unittest.TestCase):
    """
    Test cases for the Point3D class
    """
    def test_01_properties(self):
        """
        Verify that the properties are working
        """
        # Arrange
        expected_x = 3
        expected_y = 5
        expected_z = 6

        out = Point3D(3, 5, 6)

        # Act
        actual_x = out.x
        actual_y = out.y
        actual_z = out.z

        # Assert
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)
        self.assertEqual(expected_z, actual_z)

    def test_02_setters(self):
        """
        Verify that the setters are working
        """
        # Arrange
        out = Point3D(3, 5, 6)
        expected_x = 4
        expected_y = 6
        expected_z = 3

        # Act
        out.x = expected_x
        out.y = expected_y
        out.z = expected_z

        actual_x = out.x
        actual_y = out.y
        actual_z = out.z

        # Assert
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)
        self.assertEqual(expected_z, actual_z)

    def test_04_str(self):
        """
        Verify __str__ works
        """
        # Arrange
        x, y, z = (3, 5, 7)
        out = Point3D(x, y, z)
        expected = f'({x}, {y}, {z})'

        # Act
        actual = str(out)

        # Assert
        self.assertEqual(expected, actual)

    def test_05_repr(self):
        """
        Verify __repr__ works
        """
        # Arrange
        x, y, z = (3, 5, 7)
        out = Point3D(x, y, z)
        expected = f'Point3D({x}, {y}, {z})'

        # Act
        actual = repr(out)

        # Assert
        self.assertEqual(expected, actual)

    def test_06_hash(self):
        """
        Verify hash() works
        """
        # Arrange
        out = Point3D(3, 5, 7)

        # Act
        hash(out)

        # Nothing to assert - hash() should pass

    def test_07_eq(self):
        """
        Verify __eq__ works as expected
        """
        # Arrange
        p1 = Point3D(3, 4, 5)
        p2 = Point3D(4, 5, 6)  # F, F, F
        p3 = Point3D(3, 4, 4)  # T, T, F
        p4 = Point3D(3, 4, 5)  # T, T, T
        p5 = Point3D(3, 6, 5)  # T, F, T
        p6 = Point3D(4, 4, 5)  # F, T, T
        p7 = Point3D(4, 2, 5)  # F, F, T
        p8 = Point3D(3, -1, -2)  # T, F, F

        # Act
        is_p1_p2_equal = p1 == p2
        is_p1_p3_equal = p1 == p3
        is_p1_p4_equal = p1 == p4
        is_p1_p1_equal = p1 == p1
        is_p1_p5_equal = p1 == p5
        is_p1_p6_equal = p1 == p6
        is_p1_p7_equal = p1 == p7
        is_p1_p8_equal = p1 == p8

        # Assert
        self.assertFalse(is_p1_p2_equal)
        self.assertFalse(is_p1_p3_equal)
        self.assertTrue(is_p1_p4_equal)
        self.assertTrue(is_p1_p1_equal)
        self.assertFalse(is_p1_p5_equal)
        self.assertFalse(is_p1_p6_equal)
        self.assertFalse(is_p1_p7_equal)
        self.assertFalse(is_p1_p8_equal)

    def test_08_add(self):
        """
        Verify `+` works correctly
        """
        # Arrange
        x1, y1, z1 = (3, 5, 2)
        x2, y2, z2 = (4, 6, 1)

        p1 = Point3D(x1, y1, z1)
        p2 = Point3D(x2, y2, z2)

        expected_x = x1 + x2
        expected_y = y1 + y2
        expected_z = z1 + z2

        expected_point = Point3D(expected_x, expected_y, expected_z)

        # Act
        actual_point = p1 + p2

        # Assert
        self.assertEqual(expected_point, actual_point)

    def test_09_sub(self):
        """
        Verify `-` works correctly
        """
        # Arrange
        x1, y1, z1 = (3, 5, 2)
        x2, y2, z2 = (4, 6, 1)

        p1 = Point3D(x1, y1, z1)
        p2 = Point3D(x2, y2, z2)

        expected_x = x1 - x2
        expected_y = y1 - y2
        expected_z = z1 - z2

        expected_point = Point3D(expected_x, expected_y, expected_z)

        # Act
        actual_point = p1 - p2

        # Assert
        self.assertEqual(expected_point, actual_point)

    def test_10_mul(self):
        """
        Verify `*` works correctly
        """
        # Arrange
        x1, y1, z1 = (3, 5, 2)
        x2, y2, z2 = (4, 6, 3)

        p1 = Point3D(x1, y1, z1)
        p2 = Point3D(x2, y2, z2)

        expected_x = x1 * x2
        expected_y = y1 * y2
        expected_z = z1 * z2

        expected_point = Point3D(expected_x, expected_y, expected_z)

        # Act
        actual_point = p1 * p2

        # Assert
        self.assertEqual(expected_point, actual_point)

    def test_11_floordiv(self):
        """
        Verify `//` works correctly
        """
        # Arrange
        x1, y1, z1 = (6, 12, 4)
        x2, y2, z2 = (4, 6, 2)

        p1 = Point3D(x1, y1, z1)
        p2 = Point3D(x2, y2, z2)

        expected_x = x1 // x2
        expected_y = y1 // y2
        expected_z = z1 // z2

        expected_point = Point3D(expected_x, expected_y, expected_z)

        # Act
        actual_point = p1 // p2

        # Assert
        self.assertEqual(expected_point, actual_point)

    def test_12_distance(self):
        """
        Verify that distance calculations work correctly
        """
        # Arrange
        a = Point3D(0, 0, 0)
        b = Point3D(3, 4, 5)

        expected_distance = sqrt(50)

        # Act
        actual_distance = a.distance_to(b)

        # Assert
        self.assertAlmostEqual(expected_distance, actual_distance)

    # Verify the functionality of `is_within` with lower and upper bound
    # Each coordinate can have the following states:
    #     - outside lower bounds (1)
    #     - on lower bounds (2)
    #     - inside bounds (3)
    #     - on upper bounds (4)
    #     - outside upper bounds (5)

    # However, if any of the coordinates is outside of left bounds
    # or on the upper bound, the method should return False.

    # This will lower the amount of tests to the following:
    # (1, y, z) => False
    # (4, y, z) => False
    # (5, y, z) => False

    # (x, 1, z) => False
    # (x, 4, z) => False
    # (x, 5, z) => False

    # (x, y, 1) => False
    # (x, y, 4) => False
    # (x, y, 5) => False

    # (2, 2, 2) => True
    # (2, 2, 3) => True
    # (2, 3, 2) => True
    # (2, 3, 3) => True
    # (3, 2, 2) => True
    # (3, 2, 3) => True
    # (3, 3, 2) => True
    # (3, 3, 3) => True

    def test_13_within_upper_bound_x_outside(self):
        """
        Verify the functionality of `is_within` with only a upper bound
        when x is outside lower bounds, on upper and outside upper bounds
        """

        # Arrange
        upper_bounds = Point3D(4, 5, 6)
        random_y = 3
        random_z = 4

        x_outside_left = Point3D(-1, random_y, random_z)
        x_on_right = Point3D(4, random_y, random_z)
        x_outside_right = Point3D(5, random_y, random_z)

        # Act
        is_x_outside_left_within = x_outside_left.is_within(upper_bounds)
        is_x_on_right_within = x_on_right.is_within(upper_bounds)
        is_x_outside_right_within = x_outside_right.is_within(upper_bounds)

        # Assert
        self.assertFalse(is_x_outside_left_within)
        self.assertFalse(is_x_on_right_within)
        self.assertFalse(is_x_outside_right_within)

    def test_14_within_upper_bound_y_outside(self):
        """
        Verify the functionality of `is_within` with only a upper bound
        when y is outside lower bounds, on upper and outside upper bounds
        """

        # Arrange
        upper_bounds = Point3D(4, 5, 6)
        random_x = 3
        random_z = 4

        y_outside_left = Point3D(random_x, -1, random_z)
        y_on_right = Point3D(random_x, 5, random_z)
        y_outside_right = Point3D(random_x, 6, random_z)

        # Act
        is_y_outside_left_within = y_outside_left.is_within(upper_bounds)
        is_y_on_right_within = y_on_right.is_within(upper_bounds)
        is_y_outside_right_within = y_outside_right.is_within(upper_bounds)

        # Assert
        self.assertFalse(is_y_outside_left_within)
        self.assertFalse(is_y_on_right_within)
        self.assertFalse(is_y_outside_right_within)

    def test_15_within_upper_bound_z_outside(self):
        """
        Verify the functionality of `is_within` with only a upper bound
        when z is outside lower bounds, on upper and outside upper bounds
        """

        # Arrange
        upper_bounds = Point3D(4, 5, 6)
        random_x = 3
        random_y = 3

        z_outside_left = Point3D(random_x, random_y, -1)
        z_on_right = Point3D(random_x, random_y, 6)
        z_outside_right = Point3D(random_x, random_y, 7)

        # Act
        is_z_outside_left_within = z_outside_left.is_within(upper_bounds)
        is_z_on_right_within = z_on_right.is_within(upper_bounds)
        is_z_outside_right_within = z_outside_right.is_within(upper_bounds)

        # Assert
        self.assertFalse(is_z_outside_left_within)
        self.assertFalse(is_z_on_right_within)
        self.assertFalse(is_z_outside_right_within)

    def test_16_within_upper_bound_x_y_z_inside(self):
        """
        Verify the functionality of `is_within` with only a upper bound
        when all three coordinates are inside
        """

        # Arrange
        upper_bounds = Point3D(4, 5, 6)

        x_y_and_z_on_left = Point3D(0, 0, 0)
        x_and_y_on_left_z_inside = Point3D(0, 0, 2)

        x_on_left_y_inside_z_on_left = Point3D(0, 4, 0)
        x_on_left_y_inside_z_inside = Point3D(0, 4, 2)

        x_inside_y_and_z_on_left = Point3D(3, 0, 0)
        x_inside_y_on_left_z_inside = Point3D(3, 0, 2)

        x_and_y_inside_z_on_left = Point3D(3, 4, 0)
        x_y_and_z_inside = Point3D(3, 4, 2)

        # Act
        is_x_y_and_z_on_left_within = x_y_and_z_on_left.is_within(upper_bounds)
        is_x_and_y_on_left_z_inside_within = x_and_y_on_left_z_inside.is_within(upper_bounds)

        is_x_and_z_on_left_y_inside_within = x_on_left_y_inside_z_on_left.is_within(upper_bounds)
        is_x_on_left_y_inside_z_inside_within = x_on_left_y_inside_z_inside.is_within(upper_bounds)

        is_x_inside_y_and_z_on_left_within = x_inside_y_and_z_on_left.is_within(upper_bounds)
        is_x_inside_y_on_left_z_inside_within = x_inside_y_on_left_z_inside.is_within(upper_bounds)

        is_x_and_y_inside_z_on_left_within = x_and_y_inside_z_on_left.is_within(upper_bounds)
        is_x_y_and_z_inside_within = x_y_and_z_inside.is_within(upper_bounds)

        # Assert
        self.assertTrue(is_x_y_and_z_on_left_within)
        self.assertTrue(is_x_and_y_on_left_z_inside_within)

        self.assertTrue(is_x_and_z_on_left_y_inside_within)
        self.assertTrue(is_x_on_left_y_inside_z_inside_within)

        self.assertTrue(is_x_inside_y_and_z_on_left_within)
        self.assertTrue(is_x_inside_y_on_left_z_inside_within)

        self.assertTrue(is_x_and_y_inside_z_on_left_within)
        self.assertTrue(is_x_y_and_z_inside_within)

    def test_17_within_upper_lower_bounds_x_outside(self):
        """
        Verify the functionality of `is_within` with upper and lower bounds
        when x is outside lower bounds, on upper and outside upper bounds
        """

        # Arrange
        upper_bounds = Point3D(4, 5, 6)
        lower_bounds = Point3D(1, 2, 3)

        random_y = 3
        random_z = 4

        x_outside_left = Point3D(-1, random_y, random_z)
        x_on_right = Point3D(4, random_y, random_z)
        x_outside_right = Point3D(5, random_y, random_z)

        # Act
        is_x_outside_left_within = x_outside_left.is_within(upper_bounds, lower_bounds)
        is_x_on_right_within = x_on_right.is_within(upper_bounds, lower_bounds)
        is_x_outside_right_within = x_outside_right.is_within(upper_bounds, lower_bounds)

        # Assert
        self.assertFalse(is_x_outside_left_within)
        self.assertFalse(is_x_on_right_within)
        self.assertFalse(is_x_outside_right_within)

    def test_18_within_upper_lower_bounds_y_outside(self):
        """
        Verify the functionality of `is_within` with upper and lower bounds
        when y is outside lower bounds, on upper and outside upper bounds
        """

        # Arrange
        upper_bounds = Point3D(4, 5, 6)
        lower_bounds = Point3D(1, 2, 3)
        random_x = 3
        random_z = 4

        y_outside_left = Point3D(random_x, -1, random_z)
        y_on_right = Point3D(random_x, 5, random_z)
        y_outside_right = Point3D(random_x, 6, random_z)

        # Act
        is_y_outside_left_within = y_outside_left.is_within(upper_bounds, lower_bounds)
        is_y_on_right_within = y_on_right.is_within(upper_bounds, lower_bounds)
        is_y_outside_right_within = y_outside_right.is_within(upper_bounds, lower_bounds)

        # Assert
        self.assertFalse(is_y_outside_left_within)
        self.assertFalse(is_y_on_right_within)
        self.assertFalse(is_y_outside_right_within)

    def test_19_within_upper_lower_bounds_z_outside(self):
        """
        Verify the functionality of `is_within` with upper and lower bounds
        when z is outside lower bounds, on upper and outside upper bounds
        """

        # Arrange
        upper_bounds = Point3D(4, 5, 6)
        lower_bounds = Point3D(1, 2, 3)
        random_x = 3
        random_y = 3

        z_outside_left = Point3D(random_x, random_y, -1)
        z_on_right = Point3D(random_x, random_y, 6)
        z_outside_right = Point3D(random_x, random_y, 7)

        # Act
        is_z_outside_left_within = z_outside_left.is_within(upper_bounds, lower_bounds)
        is_z_on_right_within = z_on_right.is_within(upper_bounds, lower_bounds)
        is_z_outside_right_within = z_outside_right.is_within(upper_bounds, lower_bounds)

        # Assert
        self.assertFalse(is_z_outside_left_within)
        self.assertFalse(is_z_on_right_within)
        self.assertFalse(is_z_outside_right_within)

    def test_20_within_upper_lower_bounds_x_y_z_inside(self):
        """
        Verify the functionality of `is_within` with only a upper bound
        when all three coordinates are inside
        """
        # Arrange
        upper_bounds = Point3D(4, 5, 6)
        lower_bounds = Point3D(1, 2, 3)

        x_y_and_z_on_left = Point3D(1, 2, 3)
        x_and_y_on_left_z_inside = Point3D(1, 2, 5)

        x_on_left_y_inside_z_on_left = Point3D(1, 4, 3)
        x_on_left_y_inside_z_inside = Point3D(1, 4, 4)

        x_inside_y_and_z_on_left = Point3D(3, 2, 3)
        x_inside_y_on_left_z_inside = Point3D(3, 2, 4)

        x_and_y_inside_z_on_left = Point3D(3, 4, 3)
        x_y_and_z_inside = Point3D(3, 4, 4)

        # Act
        is_x_y_and_z_on_left_within = x_y_and_z_on_left.is_within(upper_bounds, lower_bounds)
        is_x_and_y_on_left_z_inside_within = x_and_y_on_left_z_inside.is_within(upper_bounds,
                                                                                lower_bounds)

        is_x_and_z_on_left_y_inside_within = x_on_left_y_inside_z_on_left.is_within(upper_bounds,
                                                                                    lower_bounds)
        is_x_on_left_y_inside_z_inside_within = x_on_left_y_inside_z_inside.is_within(upper_bounds,
                                                                                      lower_bounds)

        is_x_inside_y_and_z_on_left_within = x_inside_y_and_z_on_left.is_within(upper_bounds,
                                                                                lower_bounds)
        is_x_inside_y_on_left_z_inside_within = x_inside_y_on_left_z_inside.is_within(upper_bounds,
                                                                                      lower_bounds)

        is_x_and_y_inside_z_on_left_within = x_and_y_inside_z_on_left.is_within(upper_bounds,
                                                                                lower_bounds)
        is_x_y_and_z_inside_within = x_y_and_z_inside.is_within(upper_bounds, lower_bounds)

        # Assert
        self.assertTrue(is_x_y_and_z_on_left_within)
        self.assertTrue(is_x_and_y_on_left_z_inside_within)

        self.assertTrue(is_x_and_z_on_left_y_inside_within)
        self.assertTrue(is_x_on_left_y_inside_z_inside_within)

        self.assertTrue(is_x_inside_y_and_z_on_left_within)
        self.assertTrue(is_x_inside_y_on_left_z_inside_within)

        self.assertTrue(is_x_and_y_inside_z_on_left_within)
        self.assertTrue(is_x_y_and_z_inside_within)

    def test_21_lt(self):
        """
        Verify `<=` works properly
        """
        # Arrange
        a = Point3D(3, 5, 2)
        b = Point3D(4, 6, 3)  # T, T, T
        c = Point3D(4, 6, 1)  # T, T, F
        d = Point3D(4, 4, 4)  # T, F, ?
        e = Point3D(2, 4, 1)  # F, ?, ?

        # Act
        is_a_lt_b = a < b
        is_a_lt_c = a < c
        is_a_lt_d = a < d
        is_a_lt_e = a < e

        # Assert
        self.assertTrue(is_a_lt_b)
        self.assertFalse(is_a_lt_c)
        self.assertFalse(is_a_lt_d)
        self.assertFalse(is_a_lt_e)

    def test_22_le(self):
        """
        Verify `<=` works properly
        """
        # Arrange
        a = Point3D(3, 5, 4)
        b = Point3D(3, 6, 4)  # T, T, T
        c = Point3D(3, 4, 3)  # T, T, F
        d = Point3D(4, 4, 4)  # T, F, ?
        e = Point3D(2, 4, 7)  # F, ?, ?

        # Act
        is_a_le_b = a <= b
        is_a_le_c = a <= c
        is_a_le_d = a <= d
        is_a_le_e = a <= e

        # Assert
        self.assertTrue(is_a_le_b)
        self.assertFalse(is_a_le_c)
        self.assertFalse(is_a_le_d)
        self.assertFalse(is_a_le_e)

    def test_23_gt(self):
        """
        Verify `>` works properly
        """
        # Arrange
        a = Point3D(3, 5, 4)
        b = Point3D(2, 4, 3)  # T, T, T
        c = Point3D(2, 4, 4)  # T, T, F
        d = Point3D(2, 5, 4)  # T, F, ?
        e = Point3D(4, 4, 7)  # F, ?, ?

        # Act
        is_a_gt_b = a > b
        is_a_gt_c = a > c
        is_a_gt_d = a > d
        is_a_gt_e = a > e

        # Assert
        self.assertTrue(is_a_gt_b)
        self.assertFalse(is_a_gt_c)
        self.assertFalse(is_a_gt_d)
        self.assertFalse(is_a_gt_e)

    def test_24_ge(self):
        """
        Verify `>=` works properly
        """
        # Arrange
        a = Point3D(3, 5, 4)
        b = Point3D(2, 5, 3)  # T, T, T
        c = Point3D(2, 5, 5)  # T, T, F
        d = Point3D(2, 6, 4)  # T, F, ?
        e = Point3D(4, 4, 7)  # F, ?, ?

        # Act
        is_a_ge_b = a >= b
        is_a_ge_c = a >= c
        is_a_ge_d = a >= d
        is_a_ge_e = a >= e

        # Assert
        self.assertTrue(is_a_ge_b)
        self.assertFalse(is_a_ge_c)
        self.assertFalse(is_a_ge_d)
        self.assertFalse(is_a_ge_e)
