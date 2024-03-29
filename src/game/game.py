from typing import DefaultDict
from collections import defaultdict
from game.game_configs import FPS

import pygame

class Game:
    """
    Game Engine wrapper, a specific game should extend this class.
    """

    clock: pygame.time.Clock
    fps: int
    display: pygame.display
    screen: pygame.Surface
    running: bool
    scale: int
    height: int
    width: int
    scale: int
    
    sprites: DefaultDict[str, pygame.sprite.Group]

    def __init__(self, height: int, width: int, scale: int):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.scale = scale
        self.height = height*self.scale
        self.width = width*self.scale
        self.display = pygame.display.set_mode((self.width, self.height))
        self.screen = pygame.Surface((self.width, self.height))
        self.fps = FPS
        self.sprites = defaultdict(pygame.sprite.Group)
        
        pygame.mixer.init()
        pygame.mixer.stop()
    
    def update(self, events):
        raise NotImplementedError()

    def start(self):
        self.run(self.update)

    def run(self, update_function):
        """
        Game Loop. This is where the inputs are processed, the game is updated and the screen is rendered.
        """

        self.running = True

        while self.running:
            
            # get events
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    return
            
            # update game with the new events
            update_function(events)

            # render window
            self.screen.fill("white")
            self.render_sprites()

            # update display
            pygame.Surface.blit(self.display, self.screen, (0,0))
            pygame.display.flip()

            self.clock.tick(self.fps)
        
    def render_sprites(self):
        """
        Render sprite groups from the sprites variable.
        """
        
        for group in self.sprites.values():
            group.update()
            group.draw(self.screen)