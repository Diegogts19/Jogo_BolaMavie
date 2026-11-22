"""
PÊNALTI DA MAVIE
Arquivo principal (igual ao jogo_v22.py do handout): inicializa o pygame,
carrega os assets e usa uma máquina de estados para trocar de tela.

Para rodar:  python jogo.py
"""
import pygame

from config import WIDTH, HEIGHT, TITULO, QUIT, INIT, GAME, GOL, MAVIE, NOVA_SKIN
from assets import load_assets
from dados import carrega_dados, verifica_nova_skin
from tela_inicial import init_screen
from tela_jogo import game_screen
from tela_gol import gol_screen
from tela_mavie import mavie_screen
from tela_skin import nova_skin_screen

pygame.init()
try:
    pygame.mixer.init()
except pygame.error:
    print('Sem áudio: o jogo vai rodar sem som.')

window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption(TITULO)

assets = load_assets()
dados = carrega_dados()

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window, assets, dados)
    elif state == GAME:
        state = game_screen(window, assets, dados)
    elif state == GOL:
        state = gol_screen(window, assets, dados)
        if state != QUIT and verifica_nova_skin(dados):
            state = NOVA_SKIN
    elif state == MAVIE:
        state = mavie_screen(window, assets, dados)
    elif state == NOVA_SKIN:
        state = nova_skin_screen(window, assets, dados['skin_atual'])

pygame.quit()

