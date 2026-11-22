"""Tela inicial: escolha do personagem (skin), placar e felicidade da Mavie."""
import pygame

from config import FPS, WIDTH, HEIGHT, QUIT, GAME, BRANCO, AMARELO, VERDE, CINZA
from dados import salva_dados
from skins import SKINS
from utils import desenha_texto, desenha_felicidade, alterna_tela_cheia


def desenha_lista_de_skins(window, assets, dados):
    """Fileira com todas as skins: liberadas coloridas, trancadas como silhueta."""
    espaco = WIDTH // len(SKINS)
    for i in range(len(SKINS)):
        centro_x = espaco * i + espaco // 2
        if i < dados['skins_liberadas']:
            imagem = assets['bustos_mini'][i]
        else:
            imagem = assets['bustos_trancados'][i]
        rect = imagem.get_rect()
        rect.center = (centro_x, 440)
        moldura = rect.inflate(10, 10)
        pygame.draw.rect(window, (0, 0, 0), moldura)
        cor = AMARELO if i == dados['skin_atual'] else CINZA
        pygame.draw.rect(window, cor, moldura, 3)
        window.blit(imagem, rect)
        if i >= dados['skins_liberadas']:
            desenha_texto(window, '?', assets['fonte_grande'], BRANCO, rect.center)


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
                if event.key == pygame.K_RIGHT:
                    dados['skin_atual'] = (dados['skin_atual'] + 1) % dados['skins_liberadas']
                    salva_dados(dados)
                if event.key == pygame.K_LEFT:
                    dados['skin_atual'] = (dados['skin_atual'] - 1) % dados['skins_liberadas']
                    salva_dados(dados)

        window.blit(assets['fundo_campo'], (0, 0))
        window.blit(escuro, (0, 0))

        desenha_texto(window, 'PÊNALTI', assets['fonte_grande'], AMARELO, (270, 40))
        desenha_texto(window, 'DA MAVIE', assets['fonte_grande'], VERDE, (270, 80))

        skin = dados['skin_atual']
        imagem = assets['bustos'][skin]
        rect = imagem.get_rect()
        rect.center = (WIDTH / 2, 245)
        window.blit(imagem, rect)
        if dados['skins_liberadas'] > 1:
            desenha_texto(window, '<', assets['fonte_titulo'], BRANCO, (rect.left - 50, rect.centery))
            desenha_texto(window, '>', assets['fonte_titulo'], BRANCO, (rect.right + 50, rect.centery))
        desenha_texto(window, SKINS[skin]['nome'].upper(), assets['fonte_media'], AMARELO, (WIDTH / 2, 365))
        desenha_texto(window, f"PERSONAGENS: {dados['skins_liberadas']}/{len(SKINS)}", assets['fonte_pequena'],
                      BRANCO, (WIDTH / 2, 392))

        desenha_lista_de_skins(window, assets, dados)

        if (pygame.time.get_ticks() // 500) % 2 == 0:
            desenha_texto(window, 'APERTE ESPAÇO PARA BATER', assets['fonte_media'], BRANCO, (WIDTH / 2, 510))

        fonte = assets['fonte_pequena']
        desenha_texto(window, f"GOLS: {dados['gols']}  NA MAVIE: {dados['erros']}  DEFESAS: {dados['defesas']}  TRAVES: {dados['traves']}",
                      fonte, BRANCO, (WIDTH / 2, 545))
        desenha_texto(window, '< > SKIN   F: TELA CHEIA   ESC: SAIR', fonte, BRANCO, (WIDTH / 2, 575))

        desenha_felicidade(window, assets, dados)

        pygame.display.update()
