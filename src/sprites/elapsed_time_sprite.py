import pygame
from sprites.custom_sprite import CustomSprite
from time import time


class ElapsedTimeSprite(CustomSprite):

    font: pygame.font.SysFont
    font_size = 20
    start_time: float
    
    def __init__(self, start_time):
        super().__init__(size = 1)
        self.start_time = start_time

        self.image = pygame.Surface([self.scale*self.size, self.scale*self.size])
        
        self.font = pygame.font.SysFont('Comic Sans MS', self.font_size)
        self.rect = pygame.Rect(self.width, 5, self.width, self.height)
        
    def update(self):
        elapsed_time = time()-self.start_time
        time_str = f"{int(elapsed_time//60)}:{round((elapsed_time%60), 1)}"

        self.image = self.font.render(time_str, False, "black")
        self.rect.x = self.width - 10 - len(time_str)*10