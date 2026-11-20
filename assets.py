"""Carregamento dos assets (imagens, fontes e sons), como no assets.py do handout.

Diferença: as imagens não vêm de arquivos .png. Elas são desenhadas a
partir das listas de strings do pixel_art.py, o que deixa tudo pixelado.
"""
import random
from os import path

import pygame

from config import PASTA_SND, PASTA_FONTE, PIXEL, WIDTH, HEIGHT
import pixel_art


def cria_imagem(mapa, escala, paleta=pixel_art.PALETA):
    """Transforma uma lista de strings em uma imagem (Surface) do pygame."""
    largura = len(mapa[0])
    altura = len(mapa)
    imagem = pygame.Surface((largura, altura), pygame.SRCALPHA)
    for y in range(altura):
        linha = mapa[y]
        for x in range(largura):
            letra = linha[x]
            if letra != '.':
                imagem.set_at((x, y), paleta[letra])
    return pygame.transform.scale(imagem, (largura * escala, altura * escala))


def cria_fundo_campo():
    """Desenha o estádio numa tela pequena (160 x 120) e depois amplia."""
    fundo = pygame.Surface((WIDTH // PIXEL, HEIGHT // PIXEL))
    fundo.fill((20, 30, 70))
    pygame.draw.rect(fundo, (55, 55, 70), (0, 2, 160, 42))
    random.seed(3)
    cores_torcida = [(250, 214, 20), (0, 150, 70), (255, 255, 255), (30, 60, 170), (200, 140, 100)]
    for y in range(4, 42, 3):
        for x in range(0, 160, 2):
            if random.random() < 0.8:
                pygame.draw.rect(fundo, random.choice(cores_torcida), (x, y, 1, 2))
    random.seed()
    for x in range(0, 160, 20):
        cor = (30, 60, 170) if (x // 20) % 2 == 0 else (250, 214, 20)
        pygame.draw.rect(fundo, cor, (x, 44, 20, 6))
    for y in range(50, 120, 10):
        cor = (40, 150, 60) if (y // 10) % 2 == 0 else (52, 166, 72)
        pygame.draw.rect(fundo, cor, (0, y, 160, 10))
    pygame.draw.rect(fundo, (30, 110, 50), (44, 36, 72, 36))
    for x in range(44, 117, 4):
        pygame.draw.line(fundo, (210, 210, 210), (x, 36), (x, 71))
    for y in range(36, 72, 4):
        pygame.draw.line(fundo, (210, 210, 210), (44, y), (115, y))
    branco = (240, 240, 240)
    pygame.draw.line(fundo, branco, (0, 72), (159, 72))
    pygame.draw.lines(fundo, branco, False, [(24, 72), (20, 86), (140, 86), (136, 72)])
    pygame.draw.lines(fundo, branco, False, [(6, 72), (0, 100), (160, 100), (154, 72)])
    pygame.draw.rect(fundo, branco, (79, 103, 2, 2))
    pygame.draw.rect(fundo, branco, (42, 34, 3, 39))
    pygame.draw.rect(fundo, branco, (116, 34, 3, 39))
    pygame.draw.rect(fundo, branco, (42, 34, 77, 3))
    return pygame.transform.scale(fundo, (WIDTH, HEIGHT))


def carrega_fonte(tamanho):
    """Usa a fonte arcade do handout se ela estiver em assets/font."""
    arquivo = path.join(PASTA_FONTE, 'PressStart2P.ttf')
    if path.isfile(arquivo):
        return pygame.font.Font(arquivo, tamanho)
    return pygame.font.Font(None, int(tamanho * 1.8))


class SomMudo:
    """Usado no lugar de um som quando o áudio não funciona no computador."""
    def play(self):
        """Não toca nada."""
        pass

    def stop(self):
        """Não há nada para parar."""
        pass


def carrega_som(nome):
    """Carrega um .wav da pasta de sons; se o áudio falhar, devolve um SomMudo."""
    try:
        return pygame.mixer.Sound(path.join(PASTA_SND, nome))
    except pygame.error:
        return SomMudo()


def carrega_imagens_do_jogo(assets):
    """Campo, goleiro, bola e mira (tela da cobrança)."""
    assets['fundo_campo'] = cria_fundo_campo()
    assets['goleiro'] = cria_imagem(pixel_art.GOLEIRO, PIXEL)
    assets['bola'] = cria_imagem(pixel_art.BOLA, PIXEL)
    assets['mira'] = cria_imagem(pixel_art.MIRA, 4)
    assets['batedor'] = cria_imagem(pixel_art.BATEDOR_CABELOS['curto'] + pixel_art.BATEDOR_CORPO, PIXEL + 1)


def carrega_fontes(assets):
    """Fontes em quatro tamanhos: título, grande, média e pequena."""
    assets['fonte_titulo'] = carrega_fonte(40)
    assets['fonte_grande'] = carrega_fonte(24)
    assets['fonte_media'] = carrega_fonte(16)
    assets['fonte_pequena'] = carrega_fonte(11)


def carrega_sons(assets):
    """Carrega todos os efeitos sonoros e os áudios da equipe."""
    for nome in ['chute', 'apito', 'gol', 'defesa', 'bonk', 'trave', 'aminu', 'bolada_mavie']:
        assets[nome] = carrega_som(nome + '.wav')


def load_assets():
    """Guarda tudo num dicionário. Cada função acima carrega uma parte."""
    assets = {}
    carrega_imagens_do_jogo(assets)
    carrega_fontes(assets)
    carrega_sons(assets)
    return assets

