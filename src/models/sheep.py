from __future__ import annotations
from typing import List

from classes.vector import Vector

from models.boid import Boid
from states.sheep_fsm import SheepFSM

ACELARATION_MULTIPLIER = 0.9
MAX_VELOCITY = 2
MAX_ACCELERATION = 0.6
MIN_VELOCITY = 0.1

class Sheep(Boid):
    position: Vector
    velocity: Vector
    
    fsm: SheepFSM
    
    closest_sheep: List[Sheep]
    threats: List[Vector]

    def __init__(self, position: Vector, velocity: Vector) -> None:
        self.position = position
        self.velocity = velocity
        self.fsm = SheepFSM()

        self.threats = []
        self.closest_sheep = []


    def boid_acceleration(self) -> Vector:
        return self.get_boid_behaviour(self.closest_sheep, self.threats)


    def update(self, closest_sheep: List[Sheep], threats: List[Vector]):

        # update perception
        self.closest_sheep = closest_sheep
        self.threats = threats

        self.fsm.update(ant=self)

        # simulate drag
        self.velocity.mult(ACELARATION_MULTIPLIER)

        # ignore minimal velocity changes. Objective: diminish flickering
        if self.velocity.magnitude <= MIN_VELOCITY:
            self.velocity = Vector(0,0)

        self.position.sum(self.velocity)
    
    def accelerate(self, vector: Vector):
        self.velocity.sum(vector.limit(MAX_ACCELERATION)).limit(MAX_VELOCITY)