from __future__ import annotations

import pygame

from singletons import service_locator
from sprites.corral_sprite import CorralSprite
from classes.vector import Vector
from services.sheep_service import SheepService
from models.corral import Corral
from typing import List

class CorralService:

    sprites = pygame.sprite.Group
    sheep_service: SheepService

    game_grid: Vector

    def __init__(self, game_grid: Vector):
        self.game_grid = game_grid
        self.sprites = pygame.sprite.Group()
        
    
    def add_corral(self, corral: Corral):
        self.sprites.add(CorralSprite(corral=corral))
    
    def clear_corrals(self):
        self.sprites.empty()

    @property
    def corrals(self) -> List[Corral]:
        return [sprite.corral for sprite in self.sprites.sprites()]
    
    def update(self):
        self.sheep_service: SheepService = service_locator.get_service('sheep_service')
        sheeps = self.sheep_service.sheeps

        corrals = self.corrals
        for corral in corrals:
            corral.update(sheeps)