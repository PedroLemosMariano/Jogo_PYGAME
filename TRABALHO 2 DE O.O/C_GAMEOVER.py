from VAR_GLOBAL import tela, tela_x, tela_y
from SRC_CARGAS import Placa_game_over
import pygame

class Gameover:
    def __init__(self, x, y, size, pontos):
        self.__x = x
        self.__y = y
        self.__size = size
        self.__scores = []
        self.__players = []
        self.__font = pygame.font.Font('FONTES/Evil_Highway.ttf', 35)

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
    def _scores(self):
        return self.__scores

    @_scores.setter
    def _scores(self, value):
        self.__scores = value

    @property
    def _players(self):
        return self.__players

    @_players.setter
    def _players(self, value):
        self.__players = value

    @property
    def _font(self):
        return self.__font

    @_font.setter
    def _font(self, value):
        self.__font = value


    def draw(self, tela):
        tela.blit(Placa_game_over, (self._x + tela_x/2 - 1000/2, self._y + tela_y/2 - 900/2 ))
        #tela.blit(self.text_surface, self.text_rect)

        hiscore_surface = self._font.render(str(self._scores[0]), True, (255, 200, 0))
        segundo_surface = self._font.render(str(self._scores[1]), True, (200, 200, 200))
        terceiro_surface = self._font.render(str(self._scores[2]), True, (150, 100, 30))

        player1_surface = self._font.render(str(self._players[0]), True, (255, 200, 0))
        player2_surface = self._font.render(str(self._players[1]), True, (200, 200, 200))
        player3_surface = self._font.render(str(self._players[2]), True, (150, 100, 30))

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
                self._players.append(player)
                self._scores.append(score)
            

    def write(self):
        with open('ranking.txt', 'w') as file:
            pass
            
        with open('ranking.txt', 'a') as file:
            file.write(str(self._players[0] + " " + str(self._scores[0]) + "\n"))
            file.write(str(self._players[1] + " " + str(self._scores[1]) + "\n"))
            file.write(str(self._players[2] + " " + str(self._scores[2])))

    def update(self, current_score, player_name):
        if current_score > self._scores[0]:
            self._scores[2] = self._scores[1]
            self._scores[1] = self._scores[0]
            self._scores[0] = current_score
            
            self._players[2] = self._players[1]
            self._players[1] = self._players[0]
            self._players[0] = player_name
            return

        if current_score > self._scores[1]:
            self._scores[2] = self._scores[1]
            self._scores[1] = current_score

            self._players[2] = self._players[1]
            self._players[1] = player_name
            return
            
        if current_score > self._scores[2]:
            self._scores[2] = current_score
            self._players[2] = player_name
            return 