# Pênalti da Mavie

Jogo de pênalti em pixel art feito com pygame, seguindo o handout de PyGame de Design de Software.

# Autores

- Alexandre Trancoso
- Leonardo Riglioni
- Diego Siqueira

# Descrição

Você cobra pênaltis escolhendo o lado, a altura e a qualidade do chute. Gol deixa a Mavie feliz e aparece a comemoração "AMINU!". Chute para fora acerta a bola na Mavie (de leve) e a felicidade dela cai. Cada vez que a felicidade da Mavie enche, uma nova skin do batedor é liberada, o goleiro fica mais gordo e acertar o chute fica mais difícil. Liberando as 8 skins, o jogo é completado.

# Como rodar

O arquivo que deve ser executado é o **`jogo.py`**.

```
pip3 install pygame-ce      (ou: pip3 install pygame)
python3 jogo.py
```

Opcional: copie `PressStart2P.ttf` de `referencia/assets/font/` (do handout) para `assets/font/` para usar a fonte arcade. Sem ela, o jogo usa a fonte padrão do pygame.


# Arquivos 
| Arquivo | O que faz |
|---|---|
| `jogo.py` | Inicializa o pygame, carrega assets e dados, máquina de estados das telas (INIT, GAME, GOL, MAVIE, QUIT) e finalização |
| `config.py` | Constantes: tamanho da janela, FPS, posição do gol, estados, frases |
| `assets.py` | Cria as imagens a partir da pixel art, os fundos, as fontes e os sons (dicionário `assets`) |
| `pixel_art.py` | Desenhos como **listas de strings** + dicionário `PALETA` (letra → cor) |
| `skins.py` | Lista de dicionários com nome, cabelo e cores de cada skin |
| `tela_skin.py` | Tela "NOVA SKIN LIBERADA" |
| `tela_reiniciar.py` | Confirmação para reiniciar o jogo (botões SIM/NÃO) |
| `tela_final.py` | Tela de jogo completo (cena final) |
| `sprites.py` | Classes `Mira`, `Goleiro`, `Batedor`, `Bola`, `Estrela`, `Confete` (todas herdam de `pygame.sprite.Sprite`) |
| `tela_inicial.py` | Escolha do personagem, lista de skins (trancadas aparecem como silhueta com ?), placar e índice de felicidade |
| `tela_jogo.py` | Cobrança: game loop com a sua própria máquina de estados (MIRANDO_LADO → MIRANDO_ALTURA → CORRENDO → CHUTANDO → FIM) |
| `tela_gol.py` | Comemoração "AMINU!" com confetes |
| `tela_mavie.py` | Animação da bola acertando a Mavie + frases que mudam a cada erro |
| `dados.py` | Lê e salva felicidade, placar, skins liberadas e skin escolhida em `dados_mavie.txt`; `verifica_nova_skin` libera a próxima |
| `utils.py` | `desenha_texto` e o painel de felicidade |
| `assets/snd/` | Sons do jogo. O `aminu.wav` (tela "AMINU!") e o `bolada_mavie.wav` (tela da Mavie) foram tirados de vídeos da equipe |
| `extras/gerar_sons.py` | Script que gerou os outros sons 8-bit (não precisa rodar) |



# Sprites e áudios

- Os sprites são pixel art escrita como listas de strings em `pixel_art.py` (cada letra é uma cor do dicionário `PALETA`). As 8 skins usam o mesmo desenho com paletas diferentes (`skins.py`).
- Os áudios `aminu.wav` e `bolada_mavie.wav` foram gravados pelo grupo em vídeo e o áudio foi extraído. Os outros efeitos 8-bit foram gerados por `extras/gerar_sons.py`.

# Vídeo demonstração do jogo
https://youtu.be/oTrqgrS3pR4 



