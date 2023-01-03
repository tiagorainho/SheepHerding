

import pygame

from sprites.map_sprite import MapSprite
from services.dog_service import DogService
from services.sheep_service import SheepService
from services import service_locator
from classes.vector import Vector
from models.map_constraints import MapConstraints



class MapService:
    # change to use a map [coordinates, sheep]
    sprites = pygame.sprite.Group

    dog_service: DogService
    sheep_service: SheepService

    map_constraints: MapConstraints

    def __init__(self, map_constraints: MapConstraints):
        self.map_constraints = map_constraints

        self.sprites = pygame.sprite.Group()
        self.sprites.add(MapSprite())
    
    
    def update(self):
        self.dog_service: DogService = service_locator.get_service(DogService.__name__)
        self.sheep_service: SheepService = service_locator.get_service(SheepService.__name__)

        # constraint objects
        self.map_constraints.update(self.dog_service.dogs)
        self.map_constraints.update(self.sheep_service.sheeps)