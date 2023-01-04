from __future__ import annotations

from typing import List
from utils.math.vector import Vector

MIN_CORRAL_RADIUS: float = 8
MAX_CORRAL_RADIUS: float = 15

class Corral:
    position: Vector
    radius: float

    def __init__(self, position: Vector, radius: float) -> None:
        self.position = position
        self.radius = radius
    
    def update(self, sheeps: List):

        # remove sheeps
        for sheep in sheeps:
            if sheep.position.distance(self.position) < self.radius:
                sheep.in_corral(corral = self)
            else:
                sheep.in_corral(corral = None)