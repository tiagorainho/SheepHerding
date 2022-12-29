

import pygame

from observers.achievements import Achievements
from sprites.score_board_sprite import ScoreBoardSprite
from sprites.score_sprite import ScoreSprite



class ScoreService:

    sprites = pygame.sprite.Group

    score_board: Achievements
    level: int

    def __init__(self):

        self.sprites = pygame.sprite.Group()
        self.score_board = Achievements()
        self.level = 1
    
    def increase_level(self):
        self.score_board = Achievements()
        self.level += 1

    def update(self):
        self.sprites.empty()
        for corral, score in self.score_board.scores.items():
            self.sprites.add(ScoreBoardSprite(corral, score))

        self.sprites.add(ScoreSprite(level = self.level))