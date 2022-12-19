from __future__ import division  # we need floating division
import pygame
from typing import List
from sprites.custom_sprite import CustomSprite



from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, parse_path


class MapSprite(CustomSprite):

    
    def __init__(self):
        super().__init__()

        svgpath = """m 76,232.24998 c 81.57846,-49.53502 158.19366,-20.30271 216,27 61.26714,
59.36905 79.86223,123.38417 9,156 
-80.84947,31.72743 -125.19991,-53.11474 -118,-91 v 0 """

        self.path = parse_path(svgpath)
        n = 100
        self.pts = [ (p.real,p.imag) for p in (self.path.point(i/n) for i in range(0, n+1))] 


        self.image = pygame.Surface([self.width * self.scale, self.height * self.scale])
        # self.rect = self.image.get_rect()
    

    def update(self):
        self.image.fill("white")
        pygame.draw.aalines( self.image,pygame.Color('blue'), False, self.pts)  # False is no closing
        pygame.display.update() # copy surface to display


        
        # for f in self.food:
        #     pygame.draw.rect(self.image, "green", (self.scale * f.x, self.scale * f.y, self.scale*self.size, self.scale*self.size))