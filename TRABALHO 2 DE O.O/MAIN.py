import pygame
import random
import sys
from C_PERSONAGEM import PERS_JOGAVEL
from C_PROJETIL import Projetil
from C_INIMIGOS import InimigoCaveira, InimigoMorcego
from C_BOOST import Coracao, Raio
from C_SCORE import Score
from C_GAMEOVER import Gameover
from SRC_CARGAS import *
from VAR_GLOBAL import *

pygame.init()

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((1600, 800))
        self.clock = pygame.time.Clock()
        self.gramado = gramado
        self.Som_Tema = Som_Tema
        self.Som_Pegar_Vida = Som_Pegar_Vida
        self.canal1 = pygame.mixer.Channel(0)
        self.canal2 = pygame.mixer.Channel(1)
        self.personagem1 = PERS_JOGAVEL(tela_x / 2, tela_y / 2, 25, 5, (0, 255, 0))
        self.pontuação = Score(110,54,55,(200,200,200),0)
        self.projeteis = []
        self.inimigos_m = []
        self.inimigos_c = []
        self.boost_list_c = []
        self.boost_list_r = []
        self.bala_spd = 10
        self.pausado = False
        self.gameover = False
        self.last_tick = pygame.time.get_ticks()
        self.spawn_time = 3000
        self.hiscore = 0
        self.segundo = 0
        self.terceiro = 0
        self.last_tick = pygame.time.get_ticks()
        self.last_threshold = 0
        self.decrement = 0
        self.fonte_nome = pygame.font.Font(None, 74)
        self.nome_jogador = ""
        
        self.personagem1 = PERS_JOGAVEL(tela_x / 2, tela_y / 2, 25, 5, (0, 255, 0))
        self.pontuação = Score(110,54,55,(200,200,200),0)
        self.telafinal = Gameover(0,0,20,20)


    def calcular_direcao(self, origem, destino):
        dir_x, dir_y = destino[0] - origem[0], destino[1] - origem[1]
        magnitude = (dir_x**2 + dir_y**2) ** 0.5
        return dir_x / magnitude, dir_y / magnitude

    def gerador_inimigo(self):
        x = random.randint(0, tela_x)
        y = random.randint(0, tela_y)
        size = 20
        spd_m = random.randint(4, 5)
        spd_c = random.randint(2, 4)
        cor = (255, 0, 0)

        if random.randint(0, 4) == 0:
            inimigo = InimigoMorcego(x, y, size, spd_m, cor)
            Som_Morcego.play() 
            self.inimigos_m.append(inimigo)
        else:
            inimigo = InimigoCaveira(x, y, size, spd_c, cor)
            Som_Caveira.play()
            self.inimigos_c.append(inimigo)
        

    def gerador_boost(self):
        x = random.randint(80, tela_x - 80)
        y = random.randint(80, tela_y - 200)
        size = 20
        cor = (255, 0, 0)

        if random.randint(0, 2) == 0:
            boost = Raio(x, y, size, cor)
            Som_Raio.play()
            self.boost_list_r.append(boost)
        else:
            boost = Coracao(x, y, size, cor)
            Som_Vida.play()
            self.boost_list_c.append(boost)
            
    def mousepos(self):
        mousex,mousey = pygame.mouse.get_pos()
        tela.blit(Varinha_mouse, (mousex,mousey))

    def update_level(self):
        self.decrement = (self.spawn_time / 4)
        self.current_threshold = (self.pontuação.pontos // 5) * 5
        if self.current_threshold > self.last_threshold:
            self.spawn_time -= self.decrement
            self.last_threshold = self.current_threshold


    def rodar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos
                        dir_x, dir_y = self.calcular_direcao((self.personagem1.x, self.personagem1.y), (mouse_x, mouse_y))
                        self.projeteis.append(Projetil(self.personagem1.x, self.personagem1.y, dir_x, dir_y))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pausado = not self.pausado

            self.tela.blit(self.gramado, (0, 0))
            if not self.canal1.get_busy():
                self.canal1.play(self.Som_Tema, loops=-1)

            if not self.gameover:
                if not self.pausado:
                    self.personagem1.update()
                    
                self.personagem1.draw()
                self.personagem1.bordas()
                self.personagem1.barravida()

                tick_atual = pygame.time.get_ticks()

                if tick_atual - self.last_tick >= self.spawn_time:
                    if not self.pausado:
                        self.gerador_inimigo()
                        if random.randint(1, 5) == 3:
                            self.gerador_boost()
                    self.last_tick = tick_atual

                for poder in self.projeteis[:]:
                    if not self.pausado:
                        poder.update()
                    caveira_colidido = poder.colisao(self.inimigos_c)
                    if caveira_colidido:
                        self.inimigos_c.remove(caveira_colidido)
                        self.projeteis.remove(poder)
                        self.pontuação.pontos += 1

                    morcego_colidido = poder.colisao(self.inimigos_m)    
                    if morcego_colidido and inimigoM.esquiva > 0:
                        inimigoM.y += 50
                        inimigoM.esquiva -= 1
                           
                    elif morcego_colidido:
                        self.inimigos_m.remove(morcego_colidido)
                        self.projeteis.remove(poder)
                        self.pontuação.pontos += 1

                    poder.draw()

                for vida in self.boost_list_c:
                    vida.draw()
                    if vida.colisao(self.personagem1):
                        self.personagem1.vida += 25
                        self.Som_Pegar_Vida.play()
                        self.boost_list_c.remove(vida)
                    if self.personagem1.vida > 100:
                        self.personagem1.vida = 100

                for raio in self.boost_list_r:
                    raio.draw()
                    if raio.colisao(self.personagem1):
                        self.bala_spd += 2
                        self.canal2.play(self.Som_Pegar_Vida)
                        self.boost_list_r.remove(raio)
                    if self.bala_spd > 30:
                        self.bala_spd = 30

                for projetil in self.projeteis:
                    if not self.pausado:
                        projetil.update()
                    projetil.draw()

                for inimigoC in self.inimigos_c:
                    if not self.pausado:
                        inimigoC.update(self.personagem1.x, self.personagem1.y)
                        if inimigoC.colisao(self.personagem1):
                            self.personagem1.vida -= 1
                        
                    inimigoC.draw()
                    if self.personagem1.vida <= 0:
                        self.gameover = True

                for inimigoM in self.inimigos_m:
                    if not self.pausado:
                        inimigoM.update(self.personagem1.x, self.personagem1.y)
                        if inimigoM.colisao(self.personagem1):
                            self.personagem1.vida -= 1
                        
                    inimigoM.draw()
                    if self.personagem1.vida <= 0:
                        self.gameover = True

                if not self.pausado:
                    self.pontuação.update()
                self.pontuação.draw()

            else:
                self.telafinal.draw()
                self.canal1.stop()
                self.tela.blit(self.pontuação.text_surface, (400, 300 + 55))

                hiscore_surface = self.pontuação.fonte.render(str(self.hiscore), True, (200, 255, 0))
                segundo_surface = self.pontuação.fonte.render(str(self.hiscore), True, (200, 255, 0))
                terceiro_surface = self.pontuação.fonte.render(str(self.hiscore), True, (200, 255, 0))
                if self.pontuação.pontos >= self.hiscore:
                    self.hiscore = self.pontuação.pontos
                    with open('score.txt', 'r+') as file:
                        file.seek(0)
                        file.write(str(self.hiscore))
                        file.truncate()

                elif self.pontuação.pontos > self.segundo:
                    self.hiscore = self.pontuação.pontos
                    with open('score.txt', 'r+') as file:
                        file.seek(0)
                        file.write(str(self.hiscore))
                        file.truncate()

                elif self.pontuação.pontos >= self.terceiro:
                    self.hiscore = self.pontuação.pontos
                    with open('score.txt', 'r+') as file:
                        file.seek(0)
                        file.write(str(self.hiscore))
                        file.truncate()

                self.tela.blit(hiscore_surface, (600, 300 - 85))

            self.mousepos()
            self.update_level()
            pygame.display.flip()
            self.clock.tick(60)


def raise_memory_error():
    raise MemoryError

if __name__ == "__main__":
    try:
        jogo = Jogo()
        #jogo.rodar = raise_memory_error
        jogo.rodar()
    except MemoryError:
        print("Erro de Memória: Não há memória suficiente no dispositivo para executar este jogo.")
        pygame.quit()
        sys.exit()
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Certifique-se de que o arquivo exista.")
        pygame.quit()
        sys.exit()
    finally:
        pygame.quit()
