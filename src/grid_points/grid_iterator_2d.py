"""
Module containing the 2D grid iterator class
"""

from collections import abc
from typing import Optional

from src.grid_points.point_2d import Point2D


class GridIterator2D(abc.Iterator):
    """
    Represents the 2D Grid iterator.
    This class iterates the 2D grid defined by `end` and `start` (default is (0, 0)).

    Iteration is done row by row - iterate over the points on the first row,
    then the second one, etc.
    """
    def __init__(self, end: Point2D, start: Optional[Point2D] = None):
        self.__end = end
        self.__start = start

        if self.__start is None:
            self.__start = Point2D(0, 0)

        x_range = range(self.__start.x, self.__end.x)
        y_range = range(self.__start.y, self.__end.y)

        self.__iterator = (Point2D(x, y) for x in x_range for y in y_range)

    def __next__(self) -> Point2D:
        return next(self.__iterator)
