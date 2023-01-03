from __future__ import annotations
from typing import List

from classes.vector import Vector


class BoidBreed:
    allignment_strength: float
    cohesion_strength: float
    separation_strength: float
    threat_fear_multiplier: float
    minimum_confort_distance: float

    def __init__(self, 
        allignment_strength: float,
        cohesion_strength: float,
        separation_strength: float,
        threat_fear_multiplier: float,
        minimum_confort_distance: float
    ) -> None:
        self.allignment_strength = allignment_strength
        self.cohesion_strength = cohesion_strength
        self.separation_strength = separation_strength
        self.threat_fear_multiplier = threat_fear_multiplier
        self.minimum_confort_distance = minimum_confort_distance

    @property
    def threat_separation_strength(self):
        return self.separation_strength * self.threat_fear_multiplier


class Boid:
    breed: BoidBreed

    position: Vector
    velocity: Vector
    
    def __init__(self, breed: BoidBreed) -> None:
        self.breed = breed

    def allignment(self, closest_boids: List[Boid]) -> Vector:
        steering: Vector = Vector(0,0)
        if len(closest_boids) == 0:
            return steering

        # get stearing of closest boids
        for boid in closest_boids:
            steering.sum(boid.velocity.div(boid.position.distance(self.position)))
        
        return steering\
            .div(value = len(closest_boids))\
            .sub(vector = self.velocity)\
            .mult(scalar = self.breed.allignment_strength)


    def cohesion(self, closest_boids: List[Boid]) -> Vector:
        average_flock_position: Vector = Vector(0,0)
        if len(closest_boids) == 0:
            return average_flock_position

        # get median position of closest boids
        for boid in closest_boids:
            average_flock_position.sum(boid.position)
        
        average_flock_position.div(value = len(closest_boids))

        return average_flock_position\
            .sub(self.position)\
            .mult(scalar = self.breed.cohesion_strength)

    def separation(self, neighbors: List[Vector], separation_strength: float) -> Vector:
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
        near_boids = [boid.position for boid in closest_boids if boid.position.distance(self.position) <= self.breed.minimum_confort_distance]
        return self.allignment(closest_boids)\
            .sum(self.cohesion(closest_boids))\
            .sum(self.separation(near_boids, self.breed.separation_strength))\
            .sum(self.separation(threats, self.breed.threat_separation_strength))