import pygame
from sprites.custom_sprite import CustomSprite
from models.corral import Corral


class CorralSprite(CustomSprite):

    corral: Corral

    def __init__(self, corral: Corral):
        super().__init__(size=corral.radius)

        self.corral = corral
        self.color = (100, 255, 10)

        length = self.scale*self.size*2
        self.image = pygame.Surface([length, length])
        
        # make transparent
        self.image.set_alpha(128)

        self.image.fill((255, 255, 255))
        pygame.draw.circle(surface=self.image, color=self.color, center=(self.size*self.scale, self.size*self.scale), radius=self.size*self.scale)

        self.rect = self.image.get_rect()
        self.rect.center = (self.corral.position.x * self.scale, self.corral.position.y * self.scale)
        

    def update(self):
        pass
        