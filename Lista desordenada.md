Criar uma objeto básico para o Nó (Nodo)
![](Pasted%20image%2020241121091637.png)

```python
class Node:
    def __init__(self,item):
        self.data = item
        self.next = None

    def __str__(self):
        if self.next==None:
            x='.'
        else:
            x='->'
                
        return f"{self.data} {x} "

```

Criação de uma lista desordenada

![](Pasted%20image%2020241121091940.png)


```python
class UList:
    def __init__(self):
        self.head = None

    def add(self,item):
        temp=Node(item)
        temp.next=self.head
        self.head=temp

    def __str__(self):
        res=''
        current = self.head
        while current != None:
            res=res+ current.__str__()
            current = current.next

        return res

    def search(self,item):
        current = self.head
        achou   = False
        while current != None and not achou:
            if current.data == item:
                achou = True
            else:
                current = current.next
    
        return achou

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




x=Node(21)
y=Node(24)
print(x)

L=UList()
L.add(3)
L.add(8)
L.add(5)

print(L)

L.add(8)
print(L)

print( L.search(3) )
```


Versão com set e get sem acessar diretamente os dados.
[[UnorderedListGetSet]]
