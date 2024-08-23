import pygame
from VAR_GLOBAL import tela
from SRC_CARGAS import Placa_score

class Score:
    def __init__(self, x, y,size , cor, pontos):
        self.__x = x
        self.__y = y
        self.__size = size
        self.__cor = cor
        self.__pontos = int(pontos)
        self.__fonte = pygame.font.Font('FONTES/Evil_Highway.ttf', 35)


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
    def _pontos(self):
        return self.__pontos

    @_pontos.setter
    def _pontos(self, value):
        self.__pontos = value

    @property
    def _fonte(self):
        return self.__fonte

    @_fonte.setter
    def _fonte(self, value):
        self.__fonte = value

        self.update_texto()

    def update_texto(self):
        self.text_surface = self._fonte.render(str(self._pontos), True, self._cor)
        self.text_rect = self.text_surface.get_rect(center=(self._x,self._y))

    def draw(self):
        tela.blit(Placa_score, (10, 10))
        tela.blit(self.text_surface, self.text_rect)

    def update(self):
        self.update_texto()