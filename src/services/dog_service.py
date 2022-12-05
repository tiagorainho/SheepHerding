from __future__ import annotations

import pygame
from typing import List
from models.dog import Dog

from sprites.dog_sprite import DogSprite

class DogService:

    sprites = pygame.sprite.Group
    selected_dog: Dog

    def __init__(self):
        self.sprites = pygame.sprite.Group()
    
    @property
    def dogs(self) -> List[Dog]:
        return [sprite.dog for sprite in self.sprites.sprites()]

    def select(self, dog: Dog):
        self.selected_dog = dog

    def add_dog(self, dog: Dog):
        self.sprites.add(DogSprite(dog=dog))
    
    def update(self):
        # update dogs positions
        for dog in self.dogs:
            dog.update(selected = (dog == self.selected_dog))