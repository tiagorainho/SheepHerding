
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
        
            for file in os.scandir(f"{dir_name}/{folder.name}"):
                if not file.is_file(): continue
                if not any(ext in file.name for ext in ALLOWED_EXTENSIONS): continue

                self.sprites[folder.name].append(SpriteSheet(filename=file.path))
