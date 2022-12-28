
from typing import List

from models.sheep import Sheep

from sprites.sheep_sprite import SheepSprite
import pygame

from collections import defaultdict
from singletons import service_locator
from services.dog_service import DogService

PERCEPTION_DISTANCE = 40

class SheepService:

    # change to use a map [coordinates, sheep]
    sprites = pygame.sprite.Group

    def __init__(self):
        self.sprites = pygame.sprite.Group()

    @property
    def sheeps(self) -> List[Sheep]:
        return [sprite.sheep for sprite in self.sprites.sprites()]

    def add_sheep(self, sheep: Sheep):
        self.sprites.add(SheepSprite(sheep=sheep))
    
    def update(self):
        threats = defaultdict(list)

        # get dogs
        dog_service: DogService = service_locator.get_service('dog_service')
        dogs = dog_service.dogs
        
        # get sheeps
        sheeps: List[Sheep] = self.sheeps

        # get closest sheep
        neighbors = defaultdict(list)
        for sheep in sheeps:
            neighbors[sheep] = []
            threats[sheep] = []
            for sheep2 in sheeps:
                if sheep == sheep2: continue
                if sheep.position.distance(sheep2.position) < PERCEPTION_DISTANCE:
                    neighbors[sheep].append(sheep2)
            for dog in dogs:
                if sheep.position.distance(dog.position) < PERCEPTION_DISTANCE:
                    threats[sheep].append(dog)
        
        # update sheeps position
        for sheep, closest_sheeps in neighbors.items():
            sheep.update(closest_sheeps, [dog.position for dog in threats[sheep]])
        