"""
PÊNALTI DA MAVIE
Arquivo principal (igual ao jogo_v22.py do handout): inicializa o pygame,
carrega os assets e usa uma máquina de estados para trocar de tela.

Para rodar:  python jogo.py
"""
import pygame

from config import WIDTH, HEIGHT, TITULO, QUIT, INIT, GAME
from assets import load_assets
from tela_inicial import init_screen
from tela_jogo import game_screen

pygame.init()
try:
    pygame.mixer.init()
except pygame.error:
    print('Sem áudio: o jogo vai rodar sem som.')

window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption(TITULO)

assets = load_assets()

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window, assets)
    elif state == GAME:
        state = game_screen(window, assets)

pygame.quit()

