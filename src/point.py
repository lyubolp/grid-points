"""
Module containing the abstract class for Point
"""

from abc import ABC, abstractmethod
from typing import Optional

from src.grid_iterator.grid_iterator import GridIterator


class Point(ABC):
    """
    Represents an abstract point in a Nth dimentional grid.

    Supports iteration, string representation, distance calculations
        and bounds calculations
    """

    @abstractmethod
    def __iter__(self) -> GridIterator:
        """
        Returns an GridIterator, which can be used for iteration over the grid
        """
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        # TODO - Docstring
        pass

    @abstractmethod
    def __repr__(self) -> str:
        # TODO - Docstring
        pass

    @abstractmethod
    def __hash__(self) -> int:
        # TODO - Docstring
        pass
    
    @abstractmethod
    def __eq__(self, other: "Point") -> bool:
        pass

    @abstractmethod
    def __add__(self, other: "Point") -> "Point":
        pass

    @abstractmethod
    def __sub__(self, other: "Point") -> "Point":
        pass

    @abstractmethod
    def __mul__(self, other: "Point") -> "Point":
        pass

    @abstractmethod
    def __floordiv__(self, other: "Point") -> "Point":
        pass
    
    @abstractmethod
    def distance_to(self, other: "Point") -> float:
        # TODO - Docstring
        pass
    
    @abstractmethod
    def is_within(self, end: "Point", start: Optional["Point"] = None) -> bool:
        # TODO - Docstring
        pass
