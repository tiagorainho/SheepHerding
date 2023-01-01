import pygame
from models.dog import Dog
from sprites.custom_sprite import CustomSprite

REAL_IMAGE_SIZE = (520, 400)
NOT_SELECTED_ALPHA = 150
SELECTED_ALPHA = 255

class DogSprite(CustomSprite):

    dog: Dog
    
    def __init__(self, dog: Dog):
        super().__init__(size = 8)
        self.dog = dog

        self.image = pygame.Surface([self.scale*self.size, self.scale*self.size])
        self.image.convert_alpha()

        self.rect = self.image.get_rect()

        # setup dog sprites
        dog_img_rect = (0, 0, *REAL_IMAGE_SIZE)
        dog_sprite = self.dog.dog_model.dog_sprites[0] #.run_side_sprites()[0]

        image_from_spritesheet = dog_sprite.image_at(rectangle=dog_img_rect, colorkey=-1)
        self.dog_image_scaled = pygame.transform.scale(image_from_spritesheet, (self.scale*self.size, self.scale*self.size))

        
    def update(self):
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
        