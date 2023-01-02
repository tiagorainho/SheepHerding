from __future__ import annotations
from math import dist, sqrt

class Vector:
    x: float
    y: float

    def __init__(self, x: float, y:float) -> None:
        self.x = x
        self.y = y
    
    @property
    def magnitude(self):
        return sqrt(self.x*self.x + self.y*self.y)
    
    def distance(self, other: Vector) -> float:
        return dist((self.x, self.y), (other.x, other.y))
    
    def sum(self, vector: Vector) -> Vector:
        self.x += vector.x
        self.y += vector.y
        return self
    
    def div(self, value: float) -> Vector:
        if value == 0:
            return self

        self.x = self.x/value
        self.y = self.y/value
        return self
    
    def sub(self, vector: Vector) -> Vector:
        self.x -= vector.x
        self.y -= vector.y
        return self
    
    def mult(self, scalar: float) -> Vector:
        self.x *= scalar
        self.y *= scalar
        return self

    def normalize(self) -> Vector:
        return self.div(self.magnitude)
    
    def limit(self, value: float) -> Vector:
        mag = self.magnitude
        if mag > value:
            self.normalize().mult(value)
        return self

    def copy(self) -> Vector:
        return Vector(x=self.x, y=self.y)

    def __str__(self):
        return str((self.x, self.y))
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, vector: Vector) -> bool:
        return vector.x == self.x and vector.y == self.y

if __name__ == '__main__':
    v = Vector(1221,31212)
    import time
    s1 = time.perf_counter_ns()
    v = v.normalize()
    print(v, v.magnitude)
    print(time.perf_counter_ns()-s1)
