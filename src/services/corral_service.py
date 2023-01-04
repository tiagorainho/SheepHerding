from __future__ import annotations

import pygame

from services import service_locator
from sprites.corral_sprite import CorralSprite
from utils.math.vector import Vector
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
        """
        Spawn a new corral
        """
        
        self.sprites.add(CorralSprite(corral=corral))
    
    def clear_corrals(self):
        """
        Clear all available corrals
        """
        
        self.sprites.empty()

    @property
    def corrals(self) -> List[Corral]:
        """
        Get all available corrals
        """
        
        return [sprite.corral for sprite in self.sprites.sprites()]
    
    def update(self):
        """
        Update the corrals states
        """
        
        # fetch sheeps from sheep service
        self.sheep_service: SheepService = service_locator.get_service(SheepService.__name__)
        sheeps = self.sheep_service.sheeps

        # update corrals based on sheeps
        corrals = self.corrals
        for corral in corrals:
            corral.update(sheeps)