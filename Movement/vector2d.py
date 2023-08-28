from __future__ import annotations
import math

class Vector:
    def __init__(self, x:int = 0, y:int = 0, coordinates:tuple[int] | list[int] | bool = False):
        if coordinates:
            self.x = coordinates[0]
            self.y = coordinates[1]
        else:
            self.x: int = x
            self.y: int = y

    def as_tup(self) -> tuple[int]:
        return (self.x, self.y)
    
    def as_list(self) -> list[int]:
        return [self.x, self.y]

    def set_vector(self, x, y):
        self.x = x
        self.y = y
    
    def as_dict(self) -> dict[int, int]:
        return {
            1: self.x,
            2: self.y
        }

    def normalize(self) -> float | None:
        return self//self.magnitude() if self.magnitude() > 0 else None

    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __len__(self) -> round:
        return round(self.magnitude())

    def __str__(self) -> str:
        return f"   ___| X Position: {self.x} | Y Position: {self.y} |___   "

    def __repr__(self) -> str:
        return f"   ___| X Position: {self.x} | Y Position: {self.y} |___   "
    
    def __iadd__(self, obj:int | float | Vector)-> Vector:
        
        x = self.x + obj.x
        y = self.y + obj.y
        return Vector(x, y)

    def __add__(self, obj:int | float | Vector) -> Vector:
        x = self.x + obj.x
        y = self.y + obj.y
        return Vector(x, y)

    def __sub__(self, obj: int | float | Vector) -> Vector:
        x = self.x - obj.x
        y = self.y - obj.y
        return Vector(x, y)
    
    def __mul__(self, num: int | float | Vector) -> Vector:
        x = self.x * num
        y = self.y * num
        return Vector(x, y)

    def __floordiv__(self, num:int | float | Vector) -> Vector:
        x = self.x // num
        y = self.y // num
        return Vector(x, y)
    
    def __div__(self, num:int | float | Vector) -> Vector:
        x = self.x / num
        y = self.y / num
        return Vector(x, y)

    def __lt__(self, obj) -> bool:
        return self.x < obj.x and self.y < obj.y or obj.x > self.y and obj.y > self.y

    def __gt__(self, obj) -> bool:
        return self.x > obj.x and self.y > obj.y or obj.y < self.y and obj.x < self.x

    def __eq__(self, obj) -> bool:
        return self.x == obj.x and self.y == obj.y