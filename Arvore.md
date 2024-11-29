Definições:
![](Pasted%20image%2020241128225917.png)

Exemplos:
![](Pasted%20image%2020241128230014.png)

``` html
<html lang="en">
<head>
    <meta charset=utf-8" />
    <title>simple</title>
</head>
<body>
<h1>A simple web page</h1>
<ul>
    <li>List item one</li>
    <li>List item two</li>
</ul>
<h2><a href="https://www.luther.edu">Luther College</a><h2>
</body>
</html>
```


# Quadtree

Sem balanceamento de níveis

![](Pasted%20image%2020241128233859.png)

Com balanceamento de níveis

![](Pasted%20image%2020241128233821.png)


https://lume.ufrgs.br/handle/10183/23901



# Árvore binária

![](Pasted%20image%2020241128230720.png)

Uma estrutura básica (ou Node)
```python
class Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def add(self, value):     # caso especial (Vazia)
        if self.data == None:
            self.data = value
        else:
            self._add(value)

    def _add(self, x):
        if x < self.data:
            if self.left == None:
                self.left = Tree(x)   # cria a esquerda
            else:
                self.left.add(x)
        else:                         # x >= self.data
            if self.right == None:    
                self.right = Tree(x)  # cria a direita
            else:
                self.right.add(x)


```

Três maneiras de percorrer a árvore:

in ordem:  esquerda, acima, direita

```python
  def in_order(self, lista=None):
        if lista == None:
            lista = []
        if self.left != None:
            self.left.in_order(lista)    # Esquerda
            
        lista.append(self.data)          # Meio
        
        if self.right != None:           # Direita
            self.right.in_order(lista)
            
        return lista
```


post-ordem:  esquerda, direita, acima

```python
    def pos_order(self, lista=None):
        if lista == None:
            lista = []
        if self.left != None:
            self.left.pos_order(lista)    # Esquerda
            
        
        if self.right != None:           # Direita
            self.right.pos_order(lista)

        lista.append(self.data)          # Meio
            
        return lista
```


pre-ordem: acima, esquerda, direita.

```python
    def pre_order(self, lista=None):
        if lista == None:
            lista = []
        lista.append(self.data)          # Meio

        if self.left != None:
            self.left.pre_order(lista)    # Esquerda
            
        
        if self.right != None:           # Direita
            self.right.pre_order(lista)

            
        return lista

```

Exemplo de uso

```python 
T = Tree()
T.add(10)

T.add(5)
T.add(15)
T.add(7)
T.add(3)
T.add(4)
T.add(8)

print("T in_order:", T.in_order())

print("T pre_order:", T.pre_order())

print("T out_order:", T.pos_order())

```

Remover nós

![](Pasted%20image%2020241128231949.png)

Exemplos: 

Remover 2
Remover 5
Remover 9
Remover 4

https://runestone.academy/ns/books/published/pythonds3/Trees/SearchTreeImplementation.html?mode=browsing

![](Pasted%20image%2020241128232824.png)

![](Pasted%20image%2020241128232837.png)

