Exemplo para mostrar distribuição na memória

```python
import numpy as np


x=[12,23,34]
z=[-1,-2]

print(x)
x=x+z
z.append(-4)
z.append(-5)
z.append(-6)
x.append(88)
x.append(99)
x.append(87)

membase=0 #id(x[0])
membase=id(x[0])
print("Onde está x?")
for i in range( len(x)):
    mem=hex(id(x[i])- membase)
    print( f' x[{i}]={x[i]} está em {mem}' )

print("Onde está z")
for i in range( len(z)):
    mem=hex(id(z[i])- membase)
    print( f' z[{i}]={z[i]} está em {mem}' )

print("==========")
#y=np.array( list(x) )
y=np.zeros(10)
y=np.array( [0]*10)

print(y)
print( hex(id(y) ))


print("Forma de y:   ", y.shape)
print("Strides de y: ", y.strides)

memy = y.__array_interface__['data'][0] 
for i in range(10):
    mem=hex(id(y[i]))   # nao funciona diretamente
    mem = hex( memy + y.itemsize*i )
    print( f' y[{i}] está em {mem} ')

print("---")
for i in range(10):
    y[i]=2.3123
    mem = hex( memy + y.itemsize*i )
    print( f' y[{i}] está em {mem} ')
```