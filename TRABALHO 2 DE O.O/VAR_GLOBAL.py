import pygame

tela_x = 1600
tela_y = 800
tela = pygame.display.set_mode((tela_x, tela_y))
gameover = False
pausado = False

clock = pygame.time.Clock()

nomes = []
numeros = []

pygame.mouse.set_visible(False)

with open('score.txt', 'r') as file:
    hiscore = int(file.readline())

with open('ranking.txt', 'r') as arquivo:
    for linha in arquivo:
        nome, numero = linha.strip().split()
        
        numero = int(numero)
        nomes.append(nome)
        numeros.append(numero)
    
        print(f"Nome: {nome}, Número: {numero}")

spawn_time = 3000
last_tick = pygame.time.get_ticks()
last_threshold = 0