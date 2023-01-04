import pygame
import os

DEFAULT_VOLUME = 0.5

class SoundService:
    win_gold_sound: pygame.mixer.Sound
    background_sound: pygame.mixer.Sound

    def __init__(self, audios_dir):
        self.win_gold_sound = pygame.mixer.Sound(os.path.join(audios_dir, 'win_gold.wav'))
        self.background_sound = pygame.mixer.Sound(os.path.join(audios_dir, 'background.wav'))

    def play_win_gold(self, volume = DEFAULT_VOLUME):
        """
        Play a "winning gold" sound once.
        """
        
        self.win_gold_sound.set_volume(volume)
        self.win_gold_sound.play(fade_ms=100)
    
    def play_background(self):
        """
        Play a soundtrack indefinitely.
        """
        
        self.background_sound.set_volume(DEFAULT_VOLUME)
        self.background_sound.play(loops=-1)