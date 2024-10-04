
Como guardar um dado "composto" como o nome de aluno e cartão. Simplesmente criar uma lista em python.
```python
def Aluno(nome,cartao):
    return (nome,str(cartao))

a=Aluno('João',112121)
b=Aluno('Maria',988811)
```

ou criar um objeto do  tipo retangulo:
```python
def Retangulo(lado,altura):
    return (lado,altura)

def area(R):
    return R[0]*R[1]

def descricao(R):
	A=area(R)
    return f'O retângulo possui lado {R[0]} e altura {R[1]} com área {A}'


A=Retangulo( 1.0, 2.0)
B=Retangulo( 2.0, 3.0)

print(A)
print(B)

print( area(A))
print( descricao(B))

```

Um método melhor é criar uma classe de Retângulos:

```python
class Retangulo:
	def __init__(self, lado,altura):
	    self.lado = lado
	    self.altura= altura
	
	def __str__(self):
	    A=self.area()
	    return f'Retângulo lado {self.lado} e altura {self.altura} com área {A}'

    def area(self):              # definicao interna a classe  R.area() 
	    return self.lado *self.altura
	
	
def area(R):                    # definição externa à classe,  area(R)
     return R.lado * R.altura

A=Retangulo( 1.0, 2.0)
print( A.area() )
print( A )
```




Dois tipos de relações importantes entre classes são [Composição](OO%20composição.md) e [Herança](OO%20herança.md) .

Para as estruturas que criarmos (como Lista, Pilha, Árvore), poderemos usar o tipo composição.   
Todas elas podem conter um ==valor==, que pode ser por exemplo  um int, um real ou um nodo:

```python
class Node:
   def __init__(self,valor):
       self.valor = valor
       #self.nome=...
       #self.idade=...
   
   def __str__(self):
       return f'[ valor:{self.valor}]'
```



Exemplos


