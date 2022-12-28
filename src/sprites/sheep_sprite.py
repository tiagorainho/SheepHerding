import pygame
from models.sheep import Sheep
from sprites.custom_sprite import CustomSprite
from enums.events import Event

DELTA_TRANSPARENCY = 10

class SheepSprite(CustomSprite):

    sheep: Sheep
    
    def __init__(self, sheep: Sheep):
        super().__init__(size = 1.5)
        self.sheep = sheep

        self.image = pygame.Surface([self.scale*self.size, self.scale*self.size])
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.intensity = 255
    

    def update(self):
        color = [0,255,0]
        if self.sheep.corral != None:
            color = [255,0,0]
            self.intensity -= DELTA_TRANSPARENCY
            if self.intensity < 0:
                self.intensity = 0
                self.sheep.notify(entity=self.sheep, event=Event.ENTER_CORRAL, corral=self.sheep.corral)
                self.kill()
        else:
            self.intensity += DELTA_TRANSPARENCY
            if self.intensity > 255:
                self.intensity = 255
        
        self.image.fill(tuple(color + [self.intensity]))
        
        self.rect.x = self.sheep.position.x * self.scale
        self.rect.y = self.sheep.position.y * self.scale