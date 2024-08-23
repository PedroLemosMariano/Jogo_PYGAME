import math
from SRC_CARGAS import Raio_R, Coracao_vermelho
from VAR_GLOBAL import tela

class Boost_Base:
    def __init__(self, x, y, size, cor, imagens):
        self.__x = x
        self.__y = y
        self.__size = size
        self.__cor = cor
        self.__imagens = imagens
        self.__image = imagens['frente']

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


    
    def draw(self):
        tela.blit(self._image, (self._x - 70, self._y - 70))
    
    def colisao(self, jogador):
        distancia = math.hypot(self._x - jogador._x, self._y - jogador._y)
        return distancia < (self._size + jogador._size)
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
