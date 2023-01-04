import pygame

from typing import List

from models.sheep import Sheep
from sprites.sheep_sprite import SheepSprite
from collections import defaultdict
from services.service_locator import ServiceLocator
from services.dog_service import DogService


PERCEPTION_DISTANCE = 40

class SheepService:

    # change to use a map [coordinates, sheep]
    sprites = pygame.sprite.Group
    
    service_locator: ServiceLocator

    def __init__(self):
        self.sprites = pygame.sprite.Group()
        self.service_locator = ServiceLocator.get_instance()

    @property
    def sheeps(self) -> List[Sheep]:
        """
        Get all available Sheeps.
        """
        
        return [sprite.sheep for sprite in self.sprites.sprites()]

    def spawn(self, sheep: Sheep):
        """
        Spawn a new sheep.
        """

        self.sprites.add(SheepSprite(sheep=sheep))
    
    def update(self):
        """
        Update sheep. This process fetches all the sheeps and threats to them (such as the sheepard dogs) and updates the sheeps velocity based on neighbor sheeps and threats.
        """

        threats = defaultdict(list)

        # get dog service to fetch all the dogs
        dog_service: DogService = self.service_locator.get_service(DogService.__name__)
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