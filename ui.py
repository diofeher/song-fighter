from pygame.locals import *
import pygame
import os
import time
import sys
import player
import interface

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

    def __init__(self, full_path):
        
        interface.create_musics(full_path) # cria as musicas
        self.isRunning= True
        self.run(full_path)
        
               
    def run(self, full_path):
        pygame.init()

        screen = pygame.display.set_mode((600,451))

        pygame.display.set_caption("Toughtworks - Songs Fighter!")
        pygame.mouse.set_visible(1)

        background = load_image("background.png")

        screen.blit(background[0], (0,0))
        pygame.display.flip()

        musicas = interface.get_musics()
        
        if pygame.font:
            font = pygame.font.Font(None, 48)
            text1 = font.render(musicas[0].path, 1, (255, 255, 0))
            text_position1 = text1.get_rect(centerx=300, centery=100)
            text2 = font.render(musicas[1].path, 1, (255, 255, 0))
            text_position2 = text1.get_rect(centerx=300, centery=300)

        font2 = pygame.font.Font(None, 14)
        status = font.render("Espere tocar as musicas... :-)", 1, (255, 255, 255))
        status_pos = status.get_rect(centerx=300, centery=350)
        
        background[0].blit(text1, text_position1)
        background[0].blit(text2, text_position2)
        background[0].blit(status, status_pos)
        
        screen.blit(background[0], (0,0))
        pygame.display.flip()
        
 

        clock = pygame.time.Clock()
        
        _player = player.Player()
            
        
        _player.play(full_path + musicas[0].path)
        time.sleep(4)
        _player.play(full_path + musicas[1].path)
        
        background[0].blit(status, status_pos) 
        

        while self.isRunning:
            clock.tick(60)
            
            font2 = pygame.font.Font(None, 14)
            status = font.render("Musicas tocaram do_Ob", 1, (255, 255, 255))
            status_pos = status.get_rect(centerx=300, centery=400)
            screen.blit(background[0], (0,0))
            background[0].blit(text1, text_position1)
            background[0].blit(text2, text_position2)
            background[0].blit(status, status_pos)
            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == QUIT: 
                    sys.exit(0)
                
                if event.type == KEYDOWN:
                    
                    if event.key == K_UP:
                        musicas[0].update_count()
                        print 'up'
                        self.isRunning = False
                        break
                        
                    elif event.key == K_DOWN:
                        musicas[1].update_count()
                        self.isRunning = False
                        print 'down'
                        break
 
        self.isRunning = True            
        self.run(full_path)
                

        screen.blit(background[0], (0,0))
        pygame.display.flip()
        
if __name__ == "__main__":
    
    Ui("/home/flavio/devel/tw/musics/")