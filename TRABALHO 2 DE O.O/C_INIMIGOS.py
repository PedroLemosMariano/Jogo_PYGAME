import math
from SRC_CARGAS import Caveira_costa, Caveira_frente, Caveira_ladoD, Caveira_ladoE, Morcego_costa, Morcego_frente, Morcego_ladoD, Morcego_ladoE
from VAR_GLOBAL import tela

class InimigoBase:
    def __init__(self, x, y, size, spd, cor, imagens):
        self.__x = x
        self.__y = y
        self.__size = size
        self.__spd = spd
        self.__cor = cor
        self.__imagens = imagens
        self.__image = imagens['frente']
        self.__esquiva = 2

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
    def _size(self):
        return self.__size

    @_size.setter
    def _size(self, value):
        self.__size = value

    @property
    def _spd(self):
        return self.__spd

    @_spd.setter
    def _spd(self, value):
        self.__spd = value

    @property
    def _cor(self):
        return self.__cor

    @_cor.setter
    def _cor(self, value):
        self.__cor = value

    @property
    def _imagens(self):
        return self.__imagens

    @_imagens.setter
    def _imagens(self, value):
        self.__imagens = value

    @property
    def _image(self):
        return self.__image

    @_image.setter
    def _image(self, value):
        self.__image = value

    @property
    def _esquiva(self):
        return self.__esquiva

    @_esquiva.setter
    def _esquiva(self, value):
        self.__esquiva = value



    def update(self, player_x, player_y):
        dir_x = player_x - self._x
        dir_y = player_y - self._y
        distancia = math.hypot(dir_x, dir_y)
        if distancia != 0:
            dir_x /= distancia
            dir_y /= distancia

        self._x += dir_x * self._spd
        self._y += dir_y * self._spd

        if abs(dir_x) > abs(dir_y):
            self.image = self.__imagens['ladoD'] if dir_x > 0 else self.__imagens['ladoE']
        else:
            self.image = self.__imagens['frente'] if dir_y > 0 else self.__imagens['costa']

    def draw(self):
        tela.blit(self.image, (self._x - 70, self._y - 70))

    def colisao(self, jogador):
        distancia = math.hypot(self._x - jogador._x, self._y - jogador._y)
        return distancia < (self._size + jogador._size)

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