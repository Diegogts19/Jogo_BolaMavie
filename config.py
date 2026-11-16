"""Constantes do jogo (igual ao config.py do handout)."""
from os import path

PASTA_ASSETS = path.join(path.dirname(__file__), 'assets')
PASTA_SND = path.join(PASTA_ASSETS, 'snd')
PASTA_FONTE = path.join(PASTA_ASSETS, 'font')
ARQUIVO_DADOS = path.join(path.dirname(__file__), 'dados_mavie.txt')

WIDTH = 800
HEIGHT = 600
FPS = 60
TITULO = 'Pênalti da Mavie'

PIXEL = 5

GOL_ESQ = 220
GOL_DIR = 580
GOL_TOPO = 180
GOL_CHAO = 360
MARCA_PENALTI = (400, 520)

FELICIDADE_INICIAL = 50
GOLS_POR_SKIN = [1, 1, 2, 2, 3, 3, 4]

VELOCIDADE_BARRA_INICIAL = 4
AUMENTO_VELOCIDADE_BARRA = 1.5
QUALIDADE_MINIMA_INICIAL = 0.35
AUMENTO_QUALIDADE_MINIMA = 0.07

FRASES_MAVIE = [
    'Pô, pra que jogar bola na Mavie?',
    'Arroganthi!',
    'Arroganthi, pra que jogar bola na Mavie?',
    'Pra que isso, pô? Pra que isso?',
]

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AMARELO = (250, 214, 20)
VERDE = (0, 150, 70)
AZUL = (30, 60, 170)
VERMELHO = (230, 40, 40)
ROSA = (240, 90, 160)
CINZA = (120, 120, 120)

QUIT = 0
INIT = 1
GAME = 2
GOL = 3
MAVIE = 4
NOVA_SKIN = 5
FINAL = 6
REINICIAR = 7

BOTAO_REINICIAR = (12, 552, 170, 38)
