
import math
import random

import pygame

from config import WIDTH, HEIGHT, GOL_ESQ, GOL_DIR, GOL_TOPO, GOL_CHAO, MARCA_PENALTI


class Mira(pygame.sprite.Sprite):
    
    def __init__(self, img):
       
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
       
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.centerx > self.limite_dir or self.rect.centerx < self.limite_esq:
            self.speedx = -self.speedx
        if self.rect.centery > self.limite_baixo or self.rect.centery < self.limite_cima:
            self.speedy = -self.speedy

    def trava_lado(self):
       
        self.speedx = 0
        self.speedy = 5

    def trava_altura(self):
        
        self.speedy = 0


class Goleiro(pygame.sprite.Sprite):
   
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
   
    def __init__(self, img):
       
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.right = MARCA_PENALTI[0] - 40
        self.rect.bottom = HEIGHT + 30
        self.correndo = False
        self.chegou = False
        self.frames = 0

    def correr(self):
        
        self.correndo = True

    def update(self):
      
        if self.correndo and not self.chegou:
            self.rect.x += 3
            self.rect.y -= 2
            self.frames += 1
            if self.frames >= 12:
                self.chegou = True


class Bola(pygame.sprite.Sprite):
    
    def __init__(self, img):
       
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
        
        self.alvo = alvo
        self.chutada = True

    def profundidade(self):
        
        return self.frame / self.frames_total

    def rebate(self):
       
        self.defendida = True
        self.speedx = random.randint(-6, 6)
        self.speedy = 6

    def update(self):
       
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


class BarraQualidade:
    
    def __init__(self, x, y, velocidade, minimo):
       
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
       
        if self.parada:
            return
        self.posicao += self.velocidade
        if self.posicao >= self.rect.width or self.posicao <= 0:
            self.velocidade = -self.velocidade
            self.posicao = max(0, min(self.rect.width, self.posicao))

    def para(self):
       
        self.parada = True

    def qualidade(self):
        
        return self.posicao / self.rect.width

    def draw(self, window):
      
        moldura = self.rect.inflate(8, 8)
        pygame.draw.rect(window, (0, 0, 0), moldura)
        window.blit(self.imagem, self.rect)
        x_minimo = self.rect.x + int(self.minimo * self.rect.width)
        pygame.draw.rect(window, (255, 255, 255), (x_minimo - 2, self.rect.y - 8, 4, self.rect.height + 16))
        x = self.rect.x + int(self.posicao)
        pygame.draw.rect(window, (0, 0, 0), (x - 5, self.rect.y - 12, 10, self.rect.height + 24))
        pygame.draw.rect(window, (255, 255, 255), (x - 3, self.rect.y - 10, 6, self.rect.height + 20))
