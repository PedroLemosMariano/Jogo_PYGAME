import pygame
from VAR_GLOBAL import *
import math
from CA_CARGAS import *

class Projetil:
    def __init__(self, x, y, dir_x, dir_y):
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.speed = 3
        self.radius = 16

    def update(self):
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed

    def draw(self):
        tela.blit(Bola_arma, (self.x - 22, self.y - 22))

    def colisao(self, inimigos):
        for inimigo in inimigos:
            distancia = math.hypot(self.x - inimigo.x, self.y - inimigo.y)
            if distancia < (self.radius + inimigo.size):
                return inimigo
        return None