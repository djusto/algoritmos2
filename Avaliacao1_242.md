Avaliação a ser entregue:

Regras: A avaliação pode ser feita em duplas. Entretanto cada aluno deve enviar a sua cópia do trabalho executada em um computador diferente.

Idealmente o tempo aproximado para realizar deveria ser menor que 4 horas.(correspondente as aulas da semana). Façam no mínimo os exercícios 0 e 1.

# Exercício 0 (Obrigatório)
Indique qual processador e velocidade (Ex. Intel i5 7410 com 3 GHz) e a memória RAM.


# Exercício 1 (Obrigatório)

Medição de tempo:
Faça um código que utilize a classe Pilha, calcule o tempo para:

* inicia o relógio
* crie uma pilha com n elementos
* inclua n elementos aleatórios na pilha
* remova n/2 elementos
* inclua novamente n/2 elementos aleatórios na pilha.
* finaliza o relógio

Note que a criação da pilha e a inclusão dos elementos está tudo dentro da medida de tempo.

Calcule o tempo para por exemplo n=100000, n=200000, n=400000,n... até ter umas 6 medidas de tempo diferentes. Note que n vai dobrando.
Se o computador for lento, inicie com um n menor, se for rápido demais (e os tempos ficarem zerados), inicie com um n maior ou repita o processo e divida pelo número de repetições.

Faça um gráfico onde no eixo x está o log_10(n) e no eixo y está o tempo.

Entregue a listagem do código do tempo, os valores do tempo e o gráfico.


# Exercício 2 (Recomendado)
Considere a classe Pilha vista em aula e o método add (abaixo). Quando tentamos incluir um elemento que excede o tamanho da pilha (n), está imprimindo uma mensagem. Corrija o método tal que quando a inclusão passar do limite, o método cria um novo array com o dobro do tamanho, copia os elementos existentes para esse novo e apaga o array temporário.

```python 
    def add(self,x):
        if self.k<self.n:
            self.P[self.k]=x
            self.k=self.k+1
        else:
            print("         :( passou do limite  ")

```

Entregue a listagem somente da novo método add

# Exercício 3 (Recomendado)
Considerando que o exercício 2 está correto.

Repita o exercício 1 iniciando com uma pilha de tamanho n=10, P=Pilha(10),
entretanto repita o processo de medida de tempo com os mesmos valores de n do exercício 1. Queremos medir se o tempo de ficar criando e apagando cópias da pilha afetará o processo.

Ou seja, a única coisa que muda entre o exercício 1 e o 3 é que  no exercício 1 começará com P=Pilha(n) e no ex.3 começa com P=Pilha(10).



# Resultados

## Exercicio2:
```python
    def add(self, x):
        if self.k >= self.n:
            self.n *= 2
            temp = zeros(self.n, dtype=int)
            temp[0:self.k] = self.P   # copiando o vetor
            self.P = temp
            del temp
            print(f'Dobrando n={self.n}')

        self.P[self.k] = x
        self.k = self.k+1

```



* [Pilha Medida Tempo](Pilha%20Medida%20Tempo)

Resultados de alguns alunos
[aval1.py](aval1.py.md)
