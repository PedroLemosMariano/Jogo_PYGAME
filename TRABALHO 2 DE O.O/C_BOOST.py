import math
from SRC_CARGAS import Raio_R, Coracao_vermelho
from VAR_GLOBAL import tela

class Boost_Base:
    def __init__(self, x, y, size, cor, imagens):
        self.x = x
        self.y = y
        self.size = size
        self.cor = cor
        self.imagens = imagens
        self.image = imagens['frente']

    
    def draw(self):
        tela.blit(self.image, (self.x - 70, self.y - 70))
    
    def colisao(self, jogador):
        distancia = math.hypot(self.x - jogador.x, self.y - jogador.y)
        return distancia < (self.size + jogador.size)
#------------------------RAIO
class Raio(Boost_Base):
    def __init__(self, x, y, size, cor):
        imagens = {
            'frente': Raio_R
        }
        super().__init__(x, y, size, cor, imagens)

#-------------------------CORAÇÃO
class Coracao(Boost_Base):
    def __init__(self, x, y, size, cor):
        imagens = {
            'frente': Coracao_vermelho
        }
        super().__init__(x, y, size, cor, imagens)
