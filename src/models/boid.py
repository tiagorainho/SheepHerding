from __future__ import annotations
from typing import List


from classes.vector import Vector

class Boid():

    position: Vector
    velocity: Vector
    max_force: float = 1

    allignment_strength: float = 1
    cohesion_strength: float = 2
    separation_strength: float = 12

    def __init__(self) -> None:
        pass

    
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
            .mult(scalar = self.allignment_strength)


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
            .mult(scalar = self.cohesion_strength)

    def separation(self, closest_boids: List[Boid]) -> Vector:
        repulsive_force = Vector(0,0)
        if len(closest_boids) == 0:
            return repulsive_force

        # get median position of closest boids
        for boid in closest_boids:
            repulsive_vector = self.position.copy().sub(boid.position)
            mag = repulsive_vector.magnitude
            repulsive_force.sum(repulsive_vector.div(mag))

        return repulsive_force\
            .div(len(closest_boids))\
            .mult(scalar = self.separation_strength)
            
    
    # enemies: List[Vector]
    def get_boid_behaviour(self, closest_boids: List[Boid]) -> Vector:
        
        return self.allignment(closest_boids)\
            .sum(self.cohesion(closest_boids))\
            .sum(self.separation(closest_boids))\
            .limit(value = self.max_force)