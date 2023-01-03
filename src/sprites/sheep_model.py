
from sprites.sprites_model import SpriteModel

class SheepModel(SpriteModel):

    def run_left_sprites(self):
        return self.sprites["run_left"]

    def run_right_sprites(self):
        return self.sprites["run_right"]
    
    def rest_sprites(self):
        return [self.sprites["run_right"][0]]