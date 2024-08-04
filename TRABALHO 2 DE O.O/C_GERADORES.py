import random
from VAR_GLOBAL import *
from C_INIMIGO_C import *
from C_INIMIGO_M import *
from C_MAIS_VIDA import MAIS_VIDA

def gerador_inimigo():
    x = random.randint(0, tela_x)
    y = random.randint(0, tela_y)
    size = 20
    spd_m = random.randint(4, 5)
    spd_c = random.randint(2, 4)
    cor = (255, 0, 0)
    if random.randint(0, 1) == 0:
        inimigo = InimigoCaveira(x, y, size, spd_c, cor)
    else:
        inimigo = InimigoMorcego(x, y, size, spd_m, cor)
    inimigos.append(inimigo)

inimigos = []

def gerador_vida():
    x = random.randint(0, tela_x)
    y = random.randint(0, tela_y)
    size = 20
    cor = (255, 0, 0)
    maisvida = MAIS_VIDA(x, y, size, cor)
    maisvidas.append(maisvida)

maisvidas = []

def calcular_direcao(origem, destino):
    dir_x = destino[0] - origem[0]
    dir_y = destino[1] - origem[1]
    distancia = math.hypot(dir_x, dir_y)
    if distancia != 0:
        dir_x /= distancia
        dir_y /= distancia
    return dir_x, dir_y

projeteis = []