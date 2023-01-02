import pygame


from typing import List
from random import randint

from game.game import Game

from models.sheep import Sheep
from models.dog import Dog
from models.corral import Corral, MAX_CORRAL_RADIUS, MIN_CORRAL_RADIUS
from models.dog_model import DogModel

from singletons import service_locator
from services.sheep_service import SheepService
from services.dog_service import DogService
from services.map_service import MapService
from services.corral_service import CorralService
from services.score_service import ScoreService

from classes.vector import Vector
from singletons.game_configs import SCREEN_WIDTH, SCREEN_HEIGHT, SCALE
from commands.input_handler import InputHandler

NUMBER_OF_SHEEP = 10
NUMBER_OF_DOGS = 3
MIN_CORRAL_DISTANCE_FROM_BORDER = 25
DECREASE_RADIUS_BY_LEVEL = 2


KEY_DIRECTION = {
    pygame.K_UP: Vector(0, -1),
    pygame.K_DOWN: Vector(0, 1),
    pygame.K_LEFT: Vector(-1, 0),
    pygame.K_RIGHT: Vector(1, 0),
}


class SheepGame(Game):

    sheep_service: SheepService
    dog_service: DogService
    corral_service: CorralService
    map_service: MapService
    score_service: ScoreService
    input_handler: InputHandler

    def add_level(self):

        level = self.score_service.level

        dog_model = DogModel("assets/images/dog")
        # add dogs to its service
        for _ in range(NUMBER_OF_DOGS):
            self.dog_service.add_dog(
                Dog(
                    position=Vector(x = self.game_grid.x/2, y = self.game_grid.y/2),
                    dog_model=dog_model
                )
            )
        self.dog_service.select(self.dog_service.dogs[0])

        # add sheeps to its service
        for _ in range(NUMBER_OF_SHEEP + (level-1) * DECREASE_RADIUS_BY_LEVEL):
            new_sheep = Sheep(
                    position=Vector(randint(0, self.game_grid.x), randint(0, self.game_grid.y)),
                    velocity=Vector(randint(-1, 1), randint(-1, 1)),
                )

            new_sheep.add_observer(obs=self.score_service.score_board)
            self.sheep_service.add_sheep(
                new_sheep
            )
        
        # add corral
        self.corral_service.clear_corrals()

        corral_radius = max(MIN_CORRAL_RADIUS, MAX_CORRAL_RADIUS - level)
        min_distance_to_border = MIN_CORRAL_DISTANCE_FROM_BORDER + corral_radius
        corral_position = Vector(
            randint(min_distance_to_border, self.game_grid.x-min_distance_to_border), 
            randint(min_distance_to_border, self.game_grid.y-min_distance_to_border)
        )
        corral = Corral(corral_position, corral_radius)
        self.corral_service.add_corral(corral=corral)


    def __init__(self):
        self.game_grid = Vector(SCREEN_WIDTH/SCALE, SCREEN_HEIGHT/SCALE)
        super().__init__(width = self.game_grid.x, height = self.game_grid.y, scale = SCALE)

        self.input_handler = InputHandler(self)
        
        self.score_service: ScoreService = service_locator.registry(
            name="scores_service",
            service=ScoreService()
        )
        self.sprites['scores'] = self.score_service.sprites

        self.map_service: MapService = service_locator.registry(
            name="map_service",
            service=MapService(self.game_grid)
        )
        self.sprites['map'] = self.map_service.sprites

        self.corral_service: CorralService = service_locator.registry(
            name="corral_service",
            service=CorralService(self.game_grid)
        )
        self.sprites['corral'] = self.corral_service.sprites


        # registry dog service
        self.dog_service: DogService = service_locator.registry(
            name="dog_service", 
            service=DogService()
        )
        self.sprites[Dog.__name__] = self.dog_service.sprites

        # registry sheep service
        self.sheep_service: SheepService = service_locator.registry(
            name="sheep_service", 
            service=SheepService()
        )
        self.sprites[Sheep.__name__] = self.sheep_service.sprites

        self.add_level()
        
    def update(self, events: List[pygame.event.Event]):
        """
        Game logic
        """

        # handle events
        exec_commands, undo_commands = self.input_handler.handle_input(events)

        # execute commands
        for command in exec_commands:
            command.execute(game=self)

        # undo commands
        for command in undo_commands:
            command.undo()
            

        # controll selected dog
        keys = pygame.key.get_pressed()
        direction = Vector(0,0)
        for key, vector in KEY_DIRECTION.items():
            if keys[key]:
                direction.sum(vector)
        direction.normalize()

        self.corral_service.update()

        self.dog_service.selected_dog.accelerate(direction)

        # update objects state
        self.sheep_service.update()
        self.dog_service.update()

        # update map
        self.map_service.update()
        self.score_service.update()

        # level up
        if self.score_service.score_board.total_score >= NUMBER_OF_SHEEP:
            self.score_service.increase_level()
            self.add_level()