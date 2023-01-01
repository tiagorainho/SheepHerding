import os
from typing import List
from sprites.spritesheet import SpriteSheet

class DogModel:
    
    dog_sprites: List[SpriteSheet]

    def __init__(self, dir_name: str = "images/dog"):
        
        file_names = [file_name for file_name in os.listdir(dir_name) if ".png" in file_name]

        self.dog_sprites = [SpriteSheet(filename=f"{dir_name}/{file_name}") for file_name in file_names]

    
    def run_side_sprites(self):
        return self.dog_sprites[5:6]

    def run_back_sprites(self):
        return self.dog_sprites[9:10]
    
    def run_front_sprites(self):
        return self.dog_sprites[7:8]
    
    def stop_sprites(self):
        return self.dog_sprites[1:4]
