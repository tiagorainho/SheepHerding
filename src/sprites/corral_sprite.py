import pygame
from sprites.custom_sprite import CustomSprite
from models.corral import Corral

COLOR = (100, 250, 10)

class CorralSprite(CustomSprite):

    corral: Corral

    def __init__(self, corral: Corral):
        super().__init__(size=corral.radius)

        self.corral = corral

        length = self.scale*self.size*2
        self.image = pygame.Surface([length, length])
        
        # make transparent
        self.image.set_alpha(128)

        # draw circle
        self.rect = pygame.draw.circle(surface=self.image, color=COLOR, center=(self.size*self.scale, self.size*self.scale), radius=self.size*self.scale)

        # set corral position
        self.rect.centerx = self.corral.position.x * self.scale
        self.rect.centery = self.corral.position.y * self.scale

    def update(self):
        pass