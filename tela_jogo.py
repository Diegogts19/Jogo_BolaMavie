"""Tela da cobrança do pênalti (o loop principal do jogo)."""
import pygame

from config import (FPS, WIDTH, QUIT, INIT, GAME, GOL, MAVIE, GOL_ESQ, GOL_DIR, GOL_TOPO,
                    BRANCO, AMARELO, VERMELHO)
from dados import salva_dados, muda_felicidade, ganho_por_gol, nivel, velocidade_da_barra, qualidade_minima
from sprites import Mira, Goleiro, Batedor, Bola, BarraQualidade
from utils import desenha_texto, desenha_felicidade, alterna_tela_cheia

MIRANDO_LADO = 0
MIRANDO_ALTURA = 1
QUALIDADE = 2
CORRENDO = 3
CHUTANDO = 4
FIM = 5

GROSSURA_TRAVE = 12


def bola_dentro_do_gol(alvo):
    """True se o alvo está entre as traves e abaixo do travessão."""
    x, y = alvo
    return GOL_ESQ + GROSSURA_TRAVE < x < GOL_DIR - GROSSURA_TRAVE and y > GOL_TOPO + GROSSURA_TRAVE


def bola_na_trave(alvo):
    """True se o alvo está em cima de uma das traves ou do travessão."""
    x, y = alvo
    t = GROSSURA_TRAVE
    trave_esquerda = GOL_ESQ - t <= x <= GOL_ESQ + t and y >= GOL_TOPO - t
    trave_direita = GOL_DIR - t <= x <= GOL_DIR + t and y >= GOL_TOPO - t
    travessao = GOL_TOPO - t <= y <= GOL_TOPO + t and GOL_ESQ - t <= x <= GOL_DIR + t
    return trave_esquerda or trave_direita or travessao


def game_screen(window, assets, dados):
    """Uma cobrança de pênalti. Devolve GOL, MAVIE, GAME, INIT, REINICIAR ou QUIT."""
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    goleiro = Goleiro(assets['goleiro'], nivel(dados))
    batedor = Batedor(assets['batedores'][dados['skin_atual']])
    bola = Bola(assets['bola'])
    mira = Mira(assets['mira'])
    barra = BarraQualidade(60, 75, velocidade_da_barra(dados), qualidade_minima(dados))
    all_sprites.add(goleiro)
    all_sprites.add(batedor)
    all_sprites.add(bola)

    estado = MIRANDO_LADO
    resultado = ''
    alvo = (0, 0)
    chute_bom = False
    inicio_fim = 0
    assets['apito'].play()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            alterna_tela_cheia(event)
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return INIT
                if event.key == pygame.K_SPACE:
                    if estado == MIRANDO_LADO:
                        mira.trava_lado()
                        estado = MIRANDO_ALTURA
                    elif estado == MIRANDO_ALTURA:
                        mira.trava_altura()
                        estado = QUALIDADE
                    elif estado == QUALIDADE:
                        barra.para()
                        batedor.correr()
                        estado = CORRENDO

        if estado == CORRENDO and batedor.chegou:
            alvo = mira.rect.center
            chute_bom = barra.qualidade() >= barra.minimo
            goleiro.pula(alvo, bola_dentro_do_gol(alvo) and not chute_bom)
            bola.chuta(alvo)
            assets['chute'].play()
            estado = CHUTANDO

        all_sprites.update()
        if estado in (MIRANDO_LADO, MIRANDO_ALTURA):
            mira.update()
        if estado == QUALIDADE:
            barra.update()

        if estado == CHUTANDO:
            dentro = bola_dentro_do_gol(alvo)
            pegou = pygame.sprite.collide_mask(bola, goleiro) or bola.chegou
            if dentro and not chute_bom and bola.profundidade() > 0.75 and pegou:
                bola.rebate()
                resultado = 'DEFESA'
                assets['defesa'].play()
            elif bola.chegou:
                if dentro:
                    resultado = 'GOL'
                    assets['gol'].play()
                elif bola_na_trave(alvo):
                    resultado = 'TRAVE'
                    bola.rebate()
                    assets['trave'].play()
                else:
                    resultado = 'FORA'
            if resultado != '':
                estado = FIM
                inicio_fim = pygame.time.get_ticks()

        if estado == FIM and pygame.time.get_ticks() - inicio_fim > 1500:
            ganho = ganho_por_gol(dados)
            if resultado == 'GOL':
                dados['gols'] += 1
                muda_felicidade(dados, ganho)
                proxima_tela = GOL
            elif resultado == 'FORA':
                dados['erros'] += 1
                muda_felicidade(dados, -ganho)
                proxima_tela = MAVIE
            elif resultado == 'TRAVE':
                dados['traves'] += 1
                proxima_tela = GAME
            else:
                dados['defesas'] += 1
                proxima_tela = GAME
            salva_dados(dados)
            return proxima_tela

        window.blit(assets['fundo_campo'], (0, 0))
        all_sprites.draw(window)
        if estado in (MIRANDO_LADO, MIRANDO_ALTURA, QUALIDADE, CORRENDO):
            window.blit(mira.image, mira.rect)
        if estado != MIRANDO_LADO and estado != MIRANDO_ALTURA:
            barra.draw(window)

        fonte = assets['fonte_media']
        if estado == MIRANDO_LADO:
            desenha_texto(window, 'ESPAÇO: ESCOLHA O LADO', fonte, BRANCO, (WIDTH / 2 - 130, 40))
        elif estado == MIRANDO_ALTURA:
            desenha_texto(window, 'ESPAÇO: ESCOLHA A ALTURA', fonte, BRANCO, (WIDTH / 2 - 130, 40))
        elif estado == QUALIDADE:
            desenha_texto(window, 'ESPAÇO: PARE NO VERDE!', fonte, BRANCO, (WIDTH / 2 - 130, 40))
        elif estado == FIM:
            if resultado == 'GOL':
                desenha_texto(window, 'GOOOL!', assets['fonte_titulo'], AMARELO, (WIDTH / 2, 165))
            elif resultado == 'DEFESA':
                desenha_texto(window, 'DEFENDEU!', assets['fonte_titulo'], BRANCO, (WIDTH / 2, 165))
                desenha_texto(window, 'CHUTE FRACO: PASSE DO RISCO BRANCO', fonte, BRANCO, (WIDTH / 2, 215))
            elif resultado == 'TRAVE':
                desenha_texto(window, 'TRAVE!', assets['fonte_titulo'], BRANCO, (WIDTH / 2, 165))
            else:
                desenha_texto(window, 'FORA!', assets['fonte_titulo'], VERMELHO, (WIDTH / 2, 165))
        desenha_texto(window, 'ESC: MENU', assets['fonte_pequena'], BRANCO, (97, 532))

        desenha_felicidade(window, assets, dados)

        pygame.display.update()
