"""Tela de confirmação para reiniciar o jogo (apaga todo o progresso)."""
import pygame

from config import FPS, WIDTH, HEIGHT, QUIT, INIT, BRANCO, AMARELO, VERMELHO
from dados import dados_iniciais, salva_dados
from utils import desenha_texto, alterna_tela_cheia, desenha_botao, clicou_no_botao

BOTAO_SIM = (WIDTH / 2 - 190, 360, 170, 50)
BOTAO_NAO = (WIDTH / 2 + 20, 360, 170, 50)


def reiniciar_screen(window, assets, dados):
    """Pergunta se quer apagar o progresso. Devolve INIT ou QUIT."""
    clock = pygame.time.Clock()

    fundo = window.copy()
    escuro = pygame.Surface((WIDTH, HEIGHT))
    escuro.fill((0, 0, 0))
    escuro.set_alpha(190)

    while True:
        clock.tick(FPS)

        confirmou = False
        for event in pygame.event.get():
            alterna_tela_cheia(event)
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    confirmou = True
                if event.key in (pygame.K_n, pygame.K_ESCAPE):
                    return INIT
            if clicou_no_botao(event, BOTAO_SIM):
                confirmou = True
            if clicou_no_botao(event, BOTAO_NAO):
                return INIT

        if confirmou:
            dados.update(dados_iniciais())
            salva_dados(dados)
            return INIT

        window.blit(fundo, (0, 0))
        window.blit(escuro, (0, 0))
        desenha_texto(window, 'REINICIAR O JOGO?', assets['fonte_grande'], AMARELO, (WIDTH / 2, 210))
        desenha_texto(window, 'TODO O PROGRESSO SERÁ APAGADO:', assets['fonte_pequena'], BRANCO, (WIDTH / 2, 265))
        desenha_texto(window, 'SKINS, PLACAR E FELICIDADE DA MAVIE', assets['fonte_pequena'], VERMELHO, (WIDTH / 2, 290))
        desenha_botao(window, assets, 'SIM (S)', BOTAO_SIM)
        desenha_botao(window, assets, 'NÃO (N)', BOTAO_NAO)

        pygame.display.update()
