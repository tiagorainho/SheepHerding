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
    alpha: int

    def update_image(self, sprite):
        if self.previous_sprite == sprite: return False

        img_rect = (0, 0, *REAL_IMAGE_SIZE)
        image_from_spritesheet = sprite.image_at(rectangle=img_rect, colorkey=-1)

        self.image_scaled = pygame.transform.scale(image_from_spritesheet, (self.scale*self.size, self.scale*self.size))

        self.previous_sprite = sprite

        return True
    
    def __init__(self, sheep: Sheep):
        super().__init__(size = 8)
        self.sheep = sheep

        self.image = pygame.Surface([self.scale*self.size, self.scale*self.size])
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.alpha = 255

        self.sprite_idx = 0
        self.previous_sprite = None

    def update(self):

        # update sheep position
        self.rect.centerx = self.sheep.position.x * self.scale
        self.rect.centery = self.sheep.position.y * self.scale

        # make sheep transparent
        if self.sheep.corral != None:
            self.alpha -= DELTA_TRANSPARENCY
            if self.alpha < 0:
                self.alpha = 0
                self.sheep.notify(entity=self.sheep, event=Event.ENTER_CORRAL, corral=self.sheep.corral)
                self.kill()
        else:
            self.alpha += DELTA_TRANSPARENCY
            if self.alpha > 255:
                self.alpha = 255
        self.image.set_alpha(self.alpha)

        # animate sheep
        sheep_velocity = self.sheep.velocity.magnitude
        if sheep_velocity == 0:
            sprite = self.sheep.sheep_model.rest_sprites()[0]
        else:
            running_sprites = self.sheep.sheep_model.run_right_sprites() if self.sheep.velocity.x >= 0 else self.sheep.sheep_model.run_left_sprites()

            sprite_update_velocity = sheep_velocity/SPRITE_COUNTER_DIVIDER
            self.sprite_idx = (self.sprite_idx + sprite_update_velocity) % len(running_sprites)
            sprite = running_sprites[int(self.sprite_idx)]

        # return if the sprite remains the same, no need to blit
        if not self.update_image(sprite): return
    
        # draw sheep image
        self.image.fill("white")
        self.image.set_colorkey("white")
        self.image.blit(
            self.image_scaled,
            (0, 0)
        )