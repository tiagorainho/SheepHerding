from __future__ import annotations

from classes.vector import Vector

ACELARATION_MULTIPLIER = 0.95
MAX_VELOCITY = 2
MAX_ACCELERATION = 0.2


class Dog:
    position: Vector
    velocity: Vector
    selected: bool

    def __init__(self, position: Vector) -> None:
        self.position = position
        self.velocity = Vector(0, 0)

    def accelerate(self, acceleration: Vector):
        self.velocity.sum(acceleration.limit(MAX_ACCELERATION)).limit(MAX_VELOCITY)
    
    def update(self, selected: bool):
        self.selected = selected
        self.velocity.mult(ACELARATION_MULTIPLIER).limit(MAX_VELOCITY)
        self.position.sum(self.velocity)