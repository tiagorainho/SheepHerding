
import pygame

from typing import List
from random import randint

from game.game import Game

from models.sheep import Sheep
from models.dog import Dog

from singletons import service_locator
from services.sheep_service import SheepService
from services.dog_service import DogService

from classes.vector import Vector
from singletons.game_configs import SCREEN_WIDTH, SCREEN_HEIGHT, SCALE

NUMBER_OF_SHEEP = 20
NUMBER_OF_DOGS = 2

KEY_DIRECTION = {
    pygame.K_UP: Vector(0, -1),
    pygame.K_DOWN: Vector(0, 1),
    pygame.K_LEFT: Vector(-1, 0),
    pygame.K_RIGHT: Vector(1, 0)
}

class SheepGame(Game):

    sheep_service: SheepService
    dog_service: DogService


    def __init__(self):
        self.game_grid = Vector(SCREEN_WIDTH/SCALE, SCREEN_HEIGHT/SCALE)
        super().__init__(width = self.game_grid.x, height = self.game_grid.y, scale = SCALE)

        # registry dog service
        self.dog_service: DogService = service_locator.registry(
            name="dog_service", 
            service=DogService
        )
        self.sprites[Dog.__name__] = self.dog_service.sprites

        # registry sheep service
        self.sheep_service: SheepService = service_locator.registry(
            name="sheep_service", 
            service=SheepService
        )
        self.sprites[Sheep.__name__] = self.sheep_service.sprites

        # add dog to its service
        for _ in range(NUMBER_OF_DOGS):
            self.dog_service.add_dog(
                Dog(position=Vector(x = self.game_grid.x/2, y = self.game_grid.y/2))
            )
        self.dog_service.select(self.dog_service.dogs[0])

        # add sheeps to its service
        for _ in range(NUMBER_OF_SHEEP):
            self.sheep_service.add_sheep(
                Sheep(
                    position=Vector(randint(0, self.game_grid.x), randint(0, self.game_grid.y)),
                    velocity=Vector(randint(-1, 1), randint(-1, 1)),
                )
            )

    

    def update(self, events: List[pygame.event.Event]):
        """
        Game logic
        """

        # handle events
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    idx = self.dog_service.dogs.index(self.dog_service.selected_dog)
                    self.dog_service.select(self.dog_service.dogs[(idx+1)%len(self.dog_service.dogs)])


        # controll dog
        keys = pygame.key.get_pressed()
        direction = Vector(0,0)
        for key, vector in KEY_DIRECTION.items():
            if keys[key]:
                direction.sum(vector)
        direction.normalize()


        self.dog_service.selected_dog.move(direction)

        # update objects state
        self.sheep_service.update()
        self.dog_service.update()
            