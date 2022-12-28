import pygame
from sprites.custom_sprite import CustomSprite


class MapSprite(CustomSprite):

    def __init__(self):
        super().__init__(size=1)
        self.image = pygame.Surface([0,0])
        self.rect = self.image.get_rect()

    def update(self):
        pass