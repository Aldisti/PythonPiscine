
from math import sqrt

class Point:
    def __init__(self, x, y) -> None:
        self.x = float(x)
        self.y = float(y)
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def distance(self, point) -> float:
        return eval(f"sqrt(abs({(point.x ** 2 - self.x ** 2) + (point.y ** 2 - self.y ** 2)}))")

def main() -> None:
    tmp = input("Insert the coordinates of the first point: ")
    p1 = Point(tmp[:tmp.index(',')], tmp[tmp.index(',') + 1:])
    tmp = input("Insert the coordinates of the second point: ")
    p2 = Point(tmp[:tmp.index(',')], tmp[tmp.index(',') + 1:])
    print(f"Their distance is: {p1.distance(p2)}")

if __name__ == '__main__':
    main()
