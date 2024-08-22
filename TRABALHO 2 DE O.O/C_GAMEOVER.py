from VAR_GLOBAL import tela, tela_x, tela_y
from SRC_CARGAS import Placa_game_over
import pygame

class Gameover:
    def __init__(self, x, y, size, pontos):
        self.x = x
        self.y = y
        self.size = size
        self.scores = []
        self.players = []
        self.font = pygame.font.Font('FONTES/Evil_Highway.ttf', 35)

    def draw(self, tela):
        tela.blit(Placa_game_over, (self.x + tela_x/2 - 1000/2, self.y + tela_y/2 - 900/2 ))
        #tela.blit(self.text_surface, self.text_rect)

        hiscore_surface = self.font.render(str(self.scores[0]), True, (255, 200, 0))
        segundo_surface = self.font.render(str(self.scores[1]), True, (200, 200, 200))
        terceiro_surface = self.font.render(str(self.scores[2]), True, (150, 100, 30))

        player1_surface = self.font.render(str(self.players[0]), True, (255, 200, 0))
        player2_surface = self.font.render(str(self.players[1]), True, (200, 200, 200))
        player3_surface = self.font.render(str(self.players[2]), True, (150, 100, 30))

        tela.blit(hiscore_surface, (750, 230))
        tela.blit(segundo_surface, (750, 350))
        tela.blit(terceiro_surface, (750, 470))

        tela.blit(player1_surface, (850, 230))
        tela.blit(player2_surface, (850, 350))
        tela.blit(player3_surface, (850, 470))

    def read(self):
        with open('ranking.txt', 'r') as file:
            for line in file:
                player, score = line.strip().split()
                
                score = int(score)
                self.players.append(player)
                self.scores.append(score)
            

    def write(self):
        with open('ranking.txt', 'w') as file:
            pass
            
        with open('ranking.txt', 'a') as file:
            file.write(str(self.players[0] + " " + str(self.scores[0]) + "\n"))
            file.write(str(self.players[1] + " " + str(self.scores[1]) + "\n"))
            file.write(str(self.players[2] + " " + str(self.scores[2])))

    def update(self, current_score, player_name):
        if current_score > self.scores[0]:
            self.scores[2] = self.scores[1]
            self.scores[1] = self.scores[0]
            self.scores[0] = current_score
            
            self.players[2] = self.players[1]
            self.players[1] = self.players[0]
            self.players[0] = player_name
            return

        if current_score > self.scores[1]:
            self.scores[2] = self.scores[1]
            self.scores[1] = current_score

            self.players[2] = self.players[1]
            self.players[1] = player_name
            return
            
        if current_score > self.scores[2]:
            self.scores[2] = current_score
            self.players[2] = player_name
            return 