


```python
import pygame

# --- Configurações da matriz ---
N = 10            # Número de quadrados por linha/coluna
TAM = 50          # Tamanho de cada quadrado (pixels)
largura = N * TAM
altura  = N * TAM

# --- Cores ---
cor_fundo   = (200, 200, 200)
cor_grid    = (50, 50, 50)
cor_jogador = (255, 0, 0)

def desenha_fundo(TAM):
    # Preenche o fundo
    tela.fill(cor_fundo)

    # Desenha a grade
    for i in range(N):
        for j in range(N):
            pygame.draw.rect(tela, cor_grid, (j* TAM, i * TAM, TAM, TAM), 1)
    

# --- Posição inicial do jogador ---
linha  = 0
coluna = 0

# Inicializa o Pygame
pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Mover quadradinho com ASDW")
relogio = pygame.time.Clock()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w :
                linha -= 1
            elif evento.key == pygame.K_s :
                linha += 1
            elif evento.key == pygame.K_a :
                coluna -= 1
            elif evento.key == pygame.K_d :
                coluna += 1

    desenha_fundo(TAM)

    # Desenha o jogador
    rect_jogador = pygame.Rect(coluna * TAM, linha * TAM, TAM, TAM)
    pygame.draw.rect(tela, cor_jogador, rect_jogador)

    # Atualiza a tela
    pygame.display.flip()
    relogio.tick(30)

pygame.quit()
```


