import pygame
from models.dog import Dog
from sprites.custom_sprite import CustomSprite

# REAL_IMAGE_SIZE = (1080, 720) # dog_old_sprites
REAL_IMAGE_SIZE = (400, 300) # dog
NOT_SELECTED_ALPHA = 125
SELECTED_ALPHA = 255
SPRITE_COUNTER_DIVIDER = 5

ALPHA = (0, 255, 0)

class DogSprite(CustomSprite):

    dog: Dog
    sprite_idx: int

    def update_image(self, sprite):
        
        if self.previous_sprite == sprite: return False

        dog_img_rect = (0, 0, *REAL_IMAGE_SIZE)
        image_from_spritesheet = sprite.image_at(rectangle=dog_img_rect, colorkey=ALPHA)

        self.dog_image_scaled = pygame.transform.scale(image_from_spritesheet, (self.scale*self.size, self.scale*self.size))

        self.previous_sprite = sprite

        return True
    
    def __init__(self, dog: Dog):
        super().__init__(size = 8)
        self.dog = dog

        self.image = pygame.Surface([self.scale*self.size, self.scale*self.size], pygame.SRCALPHA)
        self.image.set_colorkey(ALPHA, pygame.RLEACCEL)
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

        # update sprite model dependent on velocity and direction
        if dog_velocity == 0:
            # rest sprites
            sprites = self.dog.dog_model.rest_sprites()

            # animate sprites
            sprite_update_velocity = 2.5/SPRITE_COUNTER_DIVIDER
            self.sprite_idx = (self.sprite_idx + sprite_update_velocity)
            if self.sprite_idx > len(sprites)-1:
                self.sprite_idx = len(sprites)-1
        else:
            # running sprites
            sprites = self.dog.dog_model.run_right_sprites() if self.dog.velocity.x >= 0 else self.dog.dog_model.run_left_sprites()
            
            # animate sprites
            sprite_update_velocity = dog_velocity/SPRITE_COUNTER_DIVIDER
            self.sprite_idx = (self.sprite_idx + sprite_update_velocity) % len(sprites)

        # return if the sprite remains the same, no need to blit
        if not self.update_image(sprites[int(self.sprite_idx)]): return
        
        self.image.fill("blue")
        self.image.set_colorkey("blue")
        self.image.blit(
            self.dog_image_scaled,
            (0, 0)
        )