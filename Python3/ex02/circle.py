
from sys import argv
from math import sqrt

class Point:

    def distance(self, point) -> float:
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = int(x)
        self.y = int(y)

    def __str__(self) -> str:
        return f"The point ({self.x}, {self.y})"

class Circle:

    def contains(self, point: Point) -> bool:
        return self.center.distance(point) <= self.radius

    def __init__(self, center: list | tuple, radius: int) -> None:
        self.center = Point(*center)
        self.radius = int(radius)

    def __str__(self) -> str:
        return f"Circle of center {self.center} and radius {self.radius}"

def main() -> None:
    if len(argv) != 3:
        return
    circle = Circle((0, 0), 1)
    point = Point(float(argv[1]), float(argv[2]))
    if circle.contains(point):
        print(f"{point} lies in the {circle}")
    else:
        print(f"{point} lies out of the {circle}")

if __name__ == '__main__':
    main()

