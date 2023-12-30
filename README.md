# grid-points

Python library, which models a discrete 2D/3D point grid. Mainly used for Advent of Code.

## Installation

Install grid-points with pip

```bash
pip install grid-points
```

## Usage/Examples

```python

```


## API Reference

### Point2D
- `init(x: int, y:int)`
#### Properties
- `x` return the x coordinate of a point
- `y` return the y coordinate of a point
#### Methonds
- `distance_to` - return the distance from the current point to another
- `is_withing` - check if the current point is within given bounds
#### Other
The following dunders were overwritten:
- `__str__` 
- `__repr__`
- `__hash__`
- `__eq__`
- `__lt__`
- `__le__`
- `__gt__`
- `__ge__`
- `__add__` - per-coordinate addition
- `__sub__` - per-coordinate subtraction
- `__mul__` - per-coordinate multiplication
- `__floordiv__` - per-coordinate floor division

### GridIterator2D
Iterate over the 2D grid defined by `start` (default is (0, 0)) and `end`.
- `init(end: Point2D, start: Optional[Point2D] = None)`
- `__next__()`

### Point3D
- `init(x: int, y:int, z: int)`
#### Properties
- `x` return the x coordinate of a point
- `y` return the y coordinate of a point
- `z` return the z coordinate of a point
#### Methonds
- `distance_to` - return the distance from the current point to another
- `is_withing` - check if the current point is within given bounds
#### Other
The following dunders were overwritten:
- `__str__` 
- `__repr__`
- `__hash__`
- `__eq__`
- `__lt__`
- `__le__`
- `__gt__`
- `__ge__`
- `__add__` - per-coordinate addition
- `__sub__` - per-coordinate subtraction
- `__mul__` - per-coordinate multiplication
- `__floordiv__` - per-coordinate floor division

### GridIterator3D
Iterate over the 3D grid defined by `start` (default is (0, 0, 0)) and `end`.
- `init(end: Point3D, start: Optional[Point3D] = None)`
- `__next__()`
