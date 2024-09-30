
$$
sin(x) = x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+...
       = \sum_{k=0}^{p} (-1)^{k}\frac{x^{2k+1}}{(2k+1)!}$$

$$
c_k =  \frac{(-1)^{k} }{(2k+1)!}$$
$$
sin(x) \approx x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}
$$
Para os primeiros 7 termos:
```fortran
p7 = x * (1.0D0 + x**2 * (-1.0D0/6.0D0 + x**2 * (1.0D0/120.0D0 + x**2 * (-1.0D0/5040.0D0))))

!ou
c1= 1.D0
c2=-1.D0/6.D0    !  1/3!
c3= 1.D0/120.D0  !  1/5!
c4=-1.D0/5040.D0 !  1/7!
c5= 1.0D0/362880.0D0  ! 1/9!
c6=-1.0D0/39916800.0D0 !  1/11!
c7= 1.0D0/6227020800.0D0   !1/13!

y = x*x
p7= x*(c1 +y*(c2 +y*(c3 +y*(c4))))
p9= x*(c1 +y*(c2 +y*(c3 +y*(c4 +y*(c5)))))
p11=x*(c1 +y*(c2 +y*(c3 +y*(c4 +y*(c5 +y*(c6))))))
p13=x*(c1 +y*(c2 +y*(c3 +y*(c4 +y*(c5 +y*(c5 +y*(c7)))))))


S=0.D0
N=1000
! integral de 0 a 1,
! 

dx=(1.d0/N)
x =0.D0
do k=1,N
   x  =x+dx 
   y  =x*x
   p13=x*(c1 +y*(c2 +y*(c3 +y*(c4 +y*(c5 +y*(c5 +y*(c7)))))))
   S  =S+p13   ! p13*dx
end do
S=S*dx

```


Utilizando N=1000000

Teste1: A expressão original
```fortran
 p13= x - (x**3 )/6.0D0 + (x**5)/120.0D0 - (x**7)/5040.0D0 + (x**9)/362880.0D0 &
    &   - (x**11)/39916800.0D0 + (x**13)/6227020800.0D0
```
temos tempo = 15.53 milis.

Teste2: Reorganizando com algoritmo de Horner
```fortran
p13=  x    *(1.0D0             +x**2 *(-1.0D0/6.0D0        &
   &+ x**2 *(1.0D0/120.0D0     +x**2 *(-1.0D0/5040.0D0     &
   &+ x**2 *(1.0D0/362880.0D0  +x**2 *(-1.0D0/39916800.0D0 &
   &+ x**2 *(1.0D0/6227020800.0D0)))))))
```
temos tempo = 5.05 milis.

Teste3: Retirando as constantes pra fora do loop,
```fortran
p13=x*(c1 +y*(c2 +y*(c3 +y*(c4 +y*(c5 +y*(c6 +y*(c7)))))))  ! 13flop
```
temos tempo = 5.7 milis !!!

Teste4: separar as parcelas,
temos tempo = 6.8 milis !!!


Utilizando -O2 (Otimização)
Teste1: 5.27 milis   ( 3.0 GFLOPS )
Teste2: 2.24 milis   ( 7.1 GFLOPS )
Teste3: 2.24 milis   ( 7.1 GFLOPS )
Teste4: 3.62 milis   ( 4.4 GFLOPS )


Utilizando computação paralela e MPI:

mpirun -np  1 taylor:       5.71 ms ( 2.8 GFLOPS)
mpirun -np  2 taylor:       2.90 ms ( 5.5 GFLOPS)
mpirun -np  4 taylor:       1.53 ms (10.4 GFLOPS)
mpirun -np  8 taylor:       0.94 ms (16.9 GFLOPS)
mpirun -np 16 taylor:       (xxxx)

-np 1                    -np 4                 -np 8

![[Pasted image 20240920201104.png]]![[Pasted image 20240920201242.png]]![[Pasted image 20240920201457.png]]


Utilizando computação paralela e MPI e otimização:

mpirun -np  1 taylor:       2.23 ms ( 7.1 GFLOPS)
mpirun -np  2 taylor:       1.13 ms (14.1 GFLOPS)
mpirun -np  4 taylor:       0.66 ms (24.0 GFLOPS)
mpirun -np  8 taylor:       0.39 ms (40.1 GFLOPS)


O máximo em memória Bandwidth é 46.9 GB/s (em DDR4-2933)
(dividindo por 8)                5.8 GFloat/s (real* 8)

Reduzindo precisão para 32bits (hmm mesmos tempos)
mpirun -np  1 taylor:       2.23 ms ( 7.1 GFLOPS)
mpirun -np  2 taylor:       1.13 ms (14.1 GFLOPS)
mpirun -np  4 taylor:       0.66 ms (24.0 GFLOPS)
mpirun -np  8 taylor:       0.38 ms (40.1 GFLOPS)
mpirun -np 16 taylor:       (xxxx)




