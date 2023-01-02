import pygame
from models.dog import Dog
from sprites.custom_sprite import CustomSprite

REAL_IMAGE_SIZE = (400, 300)
NOT_SELECTED_ALPHA = 150
SELECTED_ALPHA = 255
SPRITE_COUNTER_DIVIDER = 2

class DogSprite(CustomSprite):

    dog: Dog
    sprite_idx: int

    def update_image(self, sprite):
        dog_img_rect = (0, 0, *REAL_IMAGE_SIZE)
        image_from_spritesheet = sprite.image_at(rectangle=dog_img_rect, colorkey=-1)

        self.dog_image_scaled = pygame.transform.scale(image_from_spritesheet, (self.scale*self.size, self.scale*self.size))
    
    def __init__(self, dog: Dog):
        super().__init__(size = 5)
        self.dog = dog

        self.image = pygame.Surface([self.scale*self.size, self.scale*self.size])
        self.image.convert_alpha()

        self.rect = self.image.get_rect()

        self.sprite_idx = 0
        

    def update(self):

        dog_velocity = self.dog.velocity.magnitude

        if dog_velocity == 0:
            rest_sprite = self.dog.dog_model.rest_sprites()[0]
            self.update_image(rest_sprite)
        else:
            running_sprites = self.dog.dog_model.run_right_sprites() if self.dog.velocity.x >= 0 else self.dog.dog_model.run_left_sprites()

            velocity = dog_velocity/SPRITE_COUNTER_DIVIDER
            self.sprite_idx = (self.sprite_idx + velocity) % len(running_sprites)
            self.update_image(running_sprites[int(self.sprite_idx)])

        self.rect.x = (self.dog.position.x - self.size/2) * self.scale
        self.rect.y = (self.dog.position.y - self.size/2) * self.scale
        
        self.image.fill("white")
        self.image.set_colorkey("white")
        self.image.blit(
            self.dog_image_scaled,
            (0, 0)
        )

        alpha = SELECTED_ALPHA if hasattr(self.dog, "selected") and self.dog.selected else NOT_SELECTED_ALPHA

        self.image.set_alpha(alpha)