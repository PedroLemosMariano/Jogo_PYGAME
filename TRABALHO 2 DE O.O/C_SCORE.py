import pygame
from VAR_GLOBAL import tela
from SRC_CARGAS import Placa_score

class Score:
    def __init__(self, x, y,size , cor, pontos):
        self.x = x
        self.y = y
        self.size = size
        self.cor = cor
        self.pontos = int(pontos)

        self.fonte = pygame.font.Font('FONTES/Evil_Highway.ttf', 35)

        self.update_texto()

    def update_texto(self):
        self.text_surface = self.fonte.render(str(self.pontos), True, self.cor)
        self.text_rect = self.text_surface.get_rect(center=(self.x,self.y))

    def draw(self):
        tela.blit(Placa_score, (10, 10))
        tela.blit(self.text_surface, self.text_rect)

    def update(self):
        self.update_texto()