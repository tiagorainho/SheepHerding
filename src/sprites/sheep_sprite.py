import pygame
from models.sheep import Sheep
from sprites.custom_sprite import CustomSprite
from enums.events import Event

DELTA_TRANSPARENCY = 10
REAL_IMAGE_SIZE = (300, 180)
SPRITE_COUNTER_DIVIDER = 5

class SheepSprite(CustomSprite):

    sheep: Sheep
    sprite_idx: int

    def update_image(self, sprite):
        img_rect = (0, 0, *REAL_IMAGE_SIZE)
        image_from_spritesheet = sprite.image_at(rectangle=img_rect, colorkey=-1)

        self.image_scaled = pygame.transform.scale(image_from_spritesheet, (self.scale*self.size, self.scale*self.size))
    
    def __init__(self, sheep: Sheep):
        super().__init__(size = 8)
        self.sheep = sheep

        self.image = pygame.Surface([self.scale*self.size, self.scale*self.size])
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.intensity = 255

        self.sprite_idx = 0
    

    def update(self):
        sheep_velocity = self.sheep.velocity.magnitude

        if sheep_velocity == 0:
            rest_sprite = self.sheep.sheep_model.run_right_sprites()[0]
            self.update_image(rest_sprite)
        else:
            running_sprites = self.sheep.sheep_model.run_right_sprites() if self.sheep.velocity.x >= 0 else self.sheep.sheep_model.run_left_sprites()

            sprite_update_velocity = sheep_velocity/SPRITE_COUNTER_DIVIDER
            self.sprite_idx = (self.sprite_idx + sprite_update_velocity) % len(running_sprites)
            self.update_image(running_sprites[int(self.sprite_idx)])

        if self.sheep.corral != None:
            color = [255,0,0]
            self.intensity -= DELTA_TRANSPARENCY
            if self.intensity < 0:
                self.intensity = 0
                self.sheep.notify(entity=self.sheep, event=Event.ENTER_CORRAL, corral=self.sheep.corral)
                self.kill()
        else:
            self.intensity += DELTA_TRANSPARENCY
            if self.intensity > 255:
                self.intensity = 255
        
        self.rect.x = (self.sheep.position.x - self.size/2) * self.scale
        self.rect.y = (self.sheep.position.y - self.size/2) * self.scale
    
        self.image.fill("white")
        self.image.set_colorkey("white")
        self.image.blit(
            self.image_scaled,
            (0, 0)
        )

        self.image.set_alpha(self.intensity)