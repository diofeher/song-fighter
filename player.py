import pygame
from pygame.locals import *
import time


class Player(object):
    
    def load_sound(self, full_path):
        
        try:
            self.music = pygame.mixer.Sound(full_path)
        except pygame.error, message:
            print 'Cannot load sound:', wav
            raise SystemExit, message
        return self.music
    
    def play(self):
        self.music.play()
        time.sleep(10)
        self.music.fadeout()
        