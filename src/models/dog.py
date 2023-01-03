from __future__ import annotations

from sprites.dog_model import DogModel
from classes.vector import Vector

# breed configurations
DRAG_FACTOR = 0.95
MAX_VELOCITY = 2
MAX_ACCELERATION = 0.2

# game configurations
MIN_VELOCITY = 0.02

class DogBreed:
    drag_factor: float
    maximum_velocity: float
    maximum_acceleration: float

    def __init__(self,
        drag_factor: float = DRAG_FACTOR,
        maximum_velocity: float = MAX_VELOCITY,
        maximum_acceleration: float = MAX_ACCELERATION
    ) -> None:
        self.drag_factor = drag_factor
        self.maximum_acceleration = maximum_acceleration
        self.maximum_velocity = maximum_velocity


class Dog:
    position: Vector
    velocity: Vector
    breed: DogBreed
    dog_model: DogModel

    selected: bool

    def __init__(self, position: Vector, dog_model: DogModel, breed: DogBreed) -> None:
        self.breed = breed
        self.dog_model = dog_model
        self.position = position
        self.velocity = Vector(0, 0)

    def accelerate(self, acceleration: Vector):
        self.velocity.sum(acceleration.limit(self.breed.maximum_acceleration)).limit(MAX_VELOCITY)
    
    def update(self, selected: bool):
        self.selected = selected
        self.velocity.mult(self.breed.drag_factor).limit(self.breed.maximum_velocity)

        if self.velocity.magnitude <= MIN_VELOCITY:
            self.velocity = Vector(0,0)

        self.position.sum(self.velocity)
    
    def __str__(self) -> str:
        return f"Dog[{hex(id(self))}]: {self.position}"
    
    def __repr__(self) -> str:
        return str(self)