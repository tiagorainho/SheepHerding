from __future__ import annotations

from models.dog_model import DogModel
from classes.vector import Vector

ACELARATION_MULTIPLIER = 0.95
MAX_VELOCITY = 2
MAX_ACCELERATION = 0.2



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
        self.position.sum(self.velocity)