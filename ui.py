from pygame.locals import *
import pygame
import os
import sys

def load_image(name, colorkey=None):
    ''' From http://www.pygame.org/docs/tut/chimp/chimp.py.html '''
    fullname = os.path.join('imgs', name)

    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message

    image = image.convert()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)

    return image, image.get_rect()

class Ui(object):

    def __init__(self):
        pygame.init()

        screen = pygame.display.set_mode((600,451))

        pygame.display.set_caption("Toughtworks - Songs Fighter!")
        pygame.mouse.set_visible(1)

        background = load_image("background.png")

        screen.blit(background[0], (0,0))
        pygame.display.flip()

        if pygame.font:
            font = pygame.font.Font(None, 48)
            text1 = font.render("Musica 1 - Artista 1", 1, (255, 255, 0))
            text_position1 = text1.get_rect(centerx=300, centery=100)
            text2 = font.render("Musica 2 - Artista 2", 1, (255, 255, 0))
            text_position2 = text1.get_rect(centerx=300, centery=300)

        background[0].blit(text1, text_position1)
        background[0].blit(text2, text_position2)

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            for event in pygame.event.get():

                if event.type == QUIT: sys.exit(0)
                

            screen.blit(background[0], (0,0))
            pygame.display.flip()
        
if __name__ == "__main__":
    
    Ui()