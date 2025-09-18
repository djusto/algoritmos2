import pygame
from numpy import zeros

class Fila:
    def __init__(self,n):
        self.ini=0
        self.fim=0
        self.len=0     # comprimento
        self.n  =n
        self.x=zeros(self.n, dtype=int)
        self.y=zeros(self.n, dtype=int)

    def add(self,x,y):
        self.x[self.fim]=x
        self.y[self.fim]=y
        self.fim=self.fim+1
        self.len+=1

    def remove(self):
        x=self.x[self.ini]
        y=self.y[self.ini]
        
        self.x[self.ini]=0
        self.y[self.ini]=0
        self.ini=self.ini+1
        self.len=self.len-1
        return x,y

    def __str__(self):
        res=f'Fila = {self.x},{self.y}'
        return res

    def __getitem__(self, chave):  # redefine a leitura com S[] 
        return self.x[chave],self.y[chave]

    def __setitem__(self, chave, valor):  # Redefine a escrita usando []
        #self.x[chave] = valor
        pass
    
    def desenha(self):
        c=self.ini
        for i in range(self.len):
            x=self.x[c]
            y=self.y[c]
            desenha_rect(x,y,cor_jogador)
            c=(c+1)%self.n
        

def desenha_rect(x,y,cor):
    peca = pygame.Rect(x*TAM+2, y*TAM+2, TAM-4, TAM-4)
    pygame.draw.rect(tela, cor, peca)

def desenha_fundo(TAM):
    tela.fill(cor_fundo)       # Preenche o fundo

    for i in range(N):         # Desenha a grade
        for j in range(N):
            pygame.draw.rect(tela, cor_grid, (j* TAM, i * TAM, TAM+1, TAM+1), 1)

    

# Configurações da matriz
N   = 10          # Número de quadrados por linha/coluna
TAM = 20          # Tamanho de cada quadrado (pixels)
largura = N * TAM
altura  = N * TAM

cor_fundo   = (200, 200, 200)  #cores
cor_grid    = (50, 50, 50)
cor_jogador = (255, 0, 0)
verde       = (0,150,0)


    
linha  = 5        # posição inicial do jogado
coluna = 5
cobra  = Fila( 30 )

cobra.add( coluna,linha)
coluna +=1
cobra.add( coluna,linha)
coluna +=1
cobra.add( coluna,linha)
coluna +=1
cobra.add( coluna,linha)

 
pygame.init()               # inicia o pygame
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    keys=pygame.key.get_pressed()  # le teclas pressionadas
    
    if keys[pygame.K_w]:
        linha -=1
        cobra.add(coluna,linha)
    if keys[pygame.K_s]:
        linha +=1
    if keys[pygame.K_a]:
        coluna -=1
    if keys[pygame.K_d]:
        coluna +=1
        
    desenha_fundo(TAM)

    cobra.desenha()
    desenha_rect(coluna,linha,verde)

    
    pygame.display.flip()   # Atualiza a tela
    relogio.tick(15)        # velocidade do jogo

pygame.quit()