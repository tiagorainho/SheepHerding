from __future__ import annotations
from typing import List

from classes.vector import Vector

DEFAULT_ALLIGNMENT_STRENGTH: float = 0.5
DEFAULT_COHESION_STRENGTH: float = 0.1
DEFAULT_SEPARATION_STRENGTH: float = 8
THREAT_SEPARATION_STRENGTH: float = DEFAULT_SEPARATION_STRENGTH * 5
MINIMUM_BOID_DISTANCE: float = 20

class Boid:

    position: Vector
    velocity: Vector
    max_acceleration: float = 1

    allignment_strength: float
    cohesion_strength: float
    separation_strength: float
    

    def __init__(self) -> None:
        self.allignment_strength = DEFAULT_ALLIGNMENT_STRENGTH
        self.cohesion_strength = DEFAULT_COHESION_STRENGTH
        self.separation_strength = DEFAULT_SEPARATION_STRENGTH


    def allignment(self, closest_boids: List[Boid], allignment_strength: float = DEFAULT_ALLIGNMENT_STRENGTH) -> Vector:
        steering: Vector = Vector(0,0)
        if len(closest_boids) == 0:
            return steering

        # get stearing of closest boids
        for boid in closest_boids:
            steering.sum(boid.velocity.div(boid.position.distance(self.position)))
        
        return steering\
            .div(value = len(closest_boids))\
            .sub(vector = self.velocity)\
            .mult(scalar = allignment_strength)


    def cohesion(self, closest_boids: List[Boid], cohesion_strength: float = DEFAULT_COHESION_STRENGTH) -> Vector:
        average_flock_position: Vector = Vector(0,0)
        if len(closest_boids) == 0:
            return average_flock_position

        # get median position of closest boids
        for boid in closest_boids:
            average_flock_position.sum(boid.position)
        
        average_flock_position.div(value = len(closest_boids))

        return average_flock_position\
            .sub(self.position)\
            .mult(scalar = cohesion_strength)

    def separation(self, neighbors: List[Vector], separation_strength: float = DEFAULT_SEPARATION_STRENGTH) -> Vector:
        repulsive_force = Vector(0,0)
        if len(neighbors) == 0:
            return repulsive_force

        # get median position of neighbors
        for position in neighbors:
            repulsive_vector = self.position.copy().sub(position)
            mag = repulsive_vector.magnitude
            repulsive_force.sum(repulsive_vector.div(mag*mag))

        return repulsive_force\
            .div(len(neighbors))\
            .mult(scalar = separation_strength)
            
    
    def get_boid_behaviour(self, closest_boids: List[Boid], threats: List[Vector]) -> Vector:
        near_boids = [boid.position for boid in closest_boids if boid.position.distance(self.position) <= MINIMUM_BOID_DISTANCE]
        return self.allignment(closest_boids)\
            .sum(self.cohesion(closest_boids))\
            .sum(self.separation(near_boids))\
            .sum(self.separation(threats, THREAT_SEPARATION_STRENGTH))\
            .limit(value = self.max_acceleration)