# TRABALHO 2 DE O.O SIN-141
# PEDRO LEMOS MARIANO - 6968

import pygame
import random
import sys
from C_INIMIGO_M import *
from C_INIMIGO_C import *
from C_INIMIGO_BASE import *
from C_MAIS_VIDA import *
from C_PERS_JOGAVEL import *
from C_PROJETIL import *
from CA_CARGAS import *
from VAR_GLOBAL import *
from C_GERADORES import *

pygame.init()

clock = pygame.time.Clock()

last_tick = pygame.time.get_ticks()
spawn_time = 3000

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