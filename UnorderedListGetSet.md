Criar uma objeto básico para o Nó (Nodo)
![](Pasted%20image%2020241121091637.png)

Versão de node com get, set

```python
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

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
        temp.setNext(self.head)
        self.head=temp

    def __str__(self):
        res=''
        current = self.head
        while current != None:
            res=res+ current.__str__()
            current = current.getNext()

        return res

    def search(self,item):
        current = self.head
        achou = False
        while current != None and not achou:
            if current.getData() == item:
                achou = True
            else:
                current = current.getNext()
    
        return achou


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

