# Exercício:
Criar uma pilha usando array com operações básicas (Quais são elas?)

Utilizando seed=123 (Quais pacotes?), crie um programa que adicione 4 elementos aleatórios entre 1 e 100,  retire 2 elementos e adicione mais 4 elementos aleatórios.
## passo1

```python
import numpy as np
import random

def add(x):
    pass
def remove():
    pass

n=5                      # tamanho inicial
P=np.zeros(n, dtype=int)

print(P)
random.seed(123)

```

Completar as funções, quais operações extra?

## passo2

```python
def add(x):
    global k
    P[k]=x
    k=k+1
    

def remove():
    global k
    k=k-1
    P[k]=0
    pass

def init(n):
    global k
    k=0
    P=np.zeros(n, dtype=int)
    return P

def get(i):
    pass

def set(i,x):
    pass

n=5                      # tamanho inicial
k=0
P=np.zeros(n, dtype=int)

print(P)
random.seed(123)

for i in range(4):
    x=random.randint(1,100)
    add(x)
    print(P)

for i in range(2):
    remove()
    print(P)

for i in range(4):
    x=random.randint(1,100)
    add(x)
    print(P)
```

Podemos criar essa Fila como uma classe.  
Ver [Orientação a Objeto](Orientação%20a%20Objeto.md)


# Classe Pilha

Quase tudo pronto. Definir a classe e salvar num arquivo pilha.py

```python
from numpy import zeros

class Pilha:
    def __init__(self,n):
        self.k=0
        self.n=n
        self.P=zeros(self.n, dtype=int)

    def add(self,x):
        if self.k<self.n:
            self.P[self.k]=x
            self.k=self.k+1
        else:
            print("         :( passou do limite  ")
    

    def remove(self):
        if self.k>0:
            self.k=self.k-1
            self.P[self.k]=0
        else:
            print("         :( tá vazio  ")

    def __str__(self):
        res=f'Pilha= {self.P}'
        return res

    def get(self,i):
        return self.P[i]

    def set(self,i,x):
        self.P[i]=x

    # melhor é usar os métodos __getitem__ e __setitem__
    def __getitem__(self, chave):  # redefine a leitura com P[] 
        return self.P[chave]

    def __setitem__(self, chave, valor):  # Redefine a escrita usando []
        self.P[chave] = valor



```

Exemplo de uso:

```python
 
import Pilha
import random
    
n=5                      # tamanho inicial
P=Pilha(n)

print(P)
random.seed(123)

for i in range(4):
    x=random.randint(1,100)
    P.add(x)
    print(P)

print( P.get(2) )
P.set(2,99)

for i in range(6):
    P.remove()
    print(P)

for i in range(4):
    x=random.randint(1,100)
    P.add(x)
    print(P)
```



Podemos redefinir o set e o get para usar os colchetes colocando dentro da classe. Isso é um exemplo de ==operator overload==

```python
    def __getitem__(self, chave):  # redefine a leitura com P[] 
        return self.P(chave)

    def __setitem__(self, chave, valor):  # Redefine a escrita usando []
        self.P[chave] = valor

# exemplo
print(P[3]) 
P[3] = 98
 
```

