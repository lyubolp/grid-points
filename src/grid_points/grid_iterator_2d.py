"""
Module containing the 2D grid iterator class
"""

from collections import abc
from copy import copy
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
        self._end = end
        self._start = start

        if self._start is None:
            self.__current = Point2D(0, -1)
        else:
            self.__current = self._start - Point2D(0, 1)

    def __next__(self) -> Point2D:
        self.__current.y += 1

        if self.__current.y == self._end.y:
            self.__current.x += 1
            self.__current.y = 0 if self._start is None else self._start.y

        if self.__current.x == self._end.x:
            raise StopIteration()

        return copy(self.__current)
