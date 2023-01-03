import pygame
from models.dog import Dog
from sprites.custom_sprite import CustomSprite

REAL_IMAGE_SIZE = (400, 300)
NOT_SELECTED_ALPHA = 125
SELECTED_ALPHA = 255
SPRITE_COUNTER_DIVIDER = 5

class DogSprite(CustomSprite):

    dog: Dog
    sprite_idx: int

    def update_image(self, sprite):
        
        if self.previous_sprite == sprite: return False

        dog_img_rect = (0, 0, *REAL_IMAGE_SIZE)
        image_from_spritesheet = sprite.image_at(rectangle=dog_img_rect, colorkey=-1)

        self.dog_image_scaled = pygame.transform.scale(image_from_spritesheet, (self.scale*self.size, self.scale*self.size))

        self.previous_sprite = sprite

        return True
    
    def __init__(self, dog: Dog):
        super().__init__(size = 8)
        self.dog = dog

        self.image = pygame.Surface([self.scale*self.size, self.scale*self.size])
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.sprite_idx = 0
        self.previous_sprite = None
        
    def update(self):

        # update position
        self.rect.x = (self.dog.position.x - self.size/2) * self.scale
        self.rect.y = (self.dog.position.y - self.size/2) * self.scale

        # update alpha
        alpha = SELECTED_ALPHA if hasattr(self.dog, "selected") and self.dog.selected else NOT_SELECTED_ALPHA
        self.image.set_alpha(alpha)

        # used to update the sprites iteration velocity
        dog_velocity = self.dog.velocity.magnitude

        # update sprite
        if dog_velocity == 0:
            rest_sprite = self.dog.dog_model.rest_sprites()[0]
            
            # return if the sprite remains the same, no need to blit
            if not self.update_image(rest_sprite): return
            
        else:
            running_sprites = self.dog.dog_model.run_right_sprites() if self.dog.velocity.x >= 0 else self.dog.dog_model.run_left_sprites()

            sprite_update_velocity = dog_velocity/SPRITE_COUNTER_DIVIDER
            self.sprite_idx = (self.sprite_idx + sprite_update_velocity) % len(running_sprites)

            # return if the sprite remains the same, no need to blit
            if not self.update_image(running_sprites[int(self.sprite_idx)]): return
        
        self.image.fill("white")
        self.image.set_colorkey("white")
        self.image.blit(
            self.dog_image_scaled,
            (0, 0)
        )