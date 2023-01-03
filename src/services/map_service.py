

import pygame

from sprites.map_sprite import MapSprite
from services.dog_service import DogService
from services.sheep_service import SheepService
from services import service_locator
from classes.vector import Vector


BORDER_REPULSIVE_FORCE: float = 1
BORDER_MARGIN: float = 5

class MapService:

    # change to use a map [coordinates, sheep]
    sprites = pygame.sprite.Group

    game_grid: Vector

    dog_service: DogService
    sheep_service: SheepService
    height: int
    width: int

    def __init__(self, game_grid: Vector):
        self.game_grid = game_grid.copy()
        self.game_grid.x -= 1
        self.game_grid.y -= 1

        self.sprites = pygame.sprite.Group()

        map_sprite = MapSprite()
        self.sprites.add(map_sprite)
    
    def add_repulsive_force(self, obj , direction: Vector, repulsive_force = BORDER_REPULSIVE_FORCE):
        mag = direction.magnitude
        acceleration = direction.div(mag*mag).limit(repulsive_force)
        obj.position.sum(acceleration)
    
    def constrain_position(self, obj, border_margin = BORDER_MARGIN, repulsive_force = BORDER_REPULSIVE_FORCE):

        # fix x axis
        if obj.position.x > self.game_grid.x - border_margin:
            self.add_repulsive_force(obj, Vector(x = - abs(self.game_grid.x - obj.position.x), y = 0), repulsive_force=repulsive_force)

            if obj.position.x > self.game_grid.x:
                obj.position.x = self.game_grid.x

        if obj.position.x < border_margin:
            self.add_repulsive_force(obj, Vector(x = abs(obj.position.x), y = 0), repulsive_force=repulsive_force)

            if obj.position.x < 0:
                obj.position.x = 0
        
        # fix y axis
        if obj.position.y > self.game_grid.y - border_margin:
            self.add_repulsive_force(obj, Vector(x = 0, y = - abs(self.game_grid.y - obj.position.y)), repulsive_force=repulsive_force)

            if obj.position.y > self.game_grid.y:
                obj.position.y = self.game_grid.y

        if obj.position.y < border_margin:
            self.add_repulsive_force(obj, Vector(x = 0, y = abs(obj.position.y)), repulsive_force=repulsive_force)

            if obj.position.y < 0:
                obj.position.y = 0


    def update(self):
        self.dog_service: DogService = service_locator.get_service(DogService.__name__)
        self.sheep_service: SheepService = service_locator.get_service(SheepService.__name__)

        for dog in self.dog_service.dogs:
            self.constrain_position(dog)
        
        for sheep in self.sheep_service.sheeps:
            self.constrain_position(sheep)