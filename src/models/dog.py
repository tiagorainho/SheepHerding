from __future__ import annotations

from classes.vector import Vector

DESACELARATION_MULTIPLIER = 0.95
MAX_VELOCITY = 3
MAX_ACCELERATION = 0.1


class Dog:
    position: Vector
    velocity: Vector
    selected: bool

    def __init__(self, position: Vector) -> None:
        self.position = position
        self.velocity = Vector(0, 0)

    def move(self, acceleration: Vector):
        self.velocity.sum(acceleration.limit(MAX_ACCELERATION)).limit(MAX_VELOCITY)
        self.position.sum(self.velocity)
    
    def update(self, selected: bool):
        self.selected = selected
        self.velocity.mult(DESACELARATION_MULTIPLIER)
        self.position.sum(self.velocity)