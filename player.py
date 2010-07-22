
import time
import subprocess

class Player(object):

    def play(self, full_path):
        proc = subprocess.Popen(['mplayer', full_path])
        
        time.sleep(3)
        print 'matando a musica agora!'
        proc.kill()
        

if __name__ == "__main__":
    
    player = Player()
    player.play("/home/flavio/devel/tw/musics/comanche.mp3")
        