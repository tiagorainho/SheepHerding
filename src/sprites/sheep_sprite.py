import pygame
from models.sheep import Sheep
from sprites.custom_sprite import CustomSprite


class SheepSprite(CustomSprite):

    sheep: Sheep
    
    def __init__(self, sheep: Sheep):
        super().__init__(size = 1.5)
        self.sheep = sheep

        self.image = pygame.Surface([self.scale*self.size, self.scale*self.size])
        self.rect = self.image.get_rect()
    

    def update(self):
        color = "green"
        self.image.fill(color = color)
        
        self.rect.x = self.sheep.position.x * self.scale
        self.rect.y = self.sheep.position.y * self.scale