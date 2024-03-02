
class Point:
    def __init__(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

class Circle:
    def __init__(self, center, radius) -> None:
        self.center = Point(*center)
        self.radius = int(radius)

    def __str__(self) -> str:
        return f"Circle of center {self.center} and radius {self.radius}"

def main() -> None:
    print(Circle((150, 100), 75))

if __name__ == '__main__':
    main()

