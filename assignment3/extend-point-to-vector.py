import math

class Point:
    def __init__(self, x: float,y: float):
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) == (other.x, other.y)
        return "NotImplemented"

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    def distance_to(self, other: "Point") -> float:
        #math: Euclidian distance to another point
        return math.hypot(self.x - other.x, self.y - other.y)

class Vector(Point):

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return "NotImplemented"

v1 = Vector(-10, 20)
v2 = Vector(-3.5, 4.9)
v3 = v1 + v2