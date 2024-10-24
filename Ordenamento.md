

Algoritmos de Ordenamento

![](Pasted%20image%2020240930141822.png)

melhor caso: ordenados
pior caso: ordenados na ordem inversa
Estável: é estável se duas chaves com elementos idênticos mantem a mesma ordem.

# Bubblesort

https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheBubbleSort.html?mode=browsing


![](Pasted%20image%2020241007212105.png)

Necessário fazer um swap entre dois valores x[i] com x[j].

```python
def bubble_sort(L):
    for i in range(len(L) - 1, 0, -1):
        for j in range(i):
            if L[j] > L[j + 1]:
                temp = L[j]
                L[j] = L[j + 1]
                L[j + 1] = temp

```

## Complexidade
passada  comparações
---------------------------------
  1         n-1  
  2         n-2
  3
  ...
  n-1        1


# Short Bubble
Melhoria: se a lista já estiver ordenada parar o algoritmo

# Selection Sort
Ao passar uma vez o algoritmo, movimenta somente um elemento.

![](Pasted%20image%2020241010113018.png)

da referência temos:

```python
def selection_sort(a_list):
    for i, item in enumerate(a_list):
        min_idx = len(a_list) - 1
        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_idx]:
                min_idx = j
        if min_idx != i:
            a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx]
```

# Insertion Sort

https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheInsertionSort.html?mode=browsing

Sempre mantém uma sublista ordenada nas posições mais baixas da lista. Cada novo item é então inserido de volta na sublista anterior aumentando o tamanho da sublista.

![](Pasted%20image%2020241010113324.png)

Em detalhes o passo 5:

![](Pasted%20image%2020241010113544.png)


# The Shell Sort

![](Pasted%20image%2020241010204410.png)

![](Pasted%20image%2020241010204659.png)



# Mergesort
https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheMergeSort.html?mode=browsing

É um tipo de estratégia divisão-e-conquista. 

Algoritmo com função recursiva (overhead?) x função única com recursividade.



![](Pasted%20image%2020241010204813.png)

![](Pasted%20image%2020241010204823.png)

```python
def merge_sort(a_list):
    print("Splitting", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    print("Merging", a_list)

```

O custo é $O(n log_2(n))$

# Quicksort

https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheQuickSort.html?mode=browsing

1. Escolha o pivô p (geralmente o primeiro)
2. Crie um marcador a esquerda e um a direita e movimente os dois para o centro até que a lista esteja particionada com elementos menores que p a esquerda e maiores que p a direita.
3. Repita o processo nas duas sublistas recursivamente

![](Pasted%20image%2020241024184052.png)

![](Pasted%20image%2020241024184109.png)
![](Pasted%20image%2020241024184127.png)




# Heapsort

