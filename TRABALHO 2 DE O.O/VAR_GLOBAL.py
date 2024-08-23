import pygame

tela_x = 1600
tela_y = 800
tela = pygame.display.set_mode((tela_x, tela_y))
gameover = False
pausado = False

clock = pygame.time.Clock()


pygame.mouse.set_visible(False)


spawn_time = 3000
last_tick = pygame.time.get_ticks()
last_threshold = 0