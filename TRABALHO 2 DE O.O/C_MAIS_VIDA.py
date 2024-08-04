import math
from CA_CARGAS import *
from VAR_GLOBAL import *

class MAIS_VIDA:
    def __init__(self, x, y,size , cor):
        self.x = x
        self.y = y
        self.size = size
        self.cor = cor
        self.image = Coracao_vermelho
    
    def draw(self):
        tela.blit(self.image, (self.x - 70, self.y - 70))
    
    def colisao(self, jogador):
        distancia = math.hypot(self.x - jogador.x, self.y - jogador.y)
        return distancia < (self.size + jogador.size)