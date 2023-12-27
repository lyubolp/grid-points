from src.grid_iterator.grid_iterator import GridIterator
from src.point_2d import Point2D


class GridIterator2D(GridIterator):
    def __init__(self, bounds: Point2D):
        self.__current = Point2D(0, 0)
        self.__bounds = bounds

    def __next__(self) -> Point2D:
        current = self.__current

        if not self.__current.is_within(self.__bounds):
            raise StopIteration()

        if self.__current.x < self.__bounds.x:
            self.__current.x += 1
        else:
            self.__current.y += 1
            self.__current.x = 0

        return current
