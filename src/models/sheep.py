from __future__ import annotations
from typing import List

from classes.vector import Vector

from models.boid import Boid

MAX_VELOCITY = 2
MAX_ACCELERATION = 0.6

class Sheep(Boid):
    position: Vector
    velocity: Vector

    def __init__(self, position: Vector, velocity: Vector) -> None:
        self.position = position
        self.velocity = velocity


    def update(self, closest_sheep: List[Sheep], threats: List[Vector]):
        # self.fsm.update(ant=self)

        acceleration: Vector = self.get_boid_behaviour(closest_sheep, threats)
        self.velocity.sum(acceleration.limit(MAX_ACCELERATION)).limit(MAX_VELOCITY)
        self.position.sum(self.velocity)