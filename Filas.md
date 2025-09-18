Implementação de Fila com array  
  
  
init  
add  
remove  
find  
len  
  
O que acontece quando a fila está cheia?  


# Deque  
Uma fila com entrada e saída na frente e atrás.  
  
Implementar um deque:  
Deque()  
addfront()  
addback()  
removefront()  
removeback()  
len  
find()  




```python
def add(self,x):
    self.F[self.fim]=x
    self.fim=self.fim+1


# versão circular com teste de estouro
def add(self,x):
    if self.len==self.n:
        print("  :( =>   passou do limite")
    else:
        self.F[self.fim]=x
        self.fim=(self.fim+1)%self.n
        self.len+=1


```



  
[https://panda.ime.usp.br/panda/static/pythonds_pt/03-EDBasicos/21-ListaImplementacao.html](https://panda.ime.usp.br/panda/static/pythonds_pt/03-EDBasicos/21-ListaImplementacao.html)  

