"""Tela de 'NOVA SKIN LIBERADA', quando a felicidade da Mavie enche."""
import math

import pygame

from config import FPS, WIDTH, HEIGHT, QUIT, GAME, AMARELO, BRANCO, VERDE
from skins import SKINS
from sprites import Confete
from utils import desenha_texto, alterna_tela_cheia


def nova_skin_screen(window, assets, indice):
    """Mostra a skin recém-liberada. Devolve GAME ou QUIT."""
    clock = pygame.time.Clock()
    inicio = pygame.time.get_ticks()
    assets['gol'].play()

    confetes = pygame.sprite.Group()
    for i in range(50):
        confetes.add(Confete())

    imagem = assets['bustos'][indice]
    nome = SKINS[indice]['nome'].upper()

    while True:
        clock.tick(FPS)
        agora = pygame.time.get_ticks() - inicio

        for event in pygame.event.get():
            alterna_tela_cheia(event)
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN and agora > 1000:
                if event.key in (pygame.K_SPACE, pygame.K_ESCAPE):
                    return GAME

        confetes.update()

        window.blit(assets['fundo_gol'], (0, 0))
        confetes.draw(window)

        centro = (WIDTH / 2, 280)
        for i in range(12):
            angulo = agora / 1500 + i * math.pi / 6
            p1 = (centro[0] + math.cos(angulo - 0.12) * 400, centro[1] + math.sin(angulo - 0.12) * 400)
            p2 = (centro[0] + math.cos(angulo + 0.12) * 400, centro[1] + math.sin(angulo + 0.12) * 400)
            pygame.draw.polygon(window, (110, 180, 225), [centro, p1, p2])

        escala = 1 + 0.05 * math.sin(agora / 150)
        tamanho = (int(imagem.get_width() * escala), int(imagem.get_height() * escala))
        grande = pygame.transform.scale(imagem, tamanho)
        rect = grande.get_rect()
        rect.center = centro
        window.blit(grande, rect)

        desenha_texto(window, 'NOVA SKIN LIBERADA!', assets['fonte_grande'], AMARELO, (WIDTH / 2, 70), VERDE)
        desenha_texto(window, f'"{nome}"', assets['fonte_media'], BRANCO, (WIDTH / 2, 470))
        desenha_texto(window, 'DESBLOQUEADO', assets['fonte_grande'], AMARELO, (WIDTH / 2, 510))
        if agora > 1000:
            desenha_texto(window, 'ESPAÇO PARA CONTINUAR', assets['fonte_pequena'], BRANCO, (WIDTH / 2, HEIGHT - 25))

        pygame.display.update()
