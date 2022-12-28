from __future__ import annotations

from typing import List
from classes.vector import Vector


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