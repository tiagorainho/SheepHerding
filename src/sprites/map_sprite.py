import pygame
from sprites.custom_sprite import CustomSprite

COLOR = (100, 250,10)
ALPHA = 50

class MapSprite(CustomSprite):

    def __init__(self):
        super().__init__(size=1)
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.image.fill(COLOR)
        self.image.set_alpha(ALPHA)

    def update(self):
        pass