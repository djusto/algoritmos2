**Análise de complexidade** é definida como uma técnica para caracterizar o tempo gasto por um **algoritmo** com relação ao tamanho da entrada (independente da máquina, linguagem e compilador). É usada para avaliar as **variações do tempo de execução** em diferentes algoritmos.



### Qual é a necessidade da Análise de Complexidade?

- A Análise de Complexidade determina a quantidade de recursos de ==tempo== e ==espaço== necessários para executá-la.
- Ele é usado para comparar diferentes algoritmos em diferentes tamanhos de ==entrada==.
- A complexidade ajuda a determinar a dificuldade de um problema.
- frequentemente medido por quanto tempo e espaço (memória) são necessários para resolver um problema específico

# Complexidade temporal x complexidade espacial x tempo físico

==Complexidade temporal==: número de operações básicas para um algoritmo. A operação básica depende do problema: pode ser flops, podem ser acesso a um elemento da estrutura de dados,

==Complexidade espacial==: quantidade de memória utilizada. A unidade básica pode ser baseada:
a) no tipo de dado, por ex., um vetor com 8 elementos do tipo real.
b) no n.o de bytes: 8 elementos x 8bytes = 64 bytes.

==Tempo físico==: a medida em segundos de quanto tempo leva para rodar um algoritmo. Idealmente deveria ser proporcional a complexidade temporal, porém pode depender da complexidade espacial e uma série de outros fatores.

tempo flop (+ - * /)         =
tempo sin,cos,sqrt()         =
tempo LOAD, acessar memória  =
tempo SAVE, salvar na memória=
tempo ler/salvar  no disco   =
tempo acessar banco de dados =
tempo acessar dado internet  =




# Notações assintóticas em análise de complexidade:

Ver [Notação Big O](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/)

**A notação Big-O** ("Ozão") representa o limite superior do tempo de execução de um algoritmo. Portanto, ela fornece a **pior** complexidade de um algoritmo. Ao usar **a notação Big O**, podemos limitar assintoticamente a **expansão** de um tempo de execução a uma faixa de fatores constantes acima e abaixo. É um modelo para quantificar *o desempenho do algoritmo.*

## Definição:

>[!definição]
>
Dizemos que 
$$f(n)=\mathcal O(g(n))$$
se  existem constantes positivas c e N tais que $|f(n)| ≤ c|g(n)|$ para todo n ≥ N. Geralmente  $n \rightarrow \infty$

De outra forma,
$$
\lim_{n \rightarrow \infty} \frac{f(n)}{g(n)} < \infty
$$


![[Pasted image 20240918131133.png]]


# Outras Notações de Complexidade

## Notação Omega 


>[!definição]
Dizemos que 
$$f(n)= \Omega(g(n))$$
se  existem constantes positivas c e N tais que $c|g(n)|≤|f(n)|$ para todo n ≥ N. Geralmente  $n \rightarrow \infty$

A notação **Omega** representa o limite inferior do tempo de execução de um algoritmo. Assim, ele fornece a **melhor** complexidade de um algoritmo.  

![[Pasted image 20240918163649.png]]
 
## Notação Theta 

>[!definição]
Dizemos que 
$$f(n)= \Theta(g(n))$$
se  existem constantes positivas c1,c2 e N tais que $c_1|g(n)|≤|f(n)|≤c_2|g(n)|$ para todo n ≥ N. Geralmente  $n \rightarrow \infty$

**A notação Theta** envolve a função de cima para baixo. Como ela representa o limite superior e inferior do tempo de execução de um algoritmo, ela é usada para **analisar** a complexidade **do caso médio** de um algoritmo. O tempo de execução serve como um limite **inferior e superior** na complexidade de tempo do algoritmo. Existe como um **limite máximo e mínimo** para um determinado valor de entrada. 

## Notação little-o


>[!definição]
Dizemos que 
$$f(n)= o(g(n))$$
se  $$\lim_{n \rightarrow \infty} \frac{f(n)}{g(n)} =0$$

Se a notação Big-O é uma notação onde f é mais próxima de g (apesar de poder ser distante), na notação "o-pequeno" a função g cresce muito mais rápido que f.




## Propriedades da notação Big-O:

[Propriedades gerais da notação assintótica:](https://www.geeksforgeeks.org/properties-of-asymptotic-notations/)

Propriedades das Notações:
Abaixo estão algumas propriedades importantes da notação Big O:

### 1. Reflexividade:

Para qualquer função f(n),    $f(n) = O(f(n))$.

Ex.:   $f(n) = n^2$ , então $f(n) = O(n^2)$.

### 2. Transitividade:

Se  $f(n) = O(g(n))$ e $g(n) = O(h(n))$, então  $f(n) = O(h(n))$. Ex.:

Ex: Sejam $$f(n) = n^2 , g(n) = n^3 , h(n) = n^4. $$
então  $f(n) = O(g(n))$ e $g(n) = O(h(n)).$

Portanto, $f(n) = O(h(n))$.

### 3. Fator constante:

Para qualquer constante c>0, se f(n) = O(g(n)), então cf(n) = O(g(n)).  


Ex.:  $f(n) = n$, $g(n) = n^2$. Então f(n) = O(g(n)). Portanto, $2f(n) = O(g(n))$.

Ex2.:
$$3n^2 = O(3n^2)=O(n^2)$$

### 4. Regra da soma:

Se $f(n) = O(g(n))$ e $h(n) = O(g(n))$, então  $f(n) + h(n) = O(g(n))$.

Ex.: $f(n) = n^2$, $g(n) = n^3$,  $h(n) = n^4$.

Então  $f(n) = O(h(n))$ e $g(n) = O(h(n))$. Portanto, $f(n) + g(n) = O(h(n))$.

Ou ainda,
$n^2+n^3 = O(n^2+n^3) = O(n^2)+O(n^3)=O(n^3)+O(n^3)=O(2n^3)=O(n^3)$


### 5. Regra do produto:

Se  $f(n) = O(g(n))$ e $h(n) = O(k(n))$, então $f(n).h(n) = O(g(n). k(n))$.


Ex.: Sendo $f(n) = n, g(n) = n^2 , h(n) = n^3 , k(n) = n^4$. 

Então  $f(n) = O(g(n))$ e $h(n) = O(k(n))$.

Portanto, $f(n).h(n) = O(g(n) . k(n)) = O(n^5 )$.

### 6. Regra de composição:

Se $f(n) = O(g(n))$ e $g(n) = O(h(n))$, então $f(g(n)) = O(h(n))$.

Ex:

Sendo $f(n) = n^2 , g(n) = n, h(n) = n^3$.  Então $f(n) = O(g(n))$ e $g(n) = O(h(n))$. 

Portanto, $f(g(n)) = O(h(n)) = O(n^3 )$.


# Exemplo de operações:

Considere a função  $f(n)=5n^3+17n^2+5n+1$

$$\begin{align}
f(n) &= 5n^3+17n^2+5n+1 \\
f(n) &= O(5n^3+17n^2+5n+1 )\\
f(n) &= O(5n^3)+O(17n^2)+O(5n)+O(1)\\
f(n) &= O(5n^3) \\
f(n) &= 5O(n^3) \\
f(n) &= \mathcal{O}(n^3)
\end{align}$$
Note que  $f(n)=5n^3+17n^2+5n+1=O(n^4)$ ou $O(2^n)$. (apesar de não ser tão  útil)



# Exemplos de Complexidade

![[Pasted image 20240918130713.png]]

## Complexidade Linear O(n)

Exemplo, procura um elemento:

```python
L=list(range(5))
busca = '@'
n = len(L)

for k in range(n):
    if L[k]==busca:
        print (f'Achei {busca} em {k}.)
        break


```



## Complexidade O(n^2)

Encontrar o maior elemento de uma matriz

```python

maior=A[0][0]
for i in range(m):
    for j in range(n):
        if A[i][j]>maior:
            marior=A[i][j]


```


## Complexidade Cúbica: O(n^3)

Multiplicação de matrizes

## Complexidade logarítmica: O(log(n))


## Complexidade $O(2^n)$

Gerar todos os subconjuntos de um conjunto.
```
void generateSubsets(int arr[], int n) {
for (int i = 0; i < (1 << n); i++) {
    for (int j = 0; j < n; j++) {
        if (i & (1 << j)){
             cout << arr[j] << " ";
        }
    }
    cout << endl;
}
}   
```

## Complexidade Fatorial
Gerar todas as permutações de um conjunto

```
void permute(int* a, int l, int r) {
	if (l == r) {
	    for (int i = 0; i <= r; i++) {
		    cout << a[i] << " ";
		}
		cout << endl;
	}else{
		for (int i = l; i <= r; i++) {
			swap(a[l], a[i]);
		    permute(a, l + 1, r);
		    swap(a[l], a[i]); // backtrack
		}
	}
}   
```
`




# Álgebra Linear
(Cálculo Numérico)

Custo computacional: Contar o número de operações em ponto flutuante (flops := floating operations) 

No passado contávamos somente multiplicações e divisões, pois levavam mais tempo que somas e subtrações (e em Álgebra Linear eram proporcionais as multiplicações).

## Ex. vetor x vetor:
Qual o custo para calcular o produto interno 
  $$ p=\vec{u} \cdot \vec{v}=u \cdot v$$
onde $u,v \in V^n$?

### Solução
$p=u_1 .v_1+...+u_n.v_n$

#### Em código
```python
n = len(u)
p = 0
for i in range(n):
    p = p + u[i]*v[i]
```

### Custo:
Como temos n pares, teremos n multiplicações e (n-1) somas, ou seja, 
Custo = O(n)+O(n-1) operações em ponto flutuante

>[!Custo vetor * vetor]
> C(n)=$O(2n-1)$ flops 

 = O(2n) flops
 = O(n) flops

Contando apenas multiplicações:  O(n) flops

# Exemplo com medição tempo:

```python
import numpy as np
import time
import math 

n     =10
repete=1000

x=np.zeros(n)
y=np.zeros(n)

for i in range(n):
    x[i]=math.sin( i )
    y[i]=math.cos( i )


inicio=time.time()           # <-  início do relógio
for k in range(repete):
    S=0.0                    # início do algoritmo
    for j in range(n):       # O(n)*O(2)= O(2n)
        S=S+x[j]*y[j]        #      O(2) flops
    
fim=time.time()             # <-  fim
tt =fim-inicio

print(f' Tempo {tt:3.7f} s')
tloop= tt/repete
custo= 2*n
tflop= (tloop/custo)
GFLOP= 1.0/tflop
print(f' tloop={tloop}  tflop={tflop }  GFLOP={GFLOP}')

```







## Ex. Matriz x vetor:
Qual o custo para calcular o produto matriz-vetor  $\vec{x} = A \vec{v}$ onde $x,v \in V^n$?
### Solução:
Cada elemento de x tem a forma
$x_i =A_{i,1} .v_1+A_{i,2} .v_2...+A_{i,n} .v_n,  \;\;\;i=1,...,n$
#### Em código
```python
n = len(u)
p = 0
for i in range(m):
    x[i]=0.0
    for j in range(n):
        x[i] = x[i] + A[i,j]*v[j]
```

### contagem

Cada $x_i$ é um produto interno de uma linha de A por v.

Portanto o custo para calcular cada elemento é

Custo é  O(2n-1) para uma linha.

Como temos n linhas teremos
C(n)=  (2n-1)+(2n-1)+...(2n-1) flops
C(n)=  n*(2n-1)
>[!Custo matriz * vetor]
>  C(n)= $\mathcal O( 2n^2-n)$ flops

C(n)= $O( 2n^2 ) = O( n^2  )$

Contando apenas multiplicações:  $n * O(n)=O(n^2)$ flops



## Ex. Matriz x Matriz:
Qual o custo para calcular o produto matriz-matriz
  $$ C = A \cdot  B$$
onde $A,B,C \in V^{n,n}$?
### Solução:
Note que uma cada elemento C(i,j) é calculado como o produto interno da linha i de A pela coluna j  de B: 

C[i,j] = A[i,:] * B[:,j]

#### Em código
```python
n = len(u)
p = 0
for i in range(m):
    for j in range(n):
        C[i,j]=0.0
        for k in range(n):
            C[i,j] = C[i,j] + A[i,k]*B[k,j]
```

### contagem

O custo para cada C[i,j] é um produto interno.

Como temos $n \times n$ elementos o custo será
C(n) = n.n.O(2n-1)

>[!Custo matriz * matriz]
>  C(n)= $\mathcal O( 2n^3-n^2)$ flops


Contando apenas multiplicações:  $n^2 * O(n)=O(n^3)$ flops


# Exemplos com medida de tempo real

Testar os tempos dos códigos matriz x vetor e matriz x matriz.



