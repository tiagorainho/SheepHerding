
import pygame
import numpy as np

from typing import List
from random import randint


from models.sheep import Sheep

from game.game import Game

from classes.vector import Vector

from services.sheep_service import SheepService

NUMBER_OF_SHEEP = 20

class SheepGame(Game):

    sheep_service: SheepService


    def __init__(self, width: int, height: int, scale: int):
        self.game_grid = (width/scale, height/scale)
        super().__init__(height = self.game_grid[1], width = self.game_grid[0], scale = scale)

        # create sheep
        self.sheep_service = SheepService(sprite_group=self.sprites[Sheep.__class__.__str__])
        for _ in range(NUMBER_OF_SHEEP):
            self.sheep_service.add_sheep(
                Sheep(
                    position=Vector(randint(0, self.game_grid[0]), randint(0, self.game_grid[1])),
                    velocity=Vector(randint(-1, 1), randint(-1, 1)),
                )
            )
        

    

    def update(self, events: List[pygame.event.Event]):
        """
        Game logic
        """

        # TO DO: press scape to switch simulation settings
        # handle events
        # for event in events:


        # update sheep state
        self.sheep_service.update()
            