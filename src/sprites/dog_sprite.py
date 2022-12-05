import pygame
from models.dog import Dog
from sprites.custom_sprite import CustomSprite


class DogSprite(CustomSprite):

    dog: Dog
    
    def __init__(self, dog: Dog):
        super().__init__(size = 1)
        self.dog = dog

        self.image = pygame.Surface([self.scale*self.size, self.scale*self.size])
        self.rect = self.image.get_rect()

    def update(self):

        color = "blue" if self.dog.selected else "red"
        self.image.fill(color = color)
        
        self.rect.x = self.dog.position.x * self.scale
        self.rect.y = self.dog.position.y * self.scale