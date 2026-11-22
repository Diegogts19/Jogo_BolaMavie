"""Tela inicial: título, placar e felicidade da Mavie."""
import pygame

from config import FPS, WIDTH, HEIGHT, QUIT, GAME, BRANCO, AMARELO, VERDE
from utils import desenha_texto, desenha_felicidade, alterna_tela_cheia


def init_screen(window, assets, dados):
    """Menu: escolher skin, ver placar e felicidade. Devolve GAME, REINICIAR ou QUIT."""
    clock = pygame.time.Clock()

    escuro = pygame.Surface((WIDTH, HEIGHT))
    escuro.fill((0, 0, 0))
    escuro.set_alpha(150)

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            alterna_tela_cheia(event)
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return GAME
                if event.key == pygame.K_ESCAPE:
                    return QUIT

        window.blit(assets['fundo_campo'], (0, 0))
        window.blit(escuro, (0, 0))

        desenha_texto(window, 'PÊNALTI', assets['fonte_titulo'], AMARELO, (WIDTH / 2, 220))
        desenha_texto(window, 'DA MAVIE', assets['fonte_titulo'], VERDE, (WIDTH / 2, 280))

        if (pygame.time.get_ticks() // 500) % 2 == 0:
            desenha_texto(window, 'APERTE ESPAÇO PARA BATER', assets['fonte_media'], BRANCO, (WIDTH / 2, 510))

        fonte = assets['fonte_pequena']
        desenha_texto(window, f"GOLS: {dados['gols']}  NA MAVIE: {dados['erros']}  DEFESAS: {dados['defesas']}  TRAVES: {dados['traves']}",
                      fonte, BRANCO, (WIDTH / 2, 545))
        desenha_texto(window, 'F: TELA CHEIA   ESC: SAIR', fonte, BRANCO, (WIDTH / 2, 575))

        desenha_felicidade(window, assets, dados)

        pygame.display.update()

