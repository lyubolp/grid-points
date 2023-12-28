"""
Module containing the abstract class for grid iteration
"""
from abc import ABC, abstractmethod
from typing import Optional

from src.point import Point


class GridIterator(ABC):
    """
    Represents an abstract grid iterator over a Nth dimentional grid

    :param ABC: _description_
    :type ABC: _type_
    """
    def __init__(self, end: Point, start: Optional[Point] = None):
        pass

    @abstractmethod
    def __next__(self) -> Point:
        pass
