import pygame
from sprites.custom_sprite import CustomSprite

class ScoreBoardSprite(CustomSprite):

    score: int
    font: pygame.font.SysFont
    font_size = 20
    
    def __init__(self, corral, score):
        super().__init__(size = 1)
        self.corral = corral
        self.score = score

        self.image = pygame.Surface([self.scale*self.size, self.scale*self.size])
        self.rect = self.image.get_rect()

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', self.font_size)

    def update(self):
        self.rect = pygame.Rect(
            self.corral.position.x*self.scale-self.font_size/2, 
            self.corral.position.y*self.scale-self.font_size/2, 
            self.width, 
            self.height
        )

        self.image = self.font.render(f"{self.score}", False, "black")
