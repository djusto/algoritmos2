# Algoritmos de Busca

Algoritmo de busca de uma string dentro de outra.

Sejam as string  x com comprimento m e y com comprimento n, encontre a posição de x em y.

## Algoritmo de busca força bruta

1. sem fase de pré-processamento
2. espaço extra de armazenamento constante    
3. sempre desloca a janela de busca por exatamente 1 posição à direita    
4. as comparações podem ser feitas em qualquer ordem    
5. fase de busca com complexidade: O(mn)
6. número de comparações de caracteres: O(2n)   
7. comparações são repetidas

```python
def FB(x,y):
    m=len(x)
    n=len(y)
    for j in range(0,n-m):
        i=0
        while (i<m) and (x[i]==y[i+j]):
            i=i+1
        if i>=m:
            print(j)
```

## Algoritmo de busca Morris-Pratt (MP)


O algoritmo de **Morris-Pratt** é uma variação simplificada do algoritmo de **Knuth-Morris-Pratt** (KMP) para busca de padrões em uma string. Ele é usado para encontrar todas as ocorrências de uma substring (o "padrão") em uma string maior (o "texto") de maneira eficiente, com complexidade de tempo **O(n + m)**, onde **n** é o tamanho do texto e **m** é o tamanho do padrão.

### Estrutura Básica do Algoritmo

O Morris-Pratt utiliza um array chamado **prefix function** ou **tabela de falhas**, que guarda informações sobre o padrão para evitar comparações redundantes. A ideia é que, quando há uma falha de correspondência entre o texto e o padrão, o algoritmo pode usar o prefixo que já foi verificado para pular parte das comparações, em vez de reiniciar do início do padrão.

### Passos do Algoritmo

**Construção da Tabela de Prefixos**: A tabela de prefixos é uma estrutura que armazena, para cada posição do padrão, o comprimento do maior prefixo que também é sufixo do padrão até aquela posição. Isso permite que o algoritmo saiba o quanto ele pode avançar no padrão quando ocorre uma falha de correspondência.
    
**Busca do Padrão**: A busca é realizada avançando simultaneamente no texto e no padrão. Sempre que há uma correspondência parcial, o algoritmo se baseia na tabela de prefixos para decidir o quanto pode avançar no padrão, sem precisar verificar novamente as comparações já feitas.


1. realiza as comparações da esquerda para a direita
2. fase de pré-processamento com complexidade espacial e temporal O(m)
3. fase de busca com complexidade O(m+n); independente do tamanho do alfabeto
4. realiza no máximo (2n-1) comparações
5. atraso na comparação: limitado a m
6. guarda a informação de quais caracteres já foram comparados, deixando de fazer algumas comparações, por serem desnecessárias (uso de deslocamentos calculados adequadamente), usando uma tabela contendo m+1 elementos
    

```python
def cria_tabela_MP(x):   # T[0:m-1]
    m=len(x)
    T=[0]*m #zeros(m)
    T[0]=0
    j=0                    # comprimento do maior prefixo
    for i in range(1,m):
        print(f' {i} e {j}')
        while j>0 and x[i]!=x[j]:
            j=T[j-1]

        if x[i]==x[j]:
            j=j+1
        T[i]=j
    return T

def MP(x,y):
    m=len(x)
    n=len(y)
    Tabela=cria_tabela_MP(x) # Pré-processamento: O(m)
    i=0 # Busca (usando a tabela): O(m+n)
    j=0
    for j in range(n):      # indice no texto
        while (i > 0) and (x[i] != y[j]):
            i=Tabela[i-1]
        if y[j]==x[i]:
            i=i+1
        if i==m:
            print(j-i)
            i=Tabela[i-1]
  
T1=cria_tabela_MP('ababd')
T2=Tcria_tabela_MP('aaabbaaabbacd')

x='ott'
y='Dagoberto Adriano Rizzotto Justo'  
```


## Algoritmo de busca (KMP)

Características:

1. realiza as comparações da esquerda para a direita
2. fase de pré-processamento com complexidade espacial e temporal
3. fase de busca com complexidade ; independente do tamanho do alfabeto
4. atraso na comparação: limitado a , onde (razão áurea)
5. melhoramento do algoritmo MP, com deslocamentos calculados de forma mais precisa.   


proc KMP(string x,y; int m,n)
// busca ocorrências da string x (com m caracteres)
// dentro da string y (de n) caracteres
1. int i,j,Tabela[0:m-1]
2. cria_tabela_KMP(x,m,Tabela) // Pré-processamento: O(m)
3. i:=0 // Busca (usando a tabela): O(m+n)
4. j:=0
5. enquanto j<n faça
6. enquanto (i>-1) & (x[i]/=y[j]) faça
7. i:=Tabela[i]
8. fim enquanto
9. i:=i+1
10. j:=j+1
11. se i>=m então
12. imprima j-i
13. i:=Tabela[i]
14. fim se
15. fim enquanto
fim proc
  

proc cria_tabela_KMP(string x; int m; ref int T[0:m-1])
// cria tabela T de ocorrências dos caracteres de x
1. int i,j
2. i:=0
3. T[0]:=-1
4. j:=-1
5. enquanto i<m faça
6. enquanto (j>-1) & (x[i]/=x[j]) faça
7. j:=T[j]
8. fim enquanto
9. i:=i+1
10. j:=j+1
11. se (i<m) & (x[i]==x[j]) então
12. T[i]:=T[j]
13. senão
14. T[i]:=j
15. fim se
16. fim enquanto  

fim proc
