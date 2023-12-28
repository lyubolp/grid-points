"""
Module containing the Point2D class
"""
from math import sqrt
from typing import Optional


class Point2D:
    """
    Class modeling a point in the discrete 2D space
    """
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        """
        Return the x coordinate of the point

        :rtype: int
        """
        return self.__x

    # Setters must be right after the properties themselves, otherwise mypy throws an error
    @x.setter
    def x(self, new_x: int):
        """
        Sets the x coordinate of the point
        :type new_x: int
        """
        self.__x = new_x

    @property
    def y(self) -> int:
        """
        Returns the y coordinate of the point

        :rtype: int
        """
        return self.__y

    # Setters must be right after the properties themselves, otherwise mypy throws an error
    @y.setter
    def y(self, new_y: int):
        """
        Sets the y coordinate of the point

        :type new_y: int
        """
        self.__y = new_y

    def __str__(self) -> str:
        # TODO - Docstring
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'Point2D({self.x}, {self.y})'

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point2D):
            # https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
            raise ValueError("Invalid type for other")

        return self.x == other.x and self.y == other.y

    def __add__(self, other: "Point2D") -> "Point2D":
        """
        Add two points together.
        For example - `Point2D(x1, y1) + Point2D(x2, y2) = Point2D(x1 + x2, y1 + y2)`

        :param other: The point that will be added
        :type other: Point2D
        :return: Resulting point
        :rtype: Point2D
        """
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point2D") -> "Point2D":
        """
        Subtract a point from the current one
        For example - `Point2D(x1, y1) - Point2D(x2, y2) = Point2D(x1 - x2, y1 - y2)`

        :param other: The point that will be subtracted
        :type other: Point2D
        :return: Resulting point
        :rtype: Point2D
        """
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Point2D") -> "Point2D":
        """
        Multiply two points together.
        For example - `Point2D(x1, y1) * Point2D(x2, y2) = Point2D(x1 * x2, y1 * y2)`

        :param other: The point that will be added
        :type other: Point2D
        :return: Resulting point
        :rtype: Point2D
        """
        return Point2D(self.x * other.x, self.y * other.y)

    def __floordiv__(self, other: "Point2D") -> "Point2D":
        """
        Divide a point from the current one
        For example - `Point2D(x1, y1) // Point2D(x2, y2) = Point2D(x1 // x2, y1 // y2)`

        :param other: The divisor point
        :type other: Point2D
        :return: Resulting point
        :rtype: Point2D
        """
        return Point2D(self.x // other.x, self.y // other.y)

    def distance_to(self, other: "Point2D") -> float:
        """
        Calculate the distance between the current point an any other one

        :param other: The Point to calculate the distance to
        :type other: Point2Д
        :return: The Eucledian distance between the points
        :rtype: float
        """
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def is_within(self, end: "Point2D", start: Optional["Point2D"] = None) -> bool:
        """
        Check if a point is inside bounds. Upper bounds are exclusive.
        Default lower bounds are 0

        Example:
        ```python
        bounds = Point2D(3, 4)
        a = Point2D(2, 3)
        b = Point2D(3, 4)
        c = Point2D(-1, -2)

        a.is_within(bounds)  # True
        b.is_within(bounds)  # False
        c.is_within(bounds)  # False
        ```

        :param end: The upper bounds of the region
        :type end: Point
        :param start: The lower bounds of the region, defaults to None,
          which is interpreted to (0, 0))
        :type start: Optional[Point2D], optional
        :return: If the current point is inside the specified bounds
        :rtype: bool
        """
        if start is None:
            start = Point2D(0, 0)

        return start.x <= self.x < end.x and start.y <= self.y < end.y
