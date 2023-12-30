"""
Module containing the unittests for the GridIterator3D class
"""

import unittest

from src.grid_points.grid_iterator_3d import GridIterator3D
from src.grid_points.point_3d import Point3D


class TestGridIterator3D(unittest.TestCase):
    """
    Test cases for the GridIterator3D class
    """

    def test_01_next(self):
        """
        Verify a simple iteration by checking if __next__ works
        """
        # Arrange
        bounds = Point3D(2, 3, 4)
        iterator = GridIterator3D(bounds)

        expected_first = Point3D(0, 0, 0)
        expected_second = Point3D(0, 0, 1)

        # Act
        actual_first = next(iterator)
        actual_second = next(iterator)

        # Assert
        self.assertEqual(expected_first, actual_first)
        self.assertEqual(expected_second, actual_second)

    def test_02_stop_iteration(self):
        """
        Verify that StopIteration is thrown when the bounds are reached.
        Given bounds (2, 3, 2), expected points are:
        (0, 0, 0), (0, 0, 1),
        (0, 1, 0), (0, 1, 1),
        (0, 2, 0), (0, 2, 1),
        (1, 0, 0), (1, 0, 1),
        (1, 1, 0), (1, 1, 1),
        (1, 2, 0), (1, 2, 1)
        """
        # Arrange
        bounds = Point3D(2, 3, 2)
        iterator = GridIterator3D(bounds)
        expected_amount = 12

        # Act
        for _ in range(expected_amount):
            next(iterator)

        # Assert
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_03_points_returned(self):
        """
        Verify the points returned by the iterator are correct
        """
        # Arrange
        bounds = Point3D(2, 3, 2)
        iterator = GridIterator3D(bounds)
        expected_points = [
            Point3D(0, 0, 0),
            Point3D(0, 0, 1),
            Point3D(0, 1, 0),
            Point3D(0, 1, 1),
            Point3D(0, 2, 0),
            Point3D(0, 2, 1),
            Point3D(1, 0, 0),
            Point3D(1, 0, 1),
            Point3D(1, 1, 0),
            Point3D(1, 1, 1),
            Point3D(1, 2, 0),
            Point3D(1, 2, 1),
        ]

        # Act
        actual_points = list(iterator)

        # Assert
        self.assertEqual(expected_points, actual_points)

    def test_04_points_returned_lower_bound(self):
        """
        Verify the points returned by the iterator are correct, when a lower bound is provided
        """

        # Arrange
        upper_bounds = Point3D(3, 4, 3)
        lower_bounds = Point3D(1, 1, 1)

        iterator = GridIterator3D(upper_bounds, lower_bounds)
        expected_points = [
            Point3D(1, 1, 1),
            Point3D(1, 1, 2),
            Point3D(1, 2, 1),
            Point3D(1, 2, 2),
            Point3D(1, 3, 1),
            Point3D(1, 3, 2),
            Point3D(2, 1, 1),
            Point3D(2, 1, 2),
            Point3D(2, 2, 1),
            Point3D(2, 2, 2),
            Point3D(2, 3, 1),
            Point3D(2, 3, 2),
        ]

        # Act
        actual_points = list(iterator)

        # Assert
        self.assertEqual(expected_points, actual_points)
