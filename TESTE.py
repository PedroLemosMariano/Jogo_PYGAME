# TRABALHO 2 DE O.O SIN-141
# PEDRO LEMOS MARIANO - 6968

import pygame
import random
import sys
import math

pygame.init()

tela_x = 1600
tela_y = 800
tela = pygame.display.set_mode((tela_x, tela_y))

clock = pygame.time.Clock()

last_tick = pygame.time.get_ticks()
spawn_time = 3000

#-------------------------PERSONAGEM PRINCIPAL(MANOEL)
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

#-------------------------PODER
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

def calcular_direcao(origem, destino):
    dir_x = destino[0] - origem[0]
    dir_y = destino[1] - origem[1]
    distancia = math.hypot(dir_x, dir_y)
    if distancia != 0:
        dir_x /= distancia
        dir_y /= distancia
    return dir_x, dir_y

projeteis = []

#-------------------------INIMIGO CLASSE PAI
class InimigoBase:
    def __init__(self, x, y, size, spd, cor, imagens):
        self.x = x
        self.y = y
        self.size = size
        self.spd = spd
        self.cor = cor
        self.imagens = imagens
        self.image = imagens['frente']

    def update(self, player_x, player_y):
        dir_x = player_x - self.x
        dir_y = player_y - self.y
        distancia = math.hypot(dir_x, dir_y)
        if distancia != 0:
            dir_x /= distancia
            dir_y /= distancia

        self.x += dir_x * self.spd
        self.y += dir_y * self.spd

        if abs(dir_x) > abs(dir_y):
            self.image = self.imagens['ladoD'] if dir_x > 0 else self.imagens['ladoE']
        else:
            self.image = self.imagens['frente'] if dir_y > 0 else self.imagens['costa']

    def draw(self):
        tela.blit(self.image, (self.x - 70, self.y - 70))

    def colisao(self, jogador):
        distancia = math.hypot(self.x - jogador.x, self.y - jogador.y)
        return distancia < (self.size + jogador.size)

#-------------------------CAVEIRA
class InimigoCaveira(InimigoBase):
    def __init__(self, x, y, size, spd, cor):
        imagens = {
            'frente': Caveira_frente,
            'costa': Caveira_costa,
            'ladoD': Caveira_ladoD,
            'ladoE': Caveira_ladoE,
        }
        super().__init__(x, y, size, spd, cor, imagens)

#------------------------MORCEGO
class InimigoMorcego(InimigoBase):
    def __init__(self, x, y, size, spd, cor):
        imagens = {
            'frente': Morcego_frente,
            'costa': Morcego_costa,
            'ladoD': Morcego_ladoD,
            'ladoE': Morcego_ladoE,
        }
        super().__init__(x, y, size, spd, cor, imagens)

#------------------------GERADOR DE INIMIGO
def gerador_inimigo():
    x = random.randint(0, tela_x)
    y = random.randint(0, tela_y)
    size = 20
    spd_m = random.randint(4, 5)
    spd_c = random.randint(2, 4)
    cor = (255, 0, 0)
    if random.randint(0, 1) == 0:
        inimigo = InimigoCaveira(x, y, size, spd_c, cor)
        Som_Caveira.play()
    else:
        inimigo = InimigoMorcego(x, y, size, spd_m, cor)
        Som_Morcego.play()
    inimigos.append(inimigo)

inimigos = []

#------------------------VIDA EXTRA
class MAIS_VIDA:
    def __init__(self, x, y,size , cor):
        self.x = x
        self.y = y
        self.size = size
        self.cor = cor
        self.image = Coracao_vermelho
    
    def draw(self):
        tela.blit(self.image, (self.x - 70, self.y - 70))
    
    def colisao(self, jogador):
        distancia = math.hypot(self.x - jogador.x, self.y - jogador.y)
        return distancia < (self.size + jogador.size)

def gerador_vida():
    x = random.randint(0, tela_x)
    y = random.randint(0, tela_y)
    size = 20
    cor = (255, 0, 0)
    maisvida = MAIS_VIDA(x, y, size, cor)
    Som_Vida.play()
    maisvidas.append(maisvida)

maisvidas = []

#------------------------CARGAS DO JOGO
gramado = pygame.image.load('IMAGENS\Cemiterio2.png')
Som_game_over = pygame.mixer.Sound('SONS\Som_Game_Over.mp3')
Som_Tema = pygame.mixer.Sound('SONS\Som_Tema.mp3')
Som_Tema.set_volume(0.02)

Manoel_f = pygame.image.load('IMAGENS\Manoel_frente.png')
Manoel_c = pygame.image.load('IMAGENS\Manoel_costa.png')
Manoel_le = pygame.image.load('IMAGENS\Manoel_ladoE.png')
Manoel_ld = pygame.image.load('IMAGENS\Manoel_ladoD.png')
Manoel_frente = pygame.transform.scale(Manoel_f, (128, 128))
Manoel_costa = pygame.transform.scale(Manoel_c, (128, 128))
Manoel_ladoE = pygame.transform.scale(Manoel_le, (128, 128))
Manoel_ladoD = pygame.transform.scale(Manoel_ld, (128, 128))

Caveira_f = pygame.image.load('IMAGENS\Caveira_frente.png')
Caveira_c = pygame.image.load('IMAGENS\Caveira_costa.png')
Caveira_le = pygame.image.load('IMAGENS\Caveira_ladoE.png')
Caveira_ld = pygame.image.load('IMAGENS\Caveira_ladoD.png')
Caveira_frente = pygame.transform.scale(Caveira_f, (96, 96))
Caveira_costa = pygame.transform.scale(Caveira_c, (96, 96))
Caveira_ladoE = pygame.transform.scale(Caveira_le, (96, 96))
Caveira_ladoD = pygame.transform.scale(Caveira_ld, (96, 96))
Som_Caveira = pygame.mixer.Sound('SONS\Som_Caveira.mp3')

Morcego_f = pygame.image.load('IMAGENS\Morcego_frente.png')
Morcego_c = pygame.image.load('IMAGENS\Morcego_costa.png')
Morcego_le = pygame.image.load('IMAGENS\Morcego_ladoE.png')
Morcego_ld = pygame.image.load('IMAGENS\Morcego_ladoD.png')
Morcego_frente = pygame.transform.scale(Morcego_f, (80, 80))
Morcego_costa = pygame.transform.scale(Morcego_c, (80, 80))
Morcego_ladoE = pygame.transform.scale(Morcego_le, (80, 80))
Morcego_ladoD = pygame.transform.scale(Morcego_ld, (80, 80))
Som_Morcego = pygame.mixer.Sound('SONS\Som_Morcego.mp3')

Coracao_v = pygame.image.load('IMAGENS\Coracao_vermelho.png')
Coracao_vermelho = pygame.transform.scale(Coracao_v, (64, 64))
Som_Vida = pygame.mixer.Sound('SONS\Som_Vida.mp3')
Som_Pegar_Vida = pygame.mixer.Sound('SONS\Som_Pegar_Vida.mp3')

Bola_a = pygame.image.load('IMAGENS\Bola_arma2.png')
Bola_arma = pygame.transform.scale(Bola_a, (32, 32))

personagem1 = PERS_JOGAVEL(tela_x / 2, tela_y / 2, 25, 5, (0, 255, 0))

#------------------------MAIN DO JOGO
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                dir_x, dir_y = calcular_direcao((personagem1.x, personagem1.y), (mouse_x, mouse_y))
                projeteis.append(Projetil(personagem1.x, personagem1.y, dir_x, dir_y))

    tela.blit(gramado, (0, 0))

    personagem1.update()
    personagem1.draw()
    personagem1.bordas()
    personagem1.barravida()

    tick_atual = pygame.time.get_ticks()
    if tick_atual - last_tick >= spawn_time:
        gerador_inimigo()
        if random.randint(1,4) == 3:
            gerador_vida()
        last_tick = tick_atual

    for inimigo in inimigos:
        inimigo.update(personagem1.x, personagem1.y)
        if inimigo.colisao(personagem1):
            personagem1.vida -= 1
            if personagem1.vida <= 0:
                Som_game_over.play()
                pygame.quit()
                sys.exit()
        inimigo.draw()

    for poder in projeteis[:]:
        poder.update()
        inimigo_colidido = poder.colisao(inimigos)
        if inimigo_colidido:
            inimigos.remove(inimigo_colidido)
            projeteis.remove(poder)
        poder.draw()

    for vida in maisvidas:
        vida.draw()
        if vida.colisao(personagem1):
            personagem1.vida += 25
            Som_Pegar_Vida.play()
            maisvidas.remove(vida)
        if personagem1.vida > 100:
            personagem1.vida = 100

    for projetil in projeteis:
        projetil.update()
        projetil.draw()

    pygame.display.flip()
    clock.tick(60)
