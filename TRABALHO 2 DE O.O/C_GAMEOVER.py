from VAR_GLOBAL import tela, tela_x, tela_y
from SRC_CARGAS import Placa_game_over

class Gameover:
    def __init__(self, x, y,size , pontos):
        self.x = x
        self.y = y
        self.size = size
        self.pontos = pontos

    def draw(self):
        tela.blit(Placa_game_over, (self.x + tela_x/2 - 1000/2, self.y + tela_y/2 - 900/2 ))
        #tela.blit(self.text_surface, self.text_rect)