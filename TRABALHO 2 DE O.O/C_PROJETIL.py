from VAR_GLOBAL import tela
import math
from SRC_CARGAS import Bola_arma

bala_spd = 5

class Projetil:
    def __init__(self, x, y, dir_x, dir_y, spd):
        self.__x = x
        self.__y = y
        self.__dir_x = dir_x
        self.__dir_y = dir_y
        self.__radius = 16
        self.spd = spd

    @property
    def _x(self):
        return self.__x

    @_x.setter
    def _x(self, value):
        self.__x = value

    @property
    def _y(self):
        return self.__y

    @_y.setter
    def _y(self, value):
        self.__y = value

    @property
    def _dir_x(self):
        return self.__dir_x

    @_dir_x.setter
    def _dir_x(self, value):
        self.__dir_x = value

    @property
    def _dir_y(self):
        return self.__dir_y

    @_dir_y.setter
    def _dir_y(self, value):
        self.__dir_y = value

    @property
    def _radius(self):
        return self.__radius

    @_radius.setter
    def _radius(self, value):
        self.__radius = value


    def update(self):
        global bala_spd
        self._x += self._dir_x * self.spd
        self._y += self._dir_y * self.spd

    def draw(self):
        tela.blit(Bola_arma, (self._x - 22, self._y - 22))

    def colisao(self, inimigos):
        for inimigo in inimigos:
            distancia = math.hypot(self._x - inimigo._x, self._y - inimigo._y)
            if distancia < (self._radius + inimigo._size):
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