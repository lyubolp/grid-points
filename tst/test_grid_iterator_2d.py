"""
Module containing the unittests for the GridIterator2D class
"""

import unittest

from src.grid_points.grid_iterator_2d import GridIterator2D
from src.grid_points.point_2d import Point2D


class TestGridIterator2D(unittest.TestCase):
    """
    Test cases for the GridIterator2D class
    """
    def test_01_next(self):
        """
        Verify a simple iteration by checking if __next__ works
        """
        # Arrange
        bounds = Point2D(2, 3)
        iterator = GridIterator2D(bounds)

        expected_first = Point2D(0, 0)
        expected_second = Point2D(0, 1)

        # Act
        actual_first = next(iterator)
        actual_second = next(iterator)

        # Assert
        self.assertEqual(expected_first, actual_first)
        self.assertEqual(expected_second, actual_second)

    def test_02_stop_iteration(self):
        """
        Verify that StopIteration is thrown when the bounds are reached.
        Given bounds (2, 3), expected points are:
        (0, 0), (0, 1), (0, 2)
        (1, 0), (1, 1), (1, 2)
        """
        # Arrange
        bounds = Point2D(2, 3)
        iterator = GridIterator2D(bounds)
        expected_amount = 6

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
        bounds = Point2D(2, 3)
        iterator = GridIterator2D(bounds)
        expected_points = [Point2D(0, 0), Point2D(0, 1), Point2D(0, 2),
                           Point2D(1, 0), Point2D(1, 1), Point2D(1, 2)]

        # Act
        actual_points = list(iterator)

        # Assert
        self.assertEqual(expected_points, actual_points)

    def test_04_points_returned_lower_bound(self):
        """
        Verify the points returned by the iterator are correct, when a lower bound is provided
        """

        # Arrange
        upper_bounds = Point2D(3, 4)
        lower_bounds = Point2D(1, 1)

        iterator = GridIterator2D(upper_bounds, lower_bounds)
        expected_points = [Point2D(1, 1), Point2D(1, 2), Point2D(1, 3),
                           Point2D(2, 1), Point2D(2, 2), Point2D(2, 3)]

        # Act
        actual_points = list(iterator)

        # Assert
        self.assertEqual(expected_points, actual_points)
