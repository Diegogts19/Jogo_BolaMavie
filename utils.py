"""Funções usadas por várias telas."""
import pygame

from config import PRETO, BRANCO, VERMELHO, AMARELO, VERDE, WIDTH
from dados import gols_faltando, nivel, zerou_o_jogo
from skins import SKINS


def desenha_texto(superficie, texto, fonte, cor, centro, contorno=PRETO):
    """Desenha um texto centralizado em 'centro', com contorno para dar leitura."""
    if contorno is not None:
        sombra = fonte.render(texto, False, contorno)
        sombra_rect = sombra.get_rect()
        for dx, dy in [(-3, 0), (3, 0), (0, -3), (0, 3), (3, 3)]:
            sombra_rect.center = (centro[0] + dx, centro[1] + dy)
            superficie.blit(sombra, sombra_rect)
    imagem = fonte.render(texto, False, cor)
    rect = imagem.get_rect()
    rect.center = centro
    superficie.blit(imagem, rect)


def expressao_da_mavie(felicidade):
    """Escolhe o rosto da Mavie pelo nível de felicidade."""
    if felicidade >= 70:
        return 'feliz'
    if felicidade >= 35:
        return 'neutra'
    return 'triste'


def desenha_felicidade(superficie, assets, dados):
    """Índice de felicidade da Mavie no canto superior direito."""
    felicidade = dados['felicidade']
    painel = pygame.Rect(WIDTH - 290, 10, 280, 112)
    pygame.draw.rect(superficie, PRETO, painel)
    pygame.draw.rect(superficie, BRANCO, painel, 3)

    rosto = assets['mavie_mini'][expressao_da_mavie(felicidade)]
    superficie.blit(rosto, (painel.x + 10, painel.y + 11))

    fonte = assets['fonte_pequena']
    desenha_texto(superficie, 'FELICIDADE', fonte, BRANCO, (painel.x + 180, painel.y + 18), None)
    desenha_texto(superficie, 'DA MAVIE', fonte, BRANCO, (painel.x + 180, painel.y + 36), None)

    barra = pygame.Rect(painel.x + 84, painel.y + 52, 186, 22)
    pygame.draw.rect(superficie, (60, 60, 60), barra)
    if felicidade >= 70:
        cor = VERDE
    elif felicidade >= 35:
        cor = AMARELO
    else:
        cor = VERMELHO
    cheia = pygame.Rect(barra.x, barra.y, barra.width * felicidade // 100, barra.height)
    pygame.draw.rect(superficie, cor, cheia)
    pygame.draw.rect(superficie, BRANCO, barra, 2)
    desenha_texto(superficie, f'{felicidade}%', fonte, BRANCO, barra.center)

    if zerou_o_jogo(dados):
        texto = 'JOGO COMPLETO!'
    else:
        faltam = gols_faltando(dados)
        palavra = 'GOL' if faltam == 1 else 'GOLS'
        texto = f'NÍVEL {nivel(dados) + 1}/{len(SKINS)}: FALTAM {faltam} {palavra}'
    desenha_texto(superficie, texto, fonte, AMARELO, (painel.centerx, painel.y + 94), None)


def alterna_tela_cheia(event):
    """Tecla F liga/desliga a tela cheia (chamada no for de eventos de cada tela)."""
    if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
        pygame.display.toggle_fullscreen()
