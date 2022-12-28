

import pygame

from observers.achievements import Achievements
from sprites.score_board_sprite import ScoreBoardSprite



class ScoreService:

    sprites = pygame.sprite.Group

    score_board: Achievements

    def __init__(self):

        self.sprites = pygame.sprite.Group()
        self.score_board = Achievements()

    def update(self):
        self.sprites.empty()
        for corral, score in self.score_board.scores.items():
            self.sprites.add(ScoreBoardSprite(corral, score))