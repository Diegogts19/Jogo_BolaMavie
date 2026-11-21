"""Lista das skins do batedor.

Cada skin é um DICIONÁRIO com:
  'nome'   -> nome que aparece na tela
  'cabelo' -> qual desenho de cabelo usar (chave de BATEDOR_CABELOS e BUSTO_CABELOS)
  'cores'  -> dicionário que troca as cores das letras "coringa" da PALETA

Todas usam os MESMOS desenhos do pixel_art.py; o que muda é a paleta.
A ordem da lista é a ordem de desbloqueio (a primeira já vem liberada).
"""

SKINS = [
    {
        'nome': 'Neymar Kings League',
        'cabelo': 'bone_tras',
        'cores': {'Y': (30, 30, 34), 'X': (30, 30, 34), 'Q': (30, 30, 34), 'G': (110, 110, 115),
                  'Z': (22, 22, 24), 'U': (240, 240, 240), 'E': (30, 45, 110), 'b': (60, 40, 30)},
    },
    {
        'nome': 'Neymar Al Hilal',
        'cabelo': 'curto',
        'cores': {'Y': (40, 120, 220), 'X': (40, 120, 220), 'Q': (40, 120, 220), 'G': (250, 250, 250),
                  'Z': (40, 120, 220), 'U': (40, 120, 220), 'b': (60, 40, 30)},
    },
    {
        'nome': 'Neymar Santos 2026',
        'cabelo': 'bone',
        'cores': {'Y': (245, 245, 245), 'X': (245, 245, 245), 'Q': (245, 245, 245), 'G': (20, 20, 20),
                  'Z': (245, 245, 245), 'U': (245, 245, 245), 'E': (20, 20, 20), 'b': (60, 40, 30),
                  'g': (230, 180, 40)},
    },
    {
        'nome': 'Neymar Copa 2022',
        'cabelo': 'curto',
        'cores': {'Y': (250, 214, 20), 'X': (250, 214, 20), 'Q': (250, 214, 20), 'G': (0, 150, 70),
                  'Z': (30, 60, 170), 'U': (30, 60, 170), 'H': (240, 230, 190), 'b': (150, 110, 70)},
    },
    {
        'nome': 'Neymar PSG',
        'cabelo': 'cacheado',
        'cores': {'Y': (30, 40, 90), 'X': (30, 40, 90), 'Q': (200, 30, 50), 'G': (235, 235, 235),
                  'Z': (30, 40, 90), 'U': (30, 40, 90), 'H': (110, 80, 50), 'J': (220, 190, 120),
                  'b': (110, 75, 50)},
    },
    {
        'nome': 'Neymar Barcelona 2015',
        'cabelo': 'topete',
        'cores': {'Y': (20, 50, 140), 'X': (160, 20, 60), 'Q': (160, 20, 60), 'G': (250, 214, 20),
                  'Z': (20, 50, 140), 'U': (20, 50, 140), 'H': (40, 28, 20), 'J': (150, 110, 60)},
    },
    {
        'nome': 'Neymar Copa 2014',
        'cabelo': 'topete',
        'cores': {'Y': (250, 214, 20), 'X': (250, 214, 20), 'Q': (250, 214, 20), 'G': (0, 150, 70),
                  'Z': (245, 245, 245), 'U': (245, 245, 245), 'H': (60, 45, 30), 'J': (170, 140, 90)},
    },
    {
        'nome': 'Neymar Santos 2011',
        'cabelo': 'moicano',
        'cores': {'Y': (40, 90, 200), 'X': (40, 90, 200), 'Q': (40, 90, 200), 'G': (20, 20, 20),
                  'Z': (40, 90, 200), 'U': (40, 90, 200), 'H': (35, 25, 20), 'J': (235, 210, 130),
                  'c': (245, 230, 215)},
    },
]
