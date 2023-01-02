import pygame
from sprites.custom_sprite import CustomSprite

class ScoreSprite(CustomSprite):

    level: int
    font: pygame.font.SysFont
    font_size = 20
    
    def __init__(self, level):
        super().__init__(size = 1)
        self.level = level

        self.image = pygame.Surface([self.scale*self.size, self.scale*self.size])
        
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', self.font_size)
        self.rect = pygame.Rect(10, 5, self.width, self.height)
        
    def update(self):
        self.image = self.font.render(f"Level: {self.level}", False, "black")