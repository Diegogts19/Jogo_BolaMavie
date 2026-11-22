"""Salva e carrega a felicidade da Mavie e o placar num arquivo de texto.

Assim o índice continua o mesmo quando o jogo é fechado e aberto de novo
(conteúdo de 'Armazenamento permanente em arquivos').

Formato do arquivo (uma informação por linha):
    felicidade=50
    gols=0
    erros=0
    defesas=0
    traves=0
    skins_liberadas=1
    skin_atual=0
"""
import math

from config import (ARQUIVO_DADOS, FELICIDADE_INICIAL, GOLS_POR_SKIN, VELOCIDADE_BARRA_INICIAL,
                    AUMENTO_VELOCIDADE_BARRA, QUALIDADE_MINIMA_INICIAL, AUMENTO_QUALIDADE_MINIMA)
from skins import SKINS


def dados_iniciais():
    """Dicionário com o progresso de um jogo novo."""
    return {'felicidade': FELICIDADE_INICIAL, 'gols': 0, 'erros': 0, 'defesas': 0, 'traves': 0,
            'skins_liberadas': 1, 'skin_atual': 0}


def carrega_dados():
    """Lê o progresso salvo em dados_mavie.txt (ou começa do zero)."""
    dados = dados_iniciais()
    try:
        with open(ARQUIVO_DADOS, 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split('=')
                if len(partes) == 2 and partes[0] in dados:
                    dados[partes[0]] = int(partes[1])
    except (FileNotFoundError, ValueError):
        pass
    return dados


def salva_dados(dados):
    """Grava o dicionário dados no arquivo, uma informação por linha."""
    with open(ARQUIVO_DADOS, 'w') as arquivo:
        for chave, valor in dados.items():
            arquivo.write(f'{chave}={valor}\n')


def muda_felicidade(dados, quantidade):
    """Soma (ou subtrai) da felicidade, sempre entre 0 e 100."""
    dados['felicidade'] = max(0, min(100, dados['felicidade'] + quantidade))


def nivel(dados):
    """Nível = quantas skins já foram liberadas além da primeira (0 a 7)."""
    return dados['skins_liberadas'] - 1


def gols_necessarios(dados):
    """Quantos gols seguidos enchem a felicidade no nível atual."""
    indice = min(nivel(dados), len(GOLS_POR_SKIN) - 1)
    return GOLS_POR_SKIN[indice]


def ganho_por_gol(dados):
    """Quanto cada gol soma (e cada bola na Mavie tira) da felicidade.

    Ex.: precisa de 2 gols -> (100 - 50) / 2 = 25 por gol.
    math.ceil arredonda para cima, para não faltar 1% no final.
    """
    return math.ceil((100 - FELICIDADE_INICIAL) / gols_necessarios(dados))


def gols_faltando(dados):
    """Quantos gols ainda faltam para a próxima skin."""
    return math.ceil((100 - dados['felicidade']) / ganho_por_gol(dados))


def velocidade_da_barra(dados):
    """A barrinha da qualidade fica mais rápida a cada nível."""
    return VELOCIDADE_BARRA_INICIAL + AUMENTO_VELOCIDADE_BARRA * nivel(dados)


def qualidade_minima(dados):
    """Qualidade mínima (0 a 1) para o goleiro não pegar."""
    return QUALIDADE_MINIMA_INICIAL + AUMENTO_QUALIDADE_MINIMA * nivel(dados)


def zerou_o_jogo(dados):
    """True quando todas as skins já foram liberadas."""
    return dados['skins_liberadas'] == len(SKINS)

"""Salva e carrega a felicidade da Mavie e o placar num arquivo de texto.

Assim o índice continua o mesmo quando o jogo é fechado e aberto de novo
(conteúdo de 'Armazenamento permanente em arquivos').

Formato do arquivo (uma informação por linha):
    felicidade=50
    gols=0
    erros=0
    defesas=0
    traves=0
    skins_liberadas=1
    skin_atual=0
"""
import math

from config import (ARQUIVO_DADOS, FELICIDADE_INICIAL, GOLS_POR_SKIN, VELOCIDADE_BARRA_INICIAL,
                    AUMENTO_VELOCIDADE_BARRA, QUALIDADE_MINIMA_INICIAL, AUMENTO_QUALIDADE_MINIMA)
from skins import SKINS


def dados_iniciais():
    """Dicionário com o progresso de um jogo novo."""
    return {'felicidade': FELICIDADE_INICIAL, 'gols': 0, 'erros': 0, 'defesas': 0, 'traves': 0,
            'skins_liberadas': 1, 'skin_atual': 0}


def carrega_dados():
    """Lê o progresso salvo em dados_mavie.txt (ou começa do zero)."""
    dados = dados_iniciais()
    try:
        with open(ARQUIVO_DADOS, 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split('=')
                if len(partes) == 2 and partes[0] in dados:
                    dados[partes[0]] = int(partes[1])
    except (FileNotFoundError, ValueError):
        pass
    return dados


def salva_dados(dados):
    """Grava o dicionário dados no arquivo, uma informação por linha."""
    with open(ARQUIVO_DADOS, 'w') as arquivo:
        for chave, valor in dados.items():
            arquivo.write(f'{chave}={valor}\n')


def muda_felicidade(dados, quantidade):
    """Soma (ou subtrai) da felicidade, sempre entre 0 e 100."""
    dados['felicidade'] = max(0, min(100, dados['felicidade'] + quantidade))


def nivel(dados):
    """Nível = quantas skins já foram liberadas além da primeira (0 a 7)."""
    return dados['skins_liberadas'] - 1


def gols_necessarios(dados):
    """Quantos gols seguidos enchem a felicidade no nível atual."""
    indice = min(nivel(dados), len(GOLS_POR_SKIN) - 1)
    return GOLS_POR_SKIN[indice]


def ganho_por_gol(dados):
    """Quanto cada gol soma (e cada bola na Mavie tira) da felicidade.

    Ex.: precisa de 2 gols -> (100 - 50) / 2 = 25 por gol.
    math.ceil arredonda para cima, para não faltar 1% no final.
    """
    return math.ceil((100 - FELICIDADE_INICIAL) / gols_necessarios(dados))


def gols_faltando(dados):
    """Quantos gols ainda faltam para a próxima skin."""
    return math.ceil((100 - dados['felicidade']) / ganho_por_gol(dados))


def velocidade_da_barra(dados):
    """A barrinha da qualidade fica mais rápida a cada nível."""
    return VELOCIDADE_BARRA_INICIAL + AUMENTO_VELOCIDADE_BARRA * nivel(dados)


def qualidade_minima(dados):
    """Qualidade mínima (0 a 1) para o goleiro não pegar."""
    return QUALIDADE_MINIMA_INICIAL + AUMENTO_QUALIDADE_MINIMA * nivel(dados)


def zerou_o_jogo(dados):
    """True quando todas as skins já foram liberadas."""
    return dados['skins_liberadas'] == len(SKINS)


def verifica_nova_skin(dados):
    """Se a felicidade encheu (100%), libera a próxima skin.

    Devolve True quando uma skin nova foi liberada. A felicidade volta
    para o valor inicial, para o jogador ter que encher de novo.
    """
    if dados['felicidade'] >= 100 and dados['skins_liberadas'] < len(SKINS):
        dados['skins_liberadas'] += 1
        dados['skin_atual'] = dados['skins_liberadas'] - 1
        dados['felicidade'] = FELICIDADE_INICIAL
        salva_dados(dados)
        return True
    return False

