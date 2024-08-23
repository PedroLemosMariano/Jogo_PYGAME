import pygame
from SRC_CARGAS import Manoel_costa, Manoel_frente, Manoel_ladoD, Manoel_ladoE
from VAR_GLOBAL import tela, tela_x, tela_y

class PERS_JOGAVEL:
    def __init__(self, x, y, size, spd, cor):
        self.__x = x
        self.__y = y
        self.__size = size
        self.__spd = spd
        self.__cor = cor
        self.__lastkey = 1
        self.__vida = 100

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
    def _lastkey(self):
        return self.__lastkey

    @_lastkey.setter
    def _lastkey(self, value):
        self.__lastkey = value

    @property
    def _vida(self):
        return self.__vida

    @_vida.setter
    def _vida(self, value):
        self.__vida = value


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self._lastkey = 0
            self._y -= self._spd

        if keys[pygame.K_s]:
            self._lastkey = 1
            self._y += self._spd

        if keys[pygame.K_a]:
            self._lastkey = 2
            self._x -= self._spd

        if keys[pygame.K_d]:
            self._lastkey = 3
            self._x += self._spd

        
    
    def draw(self):
        if self._lastkey == 0:
            tela.blit(Manoel_costa, (self._x - 70, self._y - 70))
        elif self._lastkey == 1:
            tela.blit(Manoel_frente, (self._x - 70, self._y - 70))
        elif self._lastkey == 2:
            tela.blit(Manoel_ladoE, (self._x - 70, self._y - 70))
        elif self._lastkey == 3:
            tela.blit(Manoel_ladoD, (self._x - 70, self._y - 70))

    def barravida(self):
        largura_total = 97
        largura_atual = self._vida/1.3
        pygame.draw.rect(tela, (0, 0, 0), (self._x - largura_total/2, self._y-90, largura_total, 13))
        pygame.draw.rect(tela, (255, 0, 0), ((self._x - largura_total/2+11), self._y- 86, largura_atual, 5))

    def bordas(self):
        if self._y < self._size + 4:
            self._y = self._size + 4
        if self._x < self._size + 60:
            self._x = self._size + 60
        if self._y > tela_y - self._size - 120:
            self._y = tela_y - self._size - 120
        if self._x > tela_x - self._size - 60:
            self._x = tela_x - self._size - 60