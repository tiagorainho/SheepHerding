

import pygame

from time import time

from observers.achievements import Achievements

from sprites.score_board_sprite import ScoreBoardSprite
from sprites.score_sprite import ScoreSprite
from sprites.elapsed_time_sprite import ElapsedTimeSprite


class ScoreService:

    sprites = pygame.sprite.Group
    timer_sprite: ElapsedTimeSprite
    score_sprite: ScoreSprite

    score_board: Achievements
    level: int
    start_time: float

    def setup_static_sprites(self):
        self.score_sprite = ScoreSprite(level = self.level)
        self.timer_sprite = ElapsedTimeSprite(start_time=self.start_time)

    def __init__(self):
        self.sprites = pygame.sprite.Group()
        self.score_board = Achievements()
        self.level = 1
        self.start_time = time()
        self.setup_static_sprites()
    
    def increase_level(self):
        self.score_board = Achievements()
        self.level += 1
        self.start_time = time()
        self.setup_static_sprites()

    def update(self):
        self.sprites.empty()
        for corral, score in self.score_board.scores.items():
            self.sprites.add(ScoreBoardSprite(corral, score))

        self.sprites.add(self.score_sprite)
        self.sprites.add(self.timer_sprite)