import pygame

class Projetil:
    def __init__(self, x, y, jogador):
        self.x = x
        self.y = y

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.x = mouse_x
        self.y = mouse_y

    def draw(self, tela):
        pygame.draw.circle(tela,(255,255,255),(self.x,self.y), 20)
        #pygame.draw.circle(tela, self.cor, (self.x, self.y), self.size)