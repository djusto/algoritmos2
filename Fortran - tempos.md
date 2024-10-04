computador i7-10700
![[Pasted image 20240919010711.png]]

4.6Ghz

L1 = 8x 32K= 256KB dados
L1 = 8x 32K= 256KB instruções
L2 = 8x256K=   2MB
L3 =          16MB

![[Pasted image 20240919011731.png]]

Repetir 5 vezes pegar a média:
 

loop    :=   1.10 ns 
r=1.12  :=   1.35 ns
r=a * b :=   1.09 ns  
r=r + a :=   1.96 ns (loop+soma+atrib)
             1.96-loop => 0.86 ns
           
r=r * a :    1.96 ns
             1.96-1.10 => 0.86 ns   (+,-,* )
r=b/r   :    4.00 ns  
             4.00-loop => 2.90 ns   (/)
           
r=r * b+a:   2.82 ns
             2.82-loop => 1.72 ns/2= 0.86 ns

Em C:
r=r * b+a:   2.82-loop => 1.72 ns/2= 0.86 ns

r=r.b+r.a+a: 3.68 ns
             3.68-loop => 2.58 ns/4= 0.645 ns??
  r*(b+a)+a               2.58 ns/3= 0.86 ns

r=a+r.(b+r.(a+r)):5.44 ns
                  5.44-loop => 4.34/5= 0.868 ns  (1.15 Gflop/s)
                  5.44-1.96 => 3.45/4= 0.87  ns

Porém colocando 2 instruções no loop
r=r+a;s=s+b  1.96 ns  (mesmo tempo!)

r=a+r.(b+r.(a+r));
s=a+s.(b+s.(a+s)):5.44 ns
                  5.44-loop => 4.34/10= 0.434 ns  (2.30 Gflop/s)
                  5.44-1.96 => 3.45/8 = 0.43  ns

r=a+r.(b+r.(a+r));
s=a+s.(b+s.(a+s)):
t=a+r.(b+r.(a+r));
u=a+r.(b+r.(a+r));5.44-2.1 => 3.34/16 = 0.20 ns (4.79 Gflop/s)


Coloquei vetores e usando a diretiva para otimização -O2

```
                  flop   ns/flop   
u(4):    4.36 ns / 20 =  0.21    =>  4.5 GFLOPS
u(8):    5.46 ns / 40 =  0.13    =>  7.3 GFLOPS
u(16):   5.92 ns / 80 =  0.074   => 13.5 GFLOPS
u(32):   9.25 ns /160 =  0.057   => 17.3 GFLOPS
u(48):  13.90 ns /240 =  0.057   => 17.3 GFLOPS
u(64):  18.6  ns /320 =  0.058   => 17.2 GFLOPS
u(128): 37.8  ns /640 =  0.058   => 17.2 GFLOPS
``` 

Retirando o tempo base (loop +soma + atribuição) dos tempos acima e diminuindo uma operação no denominador:

```
r = r + a =   0.87 ns (subtraindo dos tempos acima)
                        ns/flop
u(4):    3.49 ns / 19 = 0.18    =>  5.4 GFLOPS
u(8):    4.58 ns / 39 = 0.117   =>  8.4 GFLOPS
u(16):   5.04 ns / 79 = 0.063   => 15.6 GFLOPS
u(32):   8.35 ns /159 = 0.052   => 19.0 GFLOPS
u(48):  13.05 ns /239 = 0.054   => 18.3 GFLOPS
u(64):  17.7  ns /319 = 0.055   => 18.1 GFLOPS
u(64):  36.31 ns /639 = 0.056   => 17.5 GFLOPS
``` 


No Intel Fortran Compiler
```
r = r + a =   1.97 ns (subtraindo dos tempos acima)
                        ns/flop
u(4):   22.77 ns / 20 = 1.11    =>  0.9 GFLOPS (sem O2)

u(4):    3.86 ns / 20 = 0.19   =>  5.1 GFLOPS
u(8):    4.57 ns / 40 = 0.114  =>  8.5 GFLOPS
u(16):   8.80  ns/ 80 = 0.110   => 9.0 GFLOPS

u(32):   8.35 ns /159 = 0.052   => 19.0 GFLOPS
u(48):  13.05 ns /239 = 0.054   => 18.3 GFLOPS
u(64):  17.7  ns /319 = 0.055   => 18.1 GFLOPS
u(64):  36.31 ns /639 = 0.056   => 17.5 GFLOPS
``` 
3,866  01933  5.17


=======================
com diretiva -O2,  Otimizado
o custo do loop e 1 flop

r=r+a           :   0.86 ns
r=a+r.(b+r.(a+r):   4.32 ns 

Descontando o loop e 1 flop o custo de 4 flops: 
r=a+r.(b+r.(a+r):   4.32 ns -0.86ns = 3.46 ns/4= 0.865 ns
                                               1.16 Gflop/s




PC da UFRGS (linux)
===
i7-4820K,  3.7GHz
L1 128K+128K x4
L2  1MBx4
L3 10MBx4

r=r+a:              2.36 ns 
r=a+r.(b+r.(a+r):   6.45 ns 
                    6.45-2.36=4.09/4=1.02 ns por flop

Com otimização -O2

r=r+a:              0.77 ns 
r=a+r.(b+r.(a+r):   4.90 ns 
                    4.90-0.77=4.13/4=1.03 ns por flop  0.97 Gflop/s





[[Fortran - tempos2 - taylor]]

[[Fortran-tempos3]]
