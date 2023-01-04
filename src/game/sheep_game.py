import pygame

from typing import List
from random import randint, seed

from game.game import Game

from models.sheep import Sheep, SheepBreed
from sprites.sheep_model import SheepModel
from models.dog import Dog, DogBreed
from sprites.dog_model import DogModel
from models.corral import Corral, MAX_CORRAL_RADIUS, MIN_CORRAL_RADIUS
from models.map_constraints import MapConstraints

from services.sheep_service import SheepService
from services.dog_service import DogService
from services.map_service import MapService
from services.corral_service import CorralService
from services.score_service import ScoreService

from utils.math.vector import Vector
from utils.math.geometry import circle_points

from services.service_locator import ServiceLocator
from game.game_configs import SCREEN_WIDTH, SCREEN_HEIGHT, SCALE
from services.sound_service import SoundService

from commands.input_handler import InputHandler

NUMBER_OF_SHEEP = 10
NUMBER_OF_DOGS = 2
MIN_CORRAL_DISTANCE_FROM_BORDER = 25
DECREASE_RADIUS_BY_LEVEL = 2


class SheepGame(Game):

    sheep_service: SheepService
    dog_service: DogService
    corral_service: CorralService
    map_service: MapService
    score_service: ScoreService
    sound_service: SoundService

    input_handler: InputHandler

    dog_model: DogModel
    sheep_model: SheepModel

    def set_level(self, level: int):
        """
        Set the models such as the dogs, sheeps and corrals in the level it receives. Also, the random seed is also set to the level it receives in order to maintain all the levels equal.
        """
        
        # set seed dependent on level, therefore the levels are always the same
        seed(level)

        middle_screen = Vector(x = self.game_grid.x/2, y = self.game_grid.y/2)

        # clear dogs
        self.dog_service.clear_dogs()

        # add new dogs for each level
        number_of_dogs_level = NUMBER_OF_DOGS + (level-1)

        # create circles in a circular way
        circular_radius = number_of_dogs_level*1.5 + 2
        circular_coordinates = circle_points(radius=circular_radius, number_of_points=number_of_dogs_level)

        # add dogs to its service
        dog_breed: DogBreed = DogBreed()
        for circular_vector in circular_coordinates:
            dog_start_position = middle_screen.copy().sum(circular_vector)
            self.dog_service.spawn(
                Dog(
                    position=dog_start_position,
                    dog_model=self.dog_model,
                    breed=dog_breed
                )
            )
        self.dog_service.select(self.dog_service.dogs[0])

        # add sheeps to its service
        sheep_breed: SheepBreed = SheepBreed()
        for _ in range(NUMBER_OF_SHEEP + (level-1) * DECREASE_RADIUS_BY_LEVEL):
            new_sheep = Sheep(
                    position=Vector(randint(0, self.game_grid.x), randint(0, self.game_grid.y)),
                    velocity=Vector(randint(-1, 1), randint(-1, 1)),
                    sheep_model=self.sheep_model,
                    sheep_breed=sheep_breed
                )

            new_sheep.add_observer(obs=self.score_service.score_board)
            self.sheep_service.spawn(sheep=new_sheep)
        
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
        """
        Initiate the SheepGame services, sprite groups, models, input handler and set the initial level.
        """
        self.game_grid = Vector(SCREEN_WIDTH/SCALE, SCREEN_HEIGHT/SCALE)
        super().__init__(width = self.game_grid.x, height = self.game_grid.y, scale = SCALE)
        
        service_locator = ServiceLocator.get_instance()

        # registry score service
        self.score_service: ScoreService = service_locator.registry(service=ScoreService())
        self.sprites['score'] = self.score_service.sprites

        # registry map service
        map_constraints = MapConstraints(self.game_grid)
        self.map_service: MapService = service_locator.registry(service=MapService(map_constraints))
        self.sprites['map'] = self.map_service.sprites

        # registry corral service
        self.corral_service: CorralService = service_locator.registry(service=CorralService(self.game_grid))
        self.sprites[Corral.__name__] = self.corral_service.sprites

        # registry dog service
        self.dog_service: DogService = service_locator.registry(service=DogService())
        self.sprites[Dog.__name__] = self.dog_service.sprites

        # registry sheep service
        self.sheep_service: SheepService = service_locator.registry(service=SheepService())
        self.sprites[Sheep.__name__] = self.sheep_service.sprites

        # registry sound service
        self.sound_service: SoundService = service_locator.registry(service=SoundService("assets/sounds"))
        self.sound_service.play_background()

        # instantiate sprite models
        self.dog_model = DogModel("assets/images/dog")
        self.sheep_model = SheepModel("assets/images/sheep")

        # instantiate input handler
        self.input_handler = InputHandler(self)

        self.set_level(self.score_service.level)
        
    def update(self, events: List[pygame.event.Event]):
        """
        SheepGame logic.
        """

        # handle events by converting them into commands
        exec_commands, undo_commands = self.input_handler.handle_input(events)

        # execute commands
        for command in exec_commands:
            command.execute()

        # undo commands
        for command in undo_commands:
            command.undo()

        # update objects state
        self.sheep_service.update()
        self.dog_service.update()

        # update map
        self.map_service.update()
        self.score_service.update()
        self.corral_service.update()

        # level up
        if self.score_service.score_board.total_score >= NUMBER_OF_SHEEP:
            self.score_service.increase_level()
            self.set_level(self.score_service.level)