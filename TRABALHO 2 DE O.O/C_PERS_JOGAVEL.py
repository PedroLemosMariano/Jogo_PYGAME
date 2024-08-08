import pygame
from VAR_GLOBAL import *
from CA_CARGAS import *

class PERS_JOGAVEL:
    def __init__(self, x, y, size, spd, cor):
        self.x = x
        self.y = y
        self.size = size
        self.spd = spd
        self.cor = cor
        self.lastkey = 1
        self.vida = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.lastkey = 0
            self.y -= self.spd

        if keys[pygame.K_s]:
            self.lastkey = 1
            self.y += self.spd

        if keys[pygame.K_a]:
            self.lastkey = 2
            self.x -= self.spd

        if keys[pygame.K_d]:
            self.lastkey = 3
            self.x += self.spd
    
    def draw(self):
        if self.lastkey == 0:
            tela.blit(Manoel_costa, (self.x - 70, self.y - 70))
        elif self.lastkey == 1:
            tela.blit(Manoel_frente, (self.x - 70, self.y - 70))
        elif self.lastkey == 2:
            tela.blit(Manoel_ladoE, (self.x - 70, self.y - 70))
        elif self.lastkey == 3:
            tela.blit(Manoel_ladoD, (self.x - 70, self.y - 70))

    def barravida(self):
        largura_total = 97
        largura_atual = self.vida/1.3
        pygame.draw.rect(tela, (0, 0, 0), (self.x - largura_total/2, self.y-90, largura_total, 13))
        pygame.draw.rect(tela, (255, 0, 0), ((self.x - largura_total/2+11), self.y- 86, largura_atual, 5))

    def bordas(self):
        if self.y < self.size + 2:
            self.y = self.size + 2
        if self.x < self.size + 2:
            self.x = self.size + 2
        if self.y > tela_y - self.size - 2:
            self.y = tela_y - self.size - 2
        if self.x > tela_x - self.size - 2:
            self.x = tela_x - self.size - 2

personagem1 = PERS_JOGAVEL(tela_x / 2, tela_y / 2, 25, 5, (0, 255, 0))