```python

import numpy as np
import time
import math 

n     =10             # preparação
repete=1000

x=np.zeros(n)
y=np.zeros(n)

for i in range(n):
    x[i]=math.sin( i )
    y[i]=math.cos( i )


inicio=time.time()         # início da marcação de tempo
# <------------------------
for k in range(repete):    # repetições
    S=0.0
    for j in range(n):
        S=S+x[j]*y[j]
# <--------------------------
fim=time.time()            # fim da marcação de tempo
tt =fim-inicio

#print(f' Tempo {tt:3.7f} s')
tloop= tt/repete
custo= 2*n
tflop= (tloop/custo)
GFLOP= 1.0/tflop
print(f' t={tt:3.7f} s, tloop={tloop} s  tflop={tflop} s   FLOPS={GFLOP}')


x=[]
y=[]
for i in range(n):
    x.append( math.sin( i ))
    y.append( math.cos( i ))

    
a = 0.0000023423423

inicio=time.time()
for k in range(repete):
    for j in range(n):
        y[j]=y[j]+a*x[j]

fim=time.time()    
tt =fim-inicio
#print(f'tempo {tt:3.7f} s')
tloop= tt/repete
tflop= (tloop/(2*n))*10**9
GFLOP= 1.0/tflop
print(f' t={tt:3.7f} s, tloop={tloop:3.9f} s  tflop={tflop:3.5f} ns  GFLOP={GFLOP:3.5f}')


```