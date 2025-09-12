
# Pesquisa Linear

https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheSequentialSearch.html?mode=browsing


```python
def busca(x,L):
    n=len(L)
    for k in range(n):
        if L[k]==x:
            #print(f'Achei {x} em {k})
            return k      
    return 'não achei'


n=50
P=Pilha(n)
for i in range(40):
    x=random.randint(1,100)
    P.add(x)

x = 33
k = busca(x,P)
```

# Complexidade

## em Pilha não ordenada  

Caso           melhor   pior  Caso  
                caso    caso  médio  
------------------------------------
 item presente    1       n     n/2  
 item ausente     n       n      n  
------------------------------------

Como ficaria o algoritmo se a pilha já estivesse ordenada?

## em Pilha Ordenada

Caso           melhor   pior  Caso  
                caso    caso  médio  
------------------------------------
 item presente    1       n     n/2  
 item ausente     n       n     n/2  
------------------------------------





# Pesquisa Binária

https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheBinarySearch.html?mode=browsing


Qual a condição em `x` para que se use a busca binária?

Como implementar:  Loop x recursivo

```python
def busca_binaria(x,L):
    achou=False
    n=len(L)
    i = 1
    f = n
    while ~achou and i<f:
        m=int( i+f )/2
        if L.get(m)==x:
            achou=True
            return m
        if L.get(m)<x:
            fim=m-1
        else
            ini=m+1
    return 'não achei'

```

## Complexidade

Caso           melhor   pior      Caso  
                caso    caso      médio  
------------------------------------------
 item presente    1      log(n)  log(n)/2  
 item ausente     n      log(n)  log(n)
------------------------------------


# [[Hashing Table]]


