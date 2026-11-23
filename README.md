# Pênalti da Mavie

Jogo de pênalti em pixel art feito com pygame, seguindo o handout de PyGame de Design de Software.

## Autores

- Alexandre Trancoso
- Leonardo Riglioni
- Diego Siqueira

## Descrição

Você cobra pênaltis escolhendo o lado, a altura e a qualidade do chute. Gol deixa a Mavie feliz e aparece a comemoração "AMINU!". Chute para fora acerta a bola na Mavie (de leve) e a felicidade dela cai. Cada vez que a felicidade da Mavie enche, uma nova skin do batedor é liberada, o goleiro fica mais gordo e acertar o chute fica mais difícil. Liberando as 8 skins, o jogo é completado.

## Como rodar

O arquivo que deve ser executado é o **`jogo.py`**.

```
pip3 install pygame-ce      (ou: pip3 install pygame)
python3 jogo.py
```

Opcional: copie `PressStart2P.ttf` de `referencia/assets/font/` (do handout) para `assets/font/` para usar a fonte arcade. Sem ela, o jogo usa a fonte padrão do pygame.

## Como jogar

- **ESPAÇO** na tela inicial: vai para a cobrança.
- **1º ESPAÇO**: trava o lado da mira. **2º ESPAÇO**: trava a altura. **3º ESPAÇO**: para a barrinha da qualidade do chute (vermelho = fraco, verde = forte) e chuta.
- Se a barrinha parar depois do **risco branco**, o chute é bom e o goleiro cai para o lado errado. Antes do risco, o chute é fraco e ele defende.
- Se a mira estiver fora do gol, a bola vai para fora e acerta a Mavie (perde o mesmo tanto que um gol dá).
- Se a mira estiver em cima da trave ou do travessão: aparece "TRAVE!" e não perde nada.
- Depois de cada chute o jogo volta direto para o próximo pênalti. **ESC** abre o menu (escolha de skin).
- Gol: aparece o nosso craque com "AMINU!" e a felicidade sobe.
- O goleiro fica parado até o chute. Se ele pegar, nada muda.
- Na tela inicial, **← →** trocam o personagem (só entre os liberados).
- Quando a felicidade da Mavie chega a **100%**, a próxima skin é liberada: aparece a tela "NOVA SKIN LIBERADA" e a felicidade volta para 50%.
- Gols seguidos para liberar cada skin: 1, 1, 2, 2, 3, 3 e 4 (`GOLS_POR_SKIN` no `config.py`). A barrinha começa com 4 px por frame e acelera 1,5 a cada nível; o risco branco começa em 35% e sobe 7% por nível.
- A cada skin liberada o goleiro fica mais gordo (+20% de largura), a barrinha fica mais rápida e o risco branco anda para o verde (precisa de chute melhor).
- Liberando a última skin, o jogo é completado e aparece a cena final.
- Ordem das skins: Kings League (já liberada) → Al Hilal → Santos 2026 → Copa 2022 → PSG → Barcelona 2015 → Copa 2014 → Santos 2011.
- **F** liga/desliga a tela cheia (em qualquer tela).
- Botão **REINICIAR** (canto inferior esquerdo, no menu e no jogo) ou tecla **R**: pergunta se quer apagar todo o progresso (**S** = sim, **N** = não). **ESC** no menu sai.

## Arquivos (mesma divisão do jogo_v21/v22)

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

## Design e processo do grupo

### Divisão do trabalho

| Integrante | Parte principal |
|---|---|
| Alexandre Trancoso | Estrutura do jogo (config, máquina de estados), sprites da cobrança, dados salvos em arquivo, liberação de skins, tela final |
| Leonardo Riglioni | Pixel art e assets (desenhos em listas de strings e paletas das skins), sons, botões e tela de reiniciar |
| Diego Siqueira | Telas do jogo (inicial, cobrança, Mavie, jogo completo), seleção de personagem, placar e este README |

### Sprites e áudios

- Os sprites são pixel art escrita como listas de strings em `pixel_art.py` (cada letra é uma cor do dicionário `PALETA`). As 8 skins usam o mesmo desenho com paletas diferentes (`skins.py`).
- Os áudios `aminu.wav` e `bolada_mavie.wav` foram gravados pelo grupo em vídeo e o áudio foi extraído. Os outros efeitos 8-bit foram gerados por `extras/gerar_sons.py`.

### Rascunhos

<!-- Coloquem aqui fotos ou prints dos rascunhos do jogo (papel, quadro, conversas de ideias).
     Exemplo: salvem as imagens na pasta docs/ e escrevam ![Rascunho da tela inicial](docs/rascunho1.jpg) -->

## Conteúdo da disciplina usado (para explicar na prova)

- **Funções**: cada tela é uma função que devolve o próximo estado.
- **if / while**: game loop `while True` com `clock.tick(FPS)`; máquina de estados com `if/elif`.
- **Listas**: a pixel art é uma lista de strings; as frases da Mavie ficam em uma lista.
- **for**: `cria_imagem` percorre linhas e colunas pintando cada pixel; os confetes são criados com `for`.
- **Dicionários**: `PALETA`, `assets`, `dados` (felicidade e placar), expressões da Mavie.
- **Strings e fatiamento**: `MAVIE_BASE[:14] + expressão + MAVIE_BASE[26:]` monta o rosto; `linha.strip().split('=')` lê o arquivo.
- **Arquivos**: `dados.py` salva com `open(..., 'w')` e lê com `open(..., 'r')` (com `try/except` na primeira vez).
- **pygame**: `Sprite`, `Group`, `update()`/`draw()`, colisão por máscara (`collide_mask`, como no jogo_v19), animação por tempo com `get_ticks()` (como a `Explosion` do jogo_v15), sons com `mixer`, texto com `font.render` e `blit`.
- **Skins = mesma pixel art, paleta diferente**: `paleta_da_skin` copia o dicionário `PALETA` e troca as cores das letras "coringa" (camisa `Y`, listra `X`, faixa `Q`, calção `Z`, meião `U`, cabelo `H`/`J`, boné `E`, barba `b`, bandagem `c`). A silhueta das trancadas é uma paleta em que toda letra vira preto.
- **Soma de listas**: `BATEDOR_CABELOS[estilo] + BATEDOR_CORPO` monta o batedor de costas.
- **Resto da divisão**: `FRASES_MAVIE[(erros - 1) % len(FRASES_MAVIE)]` faz as frases darem a volta; o mesmo truque faz as setas darem a volta na lista de skins.
- **Dificuldade**: `ganho_por_gol` em `dados.py` faz a conta `(100 - 50) / gols necessários` com `math.ceil`. O goleiro (`Goleiro` em `sprites.py`) estica a imagem com `transform.scale` conforme o nível. A classe `BarraQualidade` tem uma posição que anda `velocidade` pixels por frame e inverte o sinal nas pontas (igual à mira e ao meteoro do handout); `qualidade()` devolve `posicao / largura`. Em `tela_jogo.py`, `chute_bom = qualidade >= minimo` decide se o goleiro vai na bola ou cai para o lado errado. `velocidade_da_barra` e `qualidade_minima` (em `dados.py`) aumentam com o nível; os valores ficam no `config.py`.
- **Trave**: `bola_na_trave` em `tela_jogo.py` compara as coordenadas do alvo com as das traves usando `and`/`or`.
- **Cena final**: é a mesma técnica da pixel art, desenhada com a paleta da skin Copa 2014.
- **Botão com mouse**: `clicou_no_botao` (em `utils.py`) verifica o evento `pygame.MOUSEBUTTONDOWN` e usa `Rect.collidepoint(event.pos)` para saber se o clique foi dentro do botão; `desenha_botao` usa `pygame.mouse.get_pos()` para pintar o botão de amarelo quando o mouse está em cima.


