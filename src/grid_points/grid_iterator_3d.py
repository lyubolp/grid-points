"""
Module containing the 3D grid iterator class
"""

from collections import abc
from copy import copy
from typing import Optional

from src.grid_points.point_3d import Point3D


class GridIterator3D(abc.Iterator):
    """
    Represents the 3D Grid iterator.
    This class iterates the 3D grid defined by `end` and `start` (default is (0, 0, 0)).

    Iteration is done first on the z axis, then on y, then on x.

    Example with bounds: (2, 2, 2):
        (0, 0, 0), (0, 0, 1),
        (0, 1, 0), (0, 1, 1),
        (1, 0, 0), (1, 0, 1),
        (1, 1, 0), (1, 1, 1)
    """
    def __init__(self, end: Point3D, start: Optional[Point3D] = None):
        self.__end = end
        self.__start = start

        if self.__start is None:
            self.__start = Point3D(0, 0, 0)

        x_range = range(self.__start.x, self.__end.x)
        y_range = range(self.__start.y, self.__end.y)
        z_range = range(self.__start.z, self.__end.z)

        self.__iterator = (Point3D(x, y, z) for x in x_range for y in y_range for z in z_range)

    def __next__(self) -> Point3D:
        return next(self.__iterator)
