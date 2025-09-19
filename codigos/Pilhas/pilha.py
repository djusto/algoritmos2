"""
Classe pilha como vetor
"""
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

    def get(self,i):
        return self.P[i]

    def set(self,i,x):
        self.P[i]=x

    def __str__(self):
        res=f'Pilha= {self.P}'
        return res

    def __getitem__(self, chave):  # redefine a leitura com P[] 
        return self.P(chave)

    def __setitem__(self, chave, valor):  # Redefine a escrita usando []
        self.P[chave] = valor
    
   

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


class Node:
   def __init__(self,i,r):
       self.i = i
       self.r = r 
   
   def __str__(self):
       res=f'[{self.i},{self.r}]'
       return res
   
   def area(self):
       A=self.i * self.r
       return A
    
no=Node(3, 3.33)

#print( no )
#print( no.area() )


x=[1,2,3,4,5]

#print(x[4])

