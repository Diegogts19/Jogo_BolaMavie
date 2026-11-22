"""Classes dos sprites do jogo (igual ao sprites.py do handout)."""
import math
import random

import pygame

from config import WIDTH, HEIGHT, GOL_ESQ, GOL_DIR, GOL_TOPO, GOL_CHAO, MARCA_PENALTI


class Mira(pygame.sprite.Sprite):
    """Mira que vai e volta. 1º ESPAÇO trava o lado, 2º ESPAÇO trava a altura."""
    def __init__(self, img):
        """Começa no meio do gol, andando para a direita."""
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, (GOL_TOPO + GOL_CHAO) / 2)
        self.speedx = 7
        self.speedy = 0
        self.limite_esq = GOL_ESQ - 70
        self.limite_dir = GOL_DIR + 70
        self.limite_cima = GOL_TOPO - 70
        self.limite_baixo = GOL_CHAO - 20

    def update(self):
        """Move a mira e inverte a velocidade quando passa do limite."""
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.centerx > self.limite_dir or self.rect.centerx < self.limite_esq:
            self.speedx = -self.speedx
        if self.rect.centery > self.limite_baixo or self.rect.centery < self.limite_cima:
            self.speedy = -self.speedy

    def trava_lado(self):
        """Para o movimento lateral e começa a mexer na altura."""
        self.speedx = 0
        self.speedy = 5

    def trava_altura(self):
        """Para a mira de vez: o alvo do chute está escolhido."""
        self.speedy = 0


class Goleiro(pygame.sprite.Sprite):
    """Goleiro: fica parado até o chute e então pula para um lugar.

    A cada skin liberada (nível) ele fica bem mais gordo e ocupa mais o gol.
    Quem decide se ele defende é a QUALIDADE do chute (ver tela_jogo.py).
    """
    def __init__(self, img, nivel):
        """Cria o goleiro parado no meio do gol, mais largo a cada nível."""
        pygame.sprite.Sprite.__init__(self)
        largura = int(img.get_width() * (1 + 0.20 * nivel))
        altura = int(img.get_height() * (1 + 0.05 * nivel))
        self.imagem_em_pe = pygame.transform.scale(img, (largura, altura))
        self.image = self.imagem_em_pe
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = GOL_CHAO + 8
        self.mask = pygame.mask.from_surface(self.image)
        self.pulando = False
        self.destino = self.rect.center
        self.espera = 0

    def pula(self, alvo, vai_na_bola):
        """Escolhe para onde pular.

        vai_na_bola = True  -> chute fraco: ele vai exatamente onde a bola vai.
        vai_na_bola = False -> chute bom: ele cai para o lado errado.
        """
        if vai_na_bola:
            self.destino = alvo
        elif alvo[0] >= WIDTH / 2:
            self.destino = (GOL_ESQ + 30, GOL_CHAO - 60)
        else:
            self.destino = (GOL_DIR - 30, GOL_CHAO - 60)
        diferenca = self.destino[0] - self.rect.centerx
        direcao = 0
        if diferenca > 30:
            direcao = 1
        elif diferenca < -30:
            direcao = -1
        if direcao != 0:
            centro = self.rect.center
            self.image = pygame.transform.rotate(self.imagem_em_pe, -65 * direcao)
            self.rect = self.image.get_rect()
            self.rect.center = centro
            self.mask = pygame.mask.from_surface(self.image)
        self.pulando = True
        self.espera = 5

    def update(self):
        """Antes do chute fica parado; depois anda um pouco por frame até o destino."""
        if not self.pulando:
            return
        if self.espera > 0:
            self.espera -= 1
            return
        dx = self.destino[0] - self.rect.centerx
        dy = self.destino[1] - self.rect.centery
        self.rect.centerx += max(-12, min(12, dx))
        self.rect.centery += max(-8, min(8, dy))
        if self.rect.bottom > GOL_CHAO + 10:
            self.rect.bottom = GOL_CHAO + 10


class Batedor(pygame.sprite.Sprite):
    """Jogador de costas que corre até a bola."""
    def __init__(self, img):
        """Posiciona o batedor de costas, à esquerda da bola."""
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.right = MARCA_PENALTI[0] - 40
        self.rect.bottom = HEIGHT + 30
        self.correndo = False
        self.chegou = False
        self.frames = 0

    def correr(self):
        """Começa a corrida até a bola."""
        self.correndo = True

    def update(self):
        """Anda na diagonal até a bola por 12 frames."""
        if self.correndo and not self.chegou:
            self.rect.x += 3
            self.rect.y -= 2
            self.frames += 1
            if self.frames >= 12:
                self.chegou = True


class Bola(pygame.sprite.Sprite):
    """Bola que vai da marca do pênalti até o alvo, diminuindo de tamanho."""
    def __init__(self, img):
        """Coloca a bola parada na marca do pênalti."""
        pygame.sprite.Sprite.__init__(self)
        self.imagem_original = img
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = MARCA_PENALTI
        self.mask = pygame.mask.from_surface(self.image)
        self.inicio = MARCA_PENALTI
        self.alvo = MARCA_PENALTI
        self.frame = 0
        self.frames_total = 36
        self.chutada = False
        self.chegou = False
        self.defendida = False
        self.speedx = 0
        self.speedy = 0

    def chuta(self, alvo):
        """Guarda o alvo e começa o movimento."""
        self.alvo = alvo
        self.chutada = True

    def profundidade(self):
        """0 = na marca do pênalti, 1 = chegou no gol."""
        return self.frame / self.frames_total

    def rebate(self):
        """O goleiro defendeu: a bola volta quicando."""
        self.defendida = True
        self.speedx = random.randint(-6, 6)
        self.speedy = 6

    def update(self):
        """Avança um frame: posição com curva, tamanho menor e nova máscara."""
        if self.defendida:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            return
        if not self.chutada or self.chegou:
            return
        self.frame += 1
        t = self.profundidade()
        x = self.inicio[0] + (self.alvo[0] - self.inicio[0]) * t
        y = self.inicio[1] + (self.alvo[1] - self.inicio[1]) * t - math.sin(math.pi * t) * 50
        escala = 1 - 0.45 * t
        largura = int(self.imagem_original.get_width() * escala)
        self.image = pygame.transform.scale(self.imagem_original, (largura, largura))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        if self.frame >= self.frames_total:
            self.chegou = True


class Estrela(pygame.sprite.Sprite):
    """Estrelinhas girando em volta da cabeça da Mavie."""
    def __init__(self, img, centro, angulo):
        """Guarda o centro da órbita e o ângulo inicial."""
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.centro = centro
        self.angulo = angulo
        self.update()

    def update(self):
        """Gira um pouco em volta do centro (elipse com cos e sin)."""
        self.angulo += 0.12
        x = self.centro[0] + math.cos(self.angulo) * 170
        y = self.centro[1] + math.sin(self.angulo) * 40
        self.rect.center = (x, y)


class Confete(pygame.sprite.Sprite):
    """Quadradinho colorido que cai na comemoração."""
    def __init__(self):
        """Cria o confete com cor sorteada em algum ponto da tela."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(random.choice([(250, 214, 20), (0, 150, 70), (255, 255, 255), (30, 60, 170)]))
        self.rect = self.image.get_rect()
        self.sorteia()
        self.rect.y = random.randint(0, HEIGHT)

    def sorteia(self):
        """Sorteia nova posição acima da tela e nova velocidade."""
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(-100, -10)
        self.speedx = random.randint(-1, 1)
        self.speedy = random.randint(2, 5)

    def update(self):
        """Cai; quando sai por baixo, volta para cima (como o meteoro do handout)."""
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.sorteia()


class BarraQualidade:
    """Barra do vermelho (esquerda) ao verde (direita) com uma barrinha que vai e volta.

    Quando o jogador aperta ESPAÇO, a barrinha para. A posição dela vira a
    qualidade do chute: 0.0 (vermelho) até 1.0 (verde).
    """
    def __init__(self, x, y, velocidade, minimo):
        """Monta a barra e desenha o degradê uma vez só."""
        self.rect = pygame.Rect(x, y, 300, 24)
        self.velocidade = velocidade
        self.minimo = minimo
        self.posicao = 0
        self.parada = False
        self.imagem = pygame.Surface((self.rect.width, self.rect.height))
        for bloco in range(0, self.rect.width, 10):
            t = bloco / self.rect.width
            if t < 0.5:
                cor = (230, int(460 * t), 30)
            else:
                cor = (int(230 * (1 - t) * 2), 210, 30)
            pygame.draw.rect(self.imagem, cor, (bloco, 0, 10, self.rect.height))

    def update(self):
        """Move a barrinha e inverte nas pontas."""
        if self.parada:
            return
        self.posicao += self.velocidade
        if self.posicao >= self.rect.width or self.posicao <= 0:
            self.velocidade = -self.velocidade
            self.posicao = max(0, min(self.rect.width, self.posicao))

    def para(self):
        """Congela a barrinha onde ela está."""
        self.parada = True

    def qualidade(self):
        """Qualidade do chute de 0.0 (vermelho) a 1.0 (verde)."""
        return self.posicao / self.rect.width

    def draw(self, window):
        """Desenha a barra, o risco da qualidade mínima e a barrinha."""
        moldura = self.rect.inflate(8, 8)
        pygame.draw.rect(window, (0, 0, 0), moldura)
        window.blit(self.imagem, self.rect)
        x_minimo = self.rect.x + int(self.minimo * self.rect.width)
        pygame.draw.rect(window, (255, 255, 255), (x_minimo - 2, self.rect.y - 8, 4, self.rect.height + 16))
        x = self.rect.x + int(self.posicao)
        pygame.draw.rect(window, (0, 0, 0), (x - 5, self.rect.y - 12, 10, self.rect.height + 24))
        pygame.draw.rect(window, (255, 255, 255), (x - 3, self.rect.y - 10, 6, self.rect.height + 20))



