from __future__ import annotations
from typing import Tuple, List

import numpy as np

from classes.vector import Vector

from models.boid import Boid


class Sheep(Boid):
    position: Vector
    velocity: Vector
    max_velocity: float = 2

    def __init__(self, position: Vector, velocity: Vector) -> None:
        self.position = position
        self.velocity = velocity


    def update(self, closest_sheep: List[Sheep], threats: List[Vector]):
        # self.fsm.update(ant=self)

        acceleration: Vector = self.get_boid_behaviour(closest_sheep, threats)
        self.velocity.sum(acceleration).limit(self.max_velocity)
        self.position.sum(self.velocity)