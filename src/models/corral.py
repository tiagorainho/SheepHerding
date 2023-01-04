from __future__ import annotations

from typing import List
from utils.math.vector import Vector

MIN_CORRAL_RADIUS: float = 8
MAX_CORRAL_RADIUS: float = 15

class Corral:
    """
    Corral to store animals.
    """
    
    position: Vector
    radius: float

    def __init__(self, position: Vector, radius: float) -> None:
        self.position = position
        self.radius = radius
    
    def update(self, sheeps: List):
        """
        Sets the corral in which the animals are.
        """

        # NOTE: in order to have multiple corrals, the in_corral(corral = None) must not exist because it would override previously set values by other corrals

        # update sheeps
        for sheep in sheeps:
            if sheep.position.distance(self.position) < self.radius:
                sheep.in_corral(corral = self)
            else:
                sheep.in_corral(corral = None)