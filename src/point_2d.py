"""
Module containing the Point2D class
"""
from math import sqrt
from typing import Optional

from grid_iterator.grid_iterator import GridIterator
from grid_iterator.grid_iterator_2d import GridIterator2D
from src.point import Point


class Point2D(Point):
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @x.setter
    def x(self, new_x: int):
        self.__x = new_x

    @y.setter
    def y(self, new_y: int):
        self.__y = new_y

    def __iter__(self) -> GridIterator:
        """
        Returns an GridIterator, which can be used for iteration over the grid
        """
        return GridIterator2D(self)

    def __str__(self) -> str:
        # TODO - Docstring
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'Point2D({self.x}, {self.y})'

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other: "Point2D") -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Point") -> "Point":
        return Point(self.x * other.x, self.y * other.y)

    def __floordiv__(self, other: "Point") -> "Point":
        return Point(self.x // other.x, self.y // other.y)

    def distance_to(self, other: "Point") -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def is_within(self, end: "Point", start: Optional["Point2D"] = None) -> bool:
        if start is None:
            start = Point2D(0, 0)

        return start.x <= self.x < end.x and start.y <= self.y < end.y
