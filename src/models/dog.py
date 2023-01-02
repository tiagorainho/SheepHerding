from __future__ import annotations

from models.dog_model import DogModel
from classes.vector import Vector

ACELARATION_MULTIPLIER = 0.95
MAX_VELOCITY = 2
MAX_ACCELERATION = 0.2
MIN_VELOCITY = 0.02

class Dog:
    position: Vector
    velocity: Vector
    selected: bool
    dog_model: DogModel

    def __init__(self, position: Vector, dog_model: DogModel) -> None:
        self.position = position
        self.velocity = Vector(0, 0)
        self.dog_model = dog_model

    def accelerate(self, acceleration: Vector):
        self.velocity.sum(acceleration.limit(MAX_ACCELERATION)).limit(MAX_VELOCITY)
    
    def update(self, selected: bool):
        self.selected = selected
        self.velocity.mult(ACELARATION_MULTIPLIER).limit(MAX_VELOCITY)

        if self.velocity.magnitude <= MIN_VELOCITY:
            self.velocity = Vector(0,0)

        self.position.sum(self.velocity)
    
    def __str__(self) -> str:
        return f"Dog[{hex(id(self))}]: {self.position}"
    
    def __repr__(self) -> str:
        return str(self)