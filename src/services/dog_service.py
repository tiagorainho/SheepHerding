from __future__ import annotations

import pygame
from typing import List
from models.dog import Dog

from classes.vector import Vector

from sprites.dog_sprite import DogSprite

class DogService:

    sprites = pygame.sprite.Group
    selected_dog: Dog

    def __init__(self):
        self.sprites = pygame.sprite.Group()
    
    @property
    def dogs(self) -> List[Dog]:
        return [sprite.dog for sprite in self.sprites.sprites()]
    
    def clear_dogs(self):
        self.sprites.empty()

    def select(self, dog: Dog):
        self.selected_dog = dog

    def add_dog(self, dog: Dog):
        self.sprites.add(DogSprite(dog=dog))
    
    def update(self):
        # update dogs positions
        for dog in self.dogs:
            dog.update(selected = (dog == self.selected_dog))
    
    def select_dog(self, direction: Vector):
        dogs = self.dogs

        # filter dogs based on direction vector
        filtered_dogs = []
        for dog in dogs:
            if dog == self.selected_dog: continue

            distance_vector = dog.position.copy().sub(self.selected_dog.position)

            if distance_vector.x > 0 and direction.x > 0:
                filtered_dogs.append(dog)
            if distance_vector.x < 0 and direction.x < 0:
                filtered_dogs.append(dog)
            if distance_vector.y > 0 and direction.y > 0:
                filtered_dogs.append(dog)
            if distance_vector.y < 0 and direction.y < 0:
                filtered_dogs.append(dog)
        
        if len(filtered_dogs) == 0: return

        # find closest
        closest_dog_in_desired_direction = min(filtered_dogs, key=lambda dog: dog.position.distance(self.selected_dog.position))
        
        # select closest dog
        self.select(closest_dog_in_desired_direction)