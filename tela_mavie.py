"""Tela de quando o chute vai para fora: a bola acerta a Mavie (de leve!)."""
import random

import pygame

from config import FPS, WIDTH, QUIT, GAME, FRASES_MAVIE, BRANCO, AMARELO, VERMELHO
from dados import ganho_por_gol
from sprites import Estrela
from utils import desenha_texto, alterna_tela_cheia

TEMPO_BATIDA = 700
TEMPO_TRISTE = 1500


def mavie_screen(window, assets, dados):
    """Animação da bola acertando a Mavie e frase do erro. Devolve GAME ou QUIT."""
    clock = pygame.time.Clock()
    inicio = pygame.time.get_ticks()
    assets['bolada_mavie'].play()

    frase = FRASES_MAVIE[(dados['erros'] - 1) % len(FRASES_MAVIE)]

    centro_rosto = (WIDTH / 2, 270)
    estrelas = pygame.sprite.Group()
    for i in range(5):
        estrelas.add(Estrela(assets['estrela'], (WIDTH / 2, 120), i * 1.256))

    bola_x = -80
    bola_y = 120
    bola_vx = 0
    bola_vy = 0
    bateu = False

    while True:
        clock.tick(FPS)
        agora = pygame.time.get_ticks() - inicio

        for event in pygame.event.get():
            alterna_tela_cheia(event)
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN and agora > TEMPO_TRISTE + 500:
                if event.key in (pygame.K_SPACE, pygame.K_ESCAPE):
                    assets['bolada_mavie'].stop()
                    return GAME

        if agora < TEMPO_BATIDA:
            t = agora / TEMPO_BATIDA
            bola_x = -80 + (centro_rosto[0] - 40 + 80) * t
            bola_y = 120 + (centro_rosto[1] + 30 - 120) * t
            tamanho = int(40 + 100 * t)
        else:
            if not bateu:
                bateu = True
                assets['bonk'].play()
                bola_vx = -9
                bola_vy = -12
            bola_x += bola_vx
            bola_y += bola_vy
            bola_vy += 0.8
            tamanho = 140

        if agora < TEMPO_BATIDA:
            expressao = 'feliz'
        elif agora < TEMPO_TRISTE:
            expressao = 'bonk'
        else:
            expressao = 'triste'

        tremor = (0, 0)
        if TEMPO_BATIDA <= agora < TEMPO_BATIDA + 300:
            tremor = (random.randint(-8, 8), random.randint(-8, 8))

        window.blit(assets['fundo_mavie'], (0, 0))
        rosto = assets['mavie'][expressao]
        rosto_rect = rosto.get_rect()
        rosto_rect.center = (centro_rosto[0] + tremor[0], centro_rosto[1] + tremor[1])
        window.blit(rosto, rosto_rect)

        if bateu:
            estrelas.update()
            estrelas.draw(window)

        bola = pygame.transform.scale(assets['bola'], (tamanho, tamanho))
        bola_rect = bola.get_rect()
        bola_rect.center = (bola_x, bola_y)
        window.blit(bola, bola_rect)

        if agora >= TEMPO_TRISTE:
            desenha_texto(window, frase, assets['fonte_media'], AMARELO, (WIDTH / 2, 50))
            desenha_texto(window, 'VOCÊ ACERTOU A BOLA NA MAVIE', assets['fonte_grande'], BRANCO, (WIDTH / 2, 485))
            desenha_texto(window, f'-{ganho_por_gol(dados)} DE FELICIDADE', assets['fonte_media'], VERMELHO, (WIDTH / 2, 530))
        if agora > TEMPO_TRISTE + 500:
            desenha_texto(window, 'ESPAÇO PARA VOLTAR', assets['fonte_pequena'], BRANCO, (WIDTH / 2, 575))

        pygame.display.update()
