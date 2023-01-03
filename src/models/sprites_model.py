
import os
from typing import Dict, List
from sprites.spritesheet import SpriteSheet
from collections import defaultdict

ALLOWED_EXTENSIONS = ["png", "jpeg"]

class SpriteModel:
    
    sprites: Dict[str, List[SpriteSheet]]

    def __init__(self, dir_name: str):

        self.sprites = defaultdict(list)

        for folder in os.scandir(dir_name):
            if not folder.is_dir(): continue

            sprite_files = []
        
            for file in os.scandir(f"{dir_name}/{folder.name}"):
                if not file.is_file(): continue
                if not any(ext in file.name for ext in ALLOWED_EXTENSIONS): continue
                
                sprite_files.append(file.path)

            for file_name in sorted(sprite_files):
                self.sprites[folder.name].append(SpriteSheet(filename=file_name))