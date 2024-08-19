import math
from SRC_CARGAS import Caveira_costa, Caveira_frente, Caveira_ladoD, Caveira_ladoE, Morcego_costa, Morcego_frente, Morcego_ladoD, Morcego_ladoE
from VAR_GLOBAL import tela

class InimigoBase:
    def __init__(self, x, y, size, spd, cor, imagens):
        self.x = x
        self.y = y
        self.size = size
        self.spd = spd
        self.cor = cor
        self.imagens = imagens
        self.image = imagens['frente']
        self.esquiva = 2

    def update(self, player_x, player_y):
        dir_x = player_x - self.x
        dir_y = player_y - self.y
        distancia = math.hypot(dir_x, dir_y)
        if distancia != 0:
            dir_x /= distancia
            dir_y /= distancia

        self.x += dir_x * self.spd
        self.y += dir_y * self.spd

        if abs(dir_x) > abs(dir_y):
            self.image = self.imagens['ladoD'] if dir_x > 0 else self.imagens['ladoE']
        else:
            self.image = self.imagens['frente'] if dir_y > 0 else self.imagens['costa']

    def draw(self):
        tela.blit(self.image, (self.x - 70, self.y - 70))

    def colisao(self, jogador):
        distancia = math.hypot(self.x - jogador.x, self.y - jogador.y)
        return distancia < (self.size + jogador.size)

#-------------------------CAVEIRA------------------------
class InimigoCaveira(InimigoBase):
    def __init__(self, x, y, size, spd, cor):
        imagens = {
            'frente': Caveira_frente,
            'costa': Caveira_costa,
            'ladoD': Caveira_ladoD,
            'ladoE': Caveira_ladoE,
        }
        super().__init__(x, y, size, spd, cor, imagens)

#------------------------MORCEGO-------------------------
class InimigoMorcego(InimigoBase):
    def __init__(self, x, y, size, spd, cor):
        imagens = {
            'frente': Morcego_frente,
            'costa': Morcego_costa,
            'ladoD': Morcego_ladoD,
            'ladoE': Morcego_ladoE,
        }
        super().__init__(x, y, size, spd, cor, imagens)