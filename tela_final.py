"""Tela de jogo completo (quando a última skin é liberada)."""
import math

import pygame

from config import FPS, WIDTH, HEIGHT, QUIT, INIT, AMARELO, BRANCO, VERDE
from sprites import Confete
from utils import desenha_texto, alterna_tela_cheia


def final_screen(window, assets):
    """Tela de jogo completo. Devolve INIT (menu) ou QUIT."""
    clock = pygame.time.Clock()
    inicio = pygame.time.get_ticks()
    assets['gol'].play()

    confetes = pygame.sprite.Group()
    for i in range(80):
        confetes.add(Confete())

    cena = assets['cena_final']
    cena_rect = cena.get_rect()

    while True:
        clock.tick(FPS)
        agora = pygame.time.get_ticks() - inicio

        for event in pygame.event.get():
            alterna_tela_cheia(event)
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN and agora > 1500:
                if event.key in (pygame.K_SPACE, pygame.K_ESCAPE):
                    return INIT

        confetes.update()

        window.blit(assets['fundo_gol'], (0, 0))
        centro = (WIDTH / 2, 260)
        for i in range(12):
            angulo = agora / 2000 + i * math.pi / 6
            p1 = (centro[0] + math.cos(angulo - 0.12) * 500, centro[1] + math.sin(angulo - 0.12) * 500)
            p2 = (centro[0] + math.cos(angulo + 0.12) * 500, centro[1] + math.sin(angulo + 0.12) * 500)
            pygame.draw.polygon(window, (110, 180, 225), [centro, p1, p2])

        cena_rect.centerx = WIDTH / 2
        cena_rect.bottom = 445 + int(math.sin(agora / 200) * 6)
        window.blit(cena, cena_rect)
        confetes.draw(window)

        pygame.draw.rect(window, (0, 0, 0), (0, 445, WIDTH, HEIGHT - 445))
        desenha_texto(window, 'JOGO COMPLETO!', assets['fonte_grande'], AMARELO, (WIDTH / 2, 40), VERDE)
        desenha_texto(window, 'NEYMAR VOLTOU COM A BRUNA MARQUEZINE', assets['fonte_media'], BRANCO, (WIDTH / 2, 480))
        desenha_texto(window, 'E GANHOU A COPA DO MUNDO!', assets['fonte_grande'], AMARELO, (WIDTH / 2, 520), VERDE)
        if agora > 1500:
            desenha_texto(window, 'ESPAÇO PARA VOLTAR AO MENU', assets['fonte_pequena'], BRANCO, (WIDTH / 2, 575))

        pygame.display.update()
