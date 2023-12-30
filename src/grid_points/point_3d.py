"""
Module containing the Point3D class
"""
from math import sqrt
from typing import Optional


class Point3D:
    """
    Class modeling a point in the discrete 3D space
    """
    def __init__(self, x: int, y: int, z: int):
        self.__x = x
        self.__y = y
        self.__z = z

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

    @property
    def z(self) -> int:
        """
        Returns the z coordinate of the point

        :rtype: int
        """
        return self.__z

    # Setters must be right after the properties themselves, otherwise mypy throws an error
    @z.setter
    def z(self, new_z: int):
        """
        Sets the z coordinate of the point

        :type new_z: int
        """
        self.__z = new_z

    def __str__(self) -> str:
        # TODO - Docstring
        return f'({self.x}, {self.y}, {self.z})'

    def __repr__(self) -> str:
        return f'Point3D({self.x}, {self.y}, {self.z})'

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point3D):
            # https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
            raise NotImplementedError("Invalid type for other")

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Point3D):
            # https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
            raise NotImplementedError("Invalid type for other")

        return self.x < other.x and self.y < other.y and self.z < other.z

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Point3D):
            # https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
            raise NotImplementedError("Invalid type for other")

        return self.x <= other.x and self.y <= other.y and self.z <= other.z

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Point3D):
            # https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
            raise NotImplementedError("Invalid type for other")

        return self.x > other.x and self.y > other.y and self.z > other.z

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Point3D):
            # https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
            raise NotImplementedError("Invalid type for other")

        return self.x >= other.x and self.y >= other.y and self.z >= other.z

    def __add__(self, other: "Point3D") -> "Point3D":
        """
        Add two points together.
        For example - `Point3D(x1, y1, z1) + Point3D(x2, y2, z2) = Point3D(x1+x2, y1+y2, z1+z2)`

        :param other: The point that will be added
        :type other: Point3D
        :return: Resulting point
        :rtype: Point3D
        """
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Point3D") -> "Point3D":
        """
        Subtract a point from the current one
        For example - `Point3D(x1, y1, z1) - Point3D(x2, y2, z2) = Point3D(x1-x2, y1-y2, z1-z2)`

        :param other: The point that will be subtracted
        :type other: Point3D
        :return: Resulting point
        :rtype: Point3D
        """
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: "Point3D") -> "Point3D":
        """
        Multiply two points together.
        For example - `Point3D(x1, y1, z1) * Point3D(x2, y2, z2) = Point3D(x1*x2, y1*y2, z1*z2)`

        :param other: The point that will be added
        :type other: Point3D
        :return: Resulting point
        :rtype: Point3D
        """
        return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __floordiv__(self, other: "Point3D") -> "Point3D":
        """
        Divide a point from the current one
        For example -
        `Point3D(x1, y1, z1) // Point3D(x2, y2, z2) = Point3D(x1//x2, y1//y2, z1//z2)`

        :param other: The divisor point
        :type other: Point3D
        :return: Resulting point
        :rtype: Point3D
        """
        return Point3D(self.x // other.x, self.y // other.y, self.z // other.z)

    def distance_to(self, other: "Point3D") -> float:
        """
        Calculate the distance between the current point an any other one

        :param other: The Point to calculate the distance to
        :type other: Point3D
        :return: The Eucledian distance between the points
        :rtype: float
        """
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def is_within(self, end: "Point3D", start: Optional["Point3D"] = None) -> bool:
        """
        Check if a point is inside bounds. Upper bounds are exclusive.
        Default lower bounds are 0

        Example:
        ```python
        bounds = Point3D(3, 4, 5)
        a = Point3D(2, 3, 4)
        b = Point3D(3, 4, 4)
        c = Point3D(-1, -2, -3)

        a.is_within(bounds)  # True
        b.is_within(bounds)  # False
        c.is_within(bounds)  # False
        ```

        :param end: The upper bounds of the region
        :type end: Point
        :param start: The lower bounds of the region, defaults to None,
          which is interpreted to (0, 0, 0))
        :type start: Optional[Point3D], optional
        :return: If the current point is inside the specified bounds
        :rtype: bool
        """
        if start is None:
            start = Point3D(0, 0, 0)

        is_x_inside = start.x <= self.x < end.x
        is_y_inside = start.y <= self.y < end.y
        is_z_inside = start.z <= self.z < end.z

        return is_x_inside and is_y_inside and is_z_inside
