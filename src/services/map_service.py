import pygame

from sprites.map_sprite import MapSprite
from services.dog_service import DogService
from services.sheep_service import SheepService
from services import service_locator
from models.map_constraints import MapConstraints


class MapService:
    sprites = pygame.sprite.Group
    map_constraints: MapConstraints

    def __init__(self, map_constraints: MapConstraints):
        self.map_constraints = map_constraints

        self.sprites = pygame.sprite.Group()
        self.sprites.add(MapSprite())
    
    def update(self):
        """
        Update map. Includes constraining the game objects to be inside the map boundaries.
        """

        # fetch services from service locator
        dog_service: DogService = service_locator.get_service(DogService.__name__)
        sheep_service: SheepService = service_locator.get_service(SheepService.__name__)

        # constraint objects to the map boundaries
        self.map_constraints.update(dog_service.dogs)
        self.map_constraints.update(sheep_service.sheeps)