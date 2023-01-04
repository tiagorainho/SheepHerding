
import pygame
from game.game_configs import SCREEN_HEIGHT, SCREEN_WIDTH, SCALE

class CustomSprite(pygame.sprite.Sprite):
    """
    Default Sprite which sets the most basic properties such as:
        - height
        - width
        - scale
        - size
    """

    height: int
    width: int
    scale: int
    size: float


    def __init__(self, size: float = 1):
        pygame.sprite.Sprite.__init__(self)

        self.height = SCREEN_HEIGHT
        self.width = SCREEN_WIDTH
        self.scale = SCALE
        self.size = size