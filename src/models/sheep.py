from __future__ import annotations
from typing import List

from observers.subject import Subject
from classes.vector import Vector

from models.boid import Boid, BoidBreed
from states.sheep_fsm import SheepFSM
from models.corral import Corral
from sprites.sheep_model import SheepModel

# breed configurations
DRAG_FACTOR = 0.9
MAX_VELOCITY = 1.5
MAX_ACCELERATION = 0.6
ALLIGNMENT_STRENGTH: float = 0.5
COHESION_STRENGTH: float = 0.1
SEPARATION_STRENGTH: float = 8
FEAR_MULTIPLIER: float = 5
MINIMUM_BOID_DISTANCE: float = 20

# game configurations
MIN_VELOCITY = 0.1

class SheepBreed(BoidBreed):
    maximum_velocity: float
    maximum_acceleration: float
    drag_factor: float

    def __init__(self, 
        allignment_strength:float = ALLIGNMENT_STRENGTH,
        cohesion_strength:float = COHESION_STRENGTH,
        separation_strength:float = SEPARATION_STRENGTH,
        minimum_confort_distance:float = MINIMUM_BOID_DISTANCE,
        threat_fear_multiplier:float = FEAR_MULTIPLIER,
        maximum_velocity:float = MAX_VELOCITY,
        maximum_acceleration:float = MAX_ACCELERATION,
        drag_factor:float = DRAG_FACTOR
    ) -> None:
        self.allignment_strength = allignment_strength
        self.cohesion_strength = cohesion_strength
        self.separation_strength = separation_strength
        self.minimum_confort_distance = minimum_confort_distance
        self.threat_fear_multiplier = threat_fear_multiplier
        self.maximum_velocity = maximum_velocity
        self.maximum_acceleration = maximum_acceleration
        self.drag_factor = drag_factor


class Sheep(Boid, Subject):
    breed: SheepBreed
    sheep_model: SheepModel
    position: Vector
    velocity: Vector
    
    fsm: SheepFSM
    
    closest_sheep: List[Sheep]
    threats: List[Vector]
    
    corral: Corral or None

    def __init__(self, position: Vector, velocity: Vector, sheep_model: SheepModel, sheep_breed: SheepBreed) -> None:
        Subject.__init__(self)
        Boid.__init__(self, breed=sheep_breed)

        self.sheep_model = sheep_model

        self.corral = None
        self.position = position
        self.velocity = velocity
        self.fsm = SheepFSM()

        self.threats = []
        self.closest_sheep = []

    def boid_acceleration(self) -> Vector:
        return self.get_boid_behaviour(self.closest_sheep, self.threats)
    
    def in_corral(self, corral = None):
        self.corral = corral

    def update(self, closest_sheep: List[Sheep], threats: List[Vector]):

        # update perception
        self.closest_sheep = closest_sheep
        self.threats = threats

        # update sheep state
        self.fsm.update(self)

        # simulate drag
        self.velocity.mult(self.breed.drag_factor)

        # ignore minimal velocity changes. Objective: diminish flickering
        if self.velocity.magnitude <= MIN_VELOCITY:
            self.velocity = Vector(0,0)

        self.position.sum(self.velocity)
    
    def accelerate(self, vector: Vector):
        self.velocity.sum(vector.limit(self.breed.maximum_acceleration)).limit(self.breed.maximum_velocity)