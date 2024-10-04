
Definindo função, valores de entrada e saída
```python
k=0
def mexe(x):
    y=x          # xi! altera o valor de x.
    #y=list(x)   # ou  y=x.copy() para fazer uma nova cópia
    y[2]=7
    k=k+1        # hmmm.... 
    return y


m=[1, 2, 3, 4, 5]

print('== entrada')
print(m)
z=mexe(m)
print('== saida')
print(m)
#print(y)
print(z)
```
