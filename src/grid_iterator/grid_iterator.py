from abc import ABC, abstractmethod

from src.point import Point


class GridIterator(ABC):
    def __next__(self) -> Point:
        pass