"""
Module containing the abstract class for Point
"""

from abc import ABC, abstractmethod
from typing import Optional


class Point(ABC):
    """
    Represents an abstract point in a Nth dimentional grid.

    Supports iteration, string representation, distance calculations
        and bounds calculations
    """

    @abstractmethod
    def __str__(self) -> str:
        """
        String representation of the Point
        :rtype: str
        """

    @abstractmethod
    def __repr__(self) -> str:
        """Python representation of the Point
        :rtype: str
        """

    @abstractmethod
    def __hash__(self) -> int:
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            # https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
            raise ValueError("Invalid type for other")

        return True

    @abstractmethod
    def __add__(self, other: "Point") -> "Point":
        """
        Add two points together.
        For example - `Point(x1, y1) + Point(x2, y2) = Point(x1 + x2, y1 + y2)`

        :param other: The point that will be added
        :type other: Point
        :return: Resulting point
        :rtype: Point
        """

    @abstractmethod
    def __sub__(self, other: "Point") -> "Point":
        """
        Subtract a point from the current one
        For example - `Point(x1, y1) - Point(x2, y2) = Point(x1 - x2, y1 - y2)`

        :param other: The point that will be subtracted
        :type other: Point
        :return: Resulting point
        :rtype: Point
        """

    @abstractmethod
    def __mul__(self, other: "Point") -> "Point":
        """
        Multiply two points together.
        For example - `Point(x1, y1) * Point(x2, y2) = Point(x1 * x2, y1 * y2)`

        :param other: The point that will be added
        :type other: Point
        :return: Resulting point
        :rtype: Point
        """

    @abstractmethod
    def __floordiv__(self, other: "Point") -> "Point":
        """
        Divide a point from the current one
        For example - `Point(x1, y1) // Point(x2, y2) = Point(x1 // x2, y1 // y2)`

        :param other: The divisor point
        :type other: Point
        :return: Resulting point
        :rtype: Point
        """

    @abstractmethod
    def distance_to(self, other: "Point") -> float:
        """
        Calculate the distance between the current point an any other one

        :param other: The Point to calculate the distance to
        :type other: Point
        :return: The Eucledian distance between the points
        :rtype: float
        """

    @abstractmethod
    def is_within(self, end: "Point", start: Optional["Point"] = None) -> bool:
        """
        Check if a point is inside bounds. Upper bounds are exclusive.
        Default lower bounds are 0

        2D example:
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
          which is interpreted to the 0-point in the space ((0, 0) for 2D, (0, 0, 0) for 3D)
        :type start: Optional[Point], optional
        :return: If the current point is inside the specified bounds
        :rtype: bool
        """
