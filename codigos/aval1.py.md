Tabelas de dados de alguns alunos (os primeiros que enviaram) e os testes do professor.

```python
import matplotlib.pyplot as plt
import math

N=[100000, 200000,400000,800000,1600000, 3200000]

def llog(L):
    r=[]
    for x in L:
        r.append(math.log10(x)) 
        #r.append(x) 
    return r


class Aval:
   def __init__(self,proc,ex1,ex2,N):
       self.proc = proc
       self.ex1  = ex1
       self.ex2  = ex2
       if isinstance(N,list):
           self.N = N
       else:
           self.N = [N*(2 ** i) for i in range( len(ex1))]

   def plot(self):
       plt.plot( self.N,self.ex1,'*-')
       plt.plot( self.N,self.ex2,'*-')

   def logplot(self):
       plt.plot( llog(self.N),llog(self.ex1),'.-',label=self.proc)
       #if( len(self.ex2)>0 ):
       #    plt.plot( llog(self.N),llog(self.ex2),'*-',label=self.proc)
       

L=[]

A = Aval(  'i38100 3.6', [0.15622, 0.31246, 0.64044, 1.29659, 2.54627, 5.39374],[0.18748, 0.35926, 0.76544, 1.57428, 3.03050, 5.93832],N)
L.append(A)

A = Aval(  'i38100lista 3.6', [0.10935, 0.21873, 0.43739, 0.91617, 1.83180, 3.62630],[],N)
L.append(A)


A = Aval(  'R6 5600 4.4', [0.115, 0.221, 0.445, 0.897, 1.774, 3.550],[],N)
L.append(A)

A = Aval(  'R5 5500U 2.1', [0.01594066619873047, 0.029628753662109375, 0.04772520065307617, 0.1145467758178711, 0.21736884117126465, 0.45238423347473145, 0.9789159297943115, 1.729532241821289],[0.01743340492248535, 0.03860950469970703, 0.0841360092163086, 0.12053060531616211, 0.2526237964630127, 0.5320589542388916, 1.0820362567901611, 2.0884604454040527],10000)
L.append(A)

A = Aval( 'ColabXeon 2.2',[0.2283, 0.4497,0.8653, 1.7366, 3.5041, 8.9252],[ 0.2210,0.4566,1.0224,1.7360,3.5101,8.6755],N)
L.append(A)
  

A = Aval( 'i51135 2.4',[0.18,0.37, 0.71, 1.06, 1.43,1.79],[0.21, 0.38, 0.79, 1.14, 1.56, 1.94],N)
L.append(A)
    
A = Aval( 'R53500 2.1',[0.15, 0.37, 0.62, 1.3, 2.3, 5.0],[0.15,0.29,0.57, 1.17,2.36,4.75 ],100000)
L.append(A)

A = Aval( 'Colabi5 2.4',[0.21,0.51,0.83,1.12,1.47,1.74],[ ],[100000,250000,400000,550000,700000,850000])
L.append(A)

A = Aval( 'i58350 3.6',[0.014,0.029,0.059,0.119,0.236,0.474,0.95,1.89],[ ],10000)
L.append(A)

A = Aval( 'i71165 4.7',[0.08,0.18,0.38,0.75,1.54,3.13],[0.09,0.18,0.38,0.76,1.57,3.06 ],N)
L.append(A)


#professor
A=Aval('i710700 4.6',[19.366, 38.79, 78.13, 157.205, 312.72],[21.125, 42.15, 83.89, 168.774, 336.17],10000000)
L.append(A)

A=Aval('i710700 4.6 spyder',[0.19, 0.39, 0.78, 1.58, 3.15], [0.22, 0.43, 0.87, 1.75, 3.48],100000)
L.append(A)

A=Aval('i710700 4.6 wsl',[0.07, 0.15, 0.30, 0.61, 1.23], [],100000)
L.append(A)
A=Aval('i710700 4.6 wsl',[7.72, 15.5, 30.7, 61.6, 124.3], [],10000000)
L.append(A)


A=Aval('i710700 fortran',[0.11,0.23,0.46,0.94,1.86], [0.12,0.24,0.49,0.96,2.0],10000000)
L.append(A)


#plt.plot( A[0].ex1,A[1].ex2,'*-')
for k in range(len(L)):
    L[k].logplot()
plt.legend(fontsize=7)

```


![](Pasted%20image%2020241023094702.png)