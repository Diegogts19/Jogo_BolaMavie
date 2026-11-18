"""
Gera os efeitos sonoros 8-bit do jogo (arquivos .wav em assets/snd).
Não precisa rodar: os sons já vêm prontos. Fica aqui só para mostrar
de onde eles vieram. Usa só bibliotecas padrão do Python (wave, math, random).
Os áudios aminu.wav e bolada_mavie.wav não são gerados aqui: foram tirados de vídeos da equipe.
"""
import math
import random
import struct
import wave

TAXA = 22050


def onda_quadrada(freq, t):
    return 1.0 if math.sin(2 * math.pi * freq * t) >= 0 else -1.0


def salva(nome, amostras):
    with wave.open(f'assets/snd/{nome}', 'w') as arq:
        arq.setnchannels(1)
        arq.setsampwidth(2)
        arq.setframerate(TAXA)
        dados = b''
        for a in amostras:
            a = max(-1.0, min(1.0, a))
            dados += struct.pack('<h', int(a * 12000))
        arq.writeframes(dados)


def gera(duracao, funcao):
    n = int(TAXA * duracao)
    return [funcao(i / TAXA, i / n) for i in range(n)]


random.seed(7)
salva('chute.wav', gera(0.12, lambda t, p: (random.uniform(-1, 1) * 0.6 + onda_quadrada(90, t) * 0.4) * (1 - p)))
salva('apito.wav', gera(0.35, lambda t, p: onda_quadrada(1900 + 120 * math.sin(60 * t), t) * 0.5 * (1 if p < 0.9 else 0)))
notas = [523, 659, 784, 1046]
salva('gol.wav', gera(1.2, lambda t, p: onda_quadrada(notas[min(int(t / 0.12), 3)], t) * 0.35 * (1 - p) + random.uniform(-1, 1) * 0.3 * math.sin(math.pi * p)))
salva('defesa.wav', gera(0.2, lambda t, p: onda_quadrada(140 - 80 * p, t) * (1 - p)))
salva('bonk.wav', gera(0.4, lambda t, p: onda_quadrada(700 - 500 * p + 40 * math.sin(80 * t), t) * 0.6 * (1 - p)))
salva('trave.wav', gera(0.6, lambda t, p: (onda_quadrada(1320, t) * 0.5 + onda_quadrada(1760, t) * 0.3) * (1 - p) ** 2))
print('Sons gerados!')
