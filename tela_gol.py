"""Tela de comemoração do gol: nosso craque + 'AMINU!'."""
import math

import pygame

from config import FPS, WIDTH, HEIGHT, QUIT, GAME, AMARELO, VERDE, BRANCO
from dados import ganho_por_gol
from sprites import Confete
from utils import desenha_texto, alterna_tela_cheia


def gol_screen(window, assets, dados):
    """Comemoração "AMINU!" com o áudio da equipe. Devolve GAME ou QUIT."""
    clock = pygame.time.Clock()
    inicio = pygame.time.get_ticks()
    assets['aminu'].play()

    confetes = pygame.sprite.Group()
    for i in range(50):
        confetes.add(Confete())

    craque = assets['craque']
    craque_rect = craque.get_rect()

    while True:
        clock.tick(FPS)
        agora = pygame.time.get_ticks() - inicio

        for event in pygame.event.get():
            alterna_tela_cheia(event)
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN and agora > 800:
                if event.key in (pygame.K_SPACE, pygame.K_ESCAPE):
                    assets['aminu'].stop()
                    return GAME

        confetes.update()

        craque_rect.centerx = WIDTH / 2
        craque_rect.bottom = 450 + int(math.sin(agora / 120) * 10)

        window.blit(assets['fundo_gol'], (0, 0))
        confetes.draw(window)
        window.blit(craque, craque_rect)
        pygame.draw.rect(window, (0, 0, 0), (0, 450, WIDTH, HEIGHT - 450))
        desenha_texto(window, 'AMINU!', assets['fonte_titulo'], AMARELO, (WIDTH / 2, 500), VERDE)
        desenha_texto(window, f'+{ganho_por_gol(dados)} DE FELICIDADE PRA MAVIE', assets['fonte_pequena'], BRANCO, (WIDTH / 2, 545))
        if agora > 800:
            desenha_texto(window, 'ESPAÇO PARA CONTINUAR', assets['fonte_pequena'], BRANCO, (WIDTH / 2, 575))

        pygame.display.update()
