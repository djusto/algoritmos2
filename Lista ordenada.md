Criar uma lista que esteja sempre ordenada
![](Pasted%20image%2020241121102101.png)

```python
class OList:
    def __init__(self):
        self.head = None
```


Criar um search que busca a posição do primeiro item maior que o fornecido

![](Pasted%20image%2020241121102253.png)

```python
    def search(self,item):
        current = self.head
        achou   = False
        stop    = False
        while current != None and not achou and not stop:
            if current.data == item:
                achou = True
            else:
                if current.data > item:
                    stop = True
                else:
                    current = current.next
    
        return achou

```

Como adicionar com o add um novo item
![](Pasted%20image%2020241121102629.png)

```python
    def add(self,item):
        current  = self.head
        previous = None
        stop     = False
        while current != None and not stop:
            if current.data > item:
                stop = True
            else:
                previous = current
                current = current.next
    
        temp = Node(item)
        if previous == None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next=temp

    def __str__(self):
        res=''
        current = self.head
        while current != None:
            res=res+ current.__str__()
            current = current.next

        return res



    def remove(self,item):
        current  = self.head
        previous = None
        achou    = False
        while not achou:
            if current.data == item:
                achou = True
            else:
                previous = current
                current = current.next
    
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next


```



## Análise de Listas Ligadas

Considere uma lista ligada que tenha _n_ nós. 

O método `isEmpty()` consome tempo : O(1) já que requer apenas um passo para verificar se a referência da cabeça é para `None`. 

`size()`, por outro lado, sempre exigirá etapas _n_, pois não há como saber quantos nós estão na lista ligada sem percorrê-la do início ao fim. 

Portanto, `size()` consome tempo O(n). (Porém guardando n, é O(1) )

Inserir um item a um lista não ordenada consumirá sempre tempo O(1) uma vez que simplesmente o novo nó é inserido como cabeça da lista ligada.

No entanto, `search()` e `remove()`, bem como `add()` para uma lista ordenada, todos requerem que a lista seja percorrida. Embora, em média, possam precisar atravessar apenas metade dos nós, todos esses métodos consomem tempo O(n) já que no pior dos casos devemos processar todos os nós da lista.
