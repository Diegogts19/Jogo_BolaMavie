"""Funções usadas por várias telas."""
import pygame
 
from config import PRETO
 
 
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
 
 
def alterna_tela_cheia(event):
    """Tecla F liga/desliga a tela cheia (chamada no for de eventos de cada tela)."""
    if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
        pygame.display.toggle_fullscreen()