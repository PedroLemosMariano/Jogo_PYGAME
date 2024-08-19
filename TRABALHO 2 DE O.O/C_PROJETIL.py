from VAR_GLOBAL import tela
import math
from SRC_CARGAS import Bola_arma

bala_spd = 5

class Projetil:
    def __init__(self, x, y, dir_x, dir_y):
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.radius = 16

    def update(self):
        global bala_spd
        self.x += self.dir_x * bala_spd
        self.y += self.dir_y * bala_spd

    def draw(self):
        tela.blit(Bola_arma, (self.x - 22, self.y - 22))

    def colisao(self, inimigos):
        for inimigo in inimigos:
            distancia = math.hypot(self.x - inimigo.x, self.y - inimigo.y)
            if distancia < (self.radius + inimigo.size):
                return inimigo
        return None

    def calcular_direcao(origem, destino):
        dir_x = destino[0] - origem[0]
        dir_y = destino[1] - origem[1]
        distancia = math.hypot(dir_x, dir_y)
        if distancia != 0:
            dir_x /= distancia
            dir_y /= distancia
        return dir_x, dir_y