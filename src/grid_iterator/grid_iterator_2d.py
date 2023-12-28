"""
Module containing the 2D grid iterator class
"""

from typing import Optional

from src.grid_iterator.grid_iterator import GridIterator
from src.point_2d import Point2D


class GridIterator2D(GridIterator):
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
            self.__current = Point2D(0, 0)
        else:
            self.__current = self._start

    def __next__(self) -> Point2D:
        current = self.__current

        if not self.__current.is_within(self._end):
            raise StopIteration()

        if self.__current.x < self._end.x:
            self.__current.x += 1
        else:
            self.__current.y += 1
            self.__current.x = 0

        return current
