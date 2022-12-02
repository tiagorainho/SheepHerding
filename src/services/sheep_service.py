
from typing import List

from models.sheep import Sheep

from sprites.sheep_sprite import SheepSprite
import pygame

from singletons import game_configs

from collections import defaultdict

class SheepService:

    # change to use a map [coordinates, sheep]
    sprites = pygame.sprite.Group

    def __init__(self, sprite_group: pygame.sprite.Group):
        self.sprites = sprite_group

    @property
    def sheeps(self) -> List[Sheep]:
        return [sprite.sheep for sprite in self.sprites.sprites()]

    def add_sheep(self, sheep: Sheep):
        self.sprites.add(SheepSprite(sheep=sheep, width=game_configs.width, height=game_configs.height, scale=game_configs.scale))
    
    def update(self):
        
        sheeps = self.sheeps

        # get closest sheep
        neighbors = defaultdict(list)
        for sheep in sheeps:
            neighbors[sheep] = []
            for sheep2 in sheeps:
                if sheep == sheep2: continue
                if sheep.position.distance(sheep2.position) < 100:
                    neighbors[sheep].append(sheep2)
        
        # 
        for sheep, closest_sheeps in neighbors.items():
            sheep.update(closest_sheeps)