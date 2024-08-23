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

class Jogo:
    def __init__(self):
        pygame.init()
        self.__tela = pygame.display.set_mode((1600, 800))
        self.__clock = pygame.time.Clock()
        self.__gramado = gramado
        self.__Som_Tema = Som_Tema
        self.__Som_Pegar_Vida = Som_Pegar_Vida
        self.__canal1 = pygame.mixer.Channel(0)
        self.__canal2 = pygame.mixer.Channel(1)
        self.__personagem1 = PERS_JOGAVEL(tela_x / 2, tela_y / 2, 25, 5, (0, 255, 0))
        self.__pontuação = Score(110,54,55,(200,200,200),0)
        self.__projeteis = []
        self.__inimigos_m = []
        self.__inimigos_c = []
        self.__boost_list_c = []
        self.__boost_list_r = []
        self.__bala_spd = 5
        self.__pausado = False
        self.__gameover = False
        self.__last_tick = pygame.time.get_ticks()
        self.__spawn_time = 3000
        self.__last_tick = pygame.time.get_ticks()
        self.__last_threshold = 0
        self.__decrement = 0
        self.__fonte_nome = pygame.font.Font(None, 74) 
        self.__player_name = "PEDRO"
        self.__personagem1 = PERS_JOGAVEL(tela_x / 2, tela_y / 2, 25, 5, (0, 255, 0))
        self.__pontuação = Score(110,54,55,(200,200,200),0)
        self.__telafinal = Gameover(0,0,20,20)
        self.__telafinal.read()
        self.__hiscore = self._telafinal._scores[0]
        self.__segundo = self._telafinal._scores[1]
        self.__terceiro = self._telafinal._scores[2]

    @property
    def _tela(self):
        return self.__tela

    @_tela.setter
    def _tela(self, value):
        self.__tela = value

    @property
    def _clock(self):
        return self.__clock

    @_clock.setter
    def _clock(self, value):
        self.__clock = value

    @property
    def _gramado(self):
        return self.__gramado

    @_gramado.setter
    def _gramado(self, value):
        self.__gramado = value

    @property
    def _Som_Tema(self):
        return self.__Som_Tema

    @_Som_Tema.setter
    def _Som_Tema(self, value):
        self.__Som_Tema = value

    @property
    def _Som_Pegar_Vida(self):
        return self.__Som_Pegar_Vida

    @_Som_Pegar_Vida.setter
    def _Som_Pegar_Vida(self, value):
        self.__Som_Pegar_Vida = value

    @property
    def _canal1(self):
        return self.__canal1

    @_canal1.setter
    def _canal1(self, value):
        self.__canal1 = value

    @property
    def _canal2(self):
        return self.__canal2

    @_canal2.setter
    def _canal2(self, value):
        self.__canal2 = value

    @property
    def _personagem1(self):
        return self.__personagem1

    @_personagem1.setter
    def _personagem1(self, value):
        self.__personagem1 = value

    @property
    def _pontuação(self):
        return self.__pontuação

    @_pontuação.setter
    def _pontuação(self, value):
        self.__pontuação = value

    @property
    def _projeteis(self):
        return self.__projeteis

    @_projeteis.setter
    def _projeteis(self, value):
        self.__projeteis = value

    @property
    def _inimigos_m(self):
        return self.__inimigos_m

    @_inimigos_m.setter
    def _inimigos_m(self, value):
        self.__inimigos_m = value

    @property
    def _inimigos_c(self):
        return self.__inimigos_c

    @_inimigos_c.setter
    def _inimigos_c(self, value):
        self.__inimigos_c = value

    @property
    def _boost_list_c(self):
        return self.__boost_list_c

    @_boost_list_c.setter
    def _boost_list_c(self, value):
        self.__boost_list_c = value

    @property
    def _boost_list_r(self):
        return self.__boost_list_r

    @_boost_list_r.setter
    def _boost_list_r(self, value):
        self.__boost_list_r = value

    @property
    def _bala_spd(self):
        return self.__bala_spd

    @_bala_spd.setter
    def _bala_spd(self, value):
        self.__bala_spd = value

    @property
    def _pausado(self):
        return self.__pausado

    @_pausado.setter
    def _pausado(self, value):
        self.__pausado = value

    @property
    def _gameover(self):
        return self.__gameover

    @_gameover.setter
    def _gameover(self, value):
        self.__gameover = value

    @property
    def _last_tick(self):
        return self.__last_tick

    @_last_tick.setter
    def _last_tick(self, value):
        self.__last_tick = value

    @property
    def _spawn_time(self):
        return self.__spawn_time

    @_spawn_time.setter
    def _spawn_time(self, value):
        self.__spawn_time = value

    @property
    def _last_tick(self):
        return self.__last_tick

    @_last_tick.setter
    def _last_tick(self, value):
        self.__last_tick = value

    @property
    def _last_threshold(self):
        return self.__last_threshold

    @_last_threshold.setter
    def _last_threshold(self, value):
        self.__last_threshold = value

    @property
    def _decrement(self):
        return self.__decrement

    @_decrement.setter
    def _decrement(self, value):
        self.__decrement = value

    @property
    def _fonte_nome(self):
        return self.__fonte_nome

    @_fonte_nome.setter
    def _fonte_nome(self, value):
        self.__fonte_nome = value

    @property
    def _player_name(self):
        return self.__player_name

    @_player_name.setter
    def _player_name(self, value):
        self.__player_name = value

    @property
    def _personagem1(self):
        return self.__personagem1

    @_personagem1.setter
    def _personagem1(self, value):
        self.__personagem1 = value

    @property
    def _pontuação(self):
        return self.__pontuação

    @_pontuação.setter
    def _pontuação(self, value):
        self.__pontuação = value

    @property
    def _telafinal(self):
        return self.__telafinal

    @_telafinal.setter
    def _telafinal(self, value):
        self.__telafinal = value

    @property
    def _telafinal(self):
        return self.__telafinal

    @_telafinal.setter
    def _telafinal(self, value):
        self.__telafinal = value

    @property
    def _hiscore(self):
        return self.__hiscore

    @_hiscore.setter
    def _hiscore(self, value):
        self.__hiscore = value

    @property
    def _segundo(self):
        return self.__segundo

    @_segundo.setter
    def _segundo(self, value):
        self.__segundo = value

    @property
    def _terceiro(self):
        return self.__terceiro

    @_terceiro.setter
    def _terceiro(self, value):
        self.__terceiro = value


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
            self._inimigos_m.append(inimigo)
        else:
            inimigo = InimigoCaveira(x, y, size, spd_c, cor)
            Som_Caveira.play()
            self._inimigos_c.append(inimigo)
        
    def gerador_boost(self):
        x = random.randint(80, tela_x - 80)
        y = random.randint(80, tela_y - 200)
        size = 20
        cor = (255, 0, 0)

        if random.randint(0, 2) == 0:
            boost = Raio(x, y, size, cor)
            Som_Raio.play()
            self._boost_list_r.append(boost)
        else:
            boost = Coracao(x, y, size, cor)
            Som_Vida.play()
            self._boost_list_c.append(boost)
            
    def mousepos(self):
        mousex,mousey = pygame.mouse.get_pos()
        tela.blit(Varinha_mouse, (mousex,mousey))

    def update_level(self):
        self._decrement = (self._spawn_time / 4)
        self._current_threshold = (self._pontuação._pontos // 5) * 5
        if self._current_threshold > self._last_threshold:
            self._spawn_time -= self._decrement
            self._last_threshold = self._current_threshold

    def rodar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos
                        dir_x, dir_y = self.calcular_direcao((self._personagem1._x, self._personagem1._y), (mouse_x, mouse_y))
                        self._projeteis.append(Projetil(self._personagem1._x, self._personagem1._y, dir_x, dir_y, self._bala_spd))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self._pausado = not self._pausado

            self._tela.blit(self._gramado, (0, 0))
            if not self._canal1.get_busy():
                self._canal1.play(self._Som_Tema, loops=-1)

            if not self._gameover:
                if not self._pausado:
                    self._personagem1.update()
                    
                self._personagem1.draw()
                self._personagem1.bordas()
                self._personagem1.barravida()

                tick_atual = pygame.time.get_ticks()

                if tick_atual - self._last_tick >= self._spawn_time:
                    if not self._pausado:
                        self.gerador_inimigo()
                        if random.randint(1, 5) == 3:
                            self.gerador_boost()
                    self._last_tick = tick_atual

                for poder in self._projeteis[:]:
                    if not self._pausado:
                        poder.update()

                    projétil_removido = False
        
                    caveira_colidido = poder.colisao(self._inimigos_c)
                    if caveira_colidido:
                        self._inimigos_c.remove(caveira_colidido)
                        if poder in self._projeteis:
                            self._projeteis.remove(poder)
                            self._pontuação._pontos += 1
                        projétil_removido = True

                    morcego_colidido = poder.colisao(self._inimigos_m)
                    if morcego_colidido and not projétil_removido:
                        if morcego_colidido and inimigoM._esquiva > 0:
                            inimigoM._y += 50
                            inimigoM._esquiva -= 1
                        elif morcego_colidido:
                            self._inimigos_m.remove(morcego_colidido)
                            if poder in self._projeteis:
                                self._projeteis.remove(poder)
                                self._pontuação._pontos += 1
                            projétil_removido = True

                    poder.draw()

                for vida in self._boost_list_c:
                    vida.draw()
                    if vida.colisao(self._personagem1):
                        self._personagem1._vida += 25
                        self._Som_Pegar_Vida.play()
                        self._boost_list_c.remove(vida)
                    if self._personagem1._vida > 100:
                        self._personagem1._vida = 100

                for raio in self._boost_list_r:
                    raio.draw()
                    if raio.colisao(self._personagem1):
                        self._bala_spd += 2
                        self._personagem1._spd += 2
                        self._canal2.play(self._Som_Pegar_Vida)
                        self._boost_list_r.remove(raio)
                    if self._bala_spd > 30:
                        self._bala_spd = 30
                    elif self._personagem1._spd > 10:
                        self._personagem1._spd = 10

                for projetil in self._projeteis:
                    if not self._pausado:
                        projetil.update()
                    projetil.draw()

                for inimigoC in self._inimigos_c:
                    if not self._pausado:
                        inimigoC.update(self._personagem1._x, self._personagem1._y)
                        if inimigoC.colisao(self._personagem1):
                            self._personagem1._vida -= 1
                        
                    inimigoC.draw()
                    if self._personagem1._vida <= 0:
                        self._gameover = True

                for inimigoM in self._inimigos_m:
                    if not self._pausado:
                        inimigoM.update(self._personagem1._x, self._personagem1._y)
                        if inimigoM.colisao(self._personagem1):
                            self._personagem1._vida -= 1
                        
                    inimigoM.draw()
                    if self._personagem1._vida <= 0:
                        self._gameover = True

                if not self._pausado:
                    self._pontuação.update()
                self._pontuação.draw()

            else:
                self._telafinal.read()
                self._telafinal.update(self._pontuação._pontos, self._player_name)
                self._telafinal.write()
                self._telafinal.draw(self._tela)
                self._pontuação._pontos = 0
                self._canal1.stop()
                self._tela.blit(self._pontuação.text_surface, (750, 590))

            self.mousepos()
            self.update_level()
            pygame.display.flip()
            self._clock.tick(60)

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