import pygame
from typing import List
from models.sheep import Sheep
from sprites.custom_sprite import CustomSprite


class SheepSprite(CustomSprite):

    sheep: Sheep
    
    def __init__(self, sheep: Sheep, width: int, height: int, scale: int):
        super().__init__(width=width, height=height, scale=scale, size = 2)
        self.sheep = sheep

        self.image = pygame.Surface([scale*self.size, scale*self.size])
        self.rect = self.image.get_rect()
    

    def update(self):
        color = "green"
        self.image.fill(color = color)
        
        self.rect.x = self.sheep.position.x * self.scale
        self.rect.y = self.sheep.position.y * self.scale