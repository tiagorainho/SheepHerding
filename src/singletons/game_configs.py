
def screen_dimensions():
    import pygame

    # get width and height from pygame
    pygame.init()
    info = pygame.display.Info()
    width, height = info.current_w,info.current_h

    # decrease a bit the height because of the top bar (otherwise it would hide the bottom area)
    height -= 30

    return width, height


SCREEN_WIDTH, SCREEN_HEIGHT = screen_dimensions()
SCALE: int = 5