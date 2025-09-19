#ifndef STACK_H
#define STACK_H

// Inclui bibliotecas necessárias para alocação de memória e tratamento de erros
#include <stdio.h>
#include <stdlib.h>

// Definição da estrutura da pilha
typedef struct {
    int k; // Topo da pilha (contador)
    int n; // Tamanho máximo da pilha
    int *p; // Ponteiro para o array de elementos
} Stack;

// Protótipos das funções
void constructor(Stack *s, int max_size);
void add(Stack *s, int x);
int remove_element(Stack *s);
void free_stack(Stack *s);
int get_max(Stack *s);

#endif // STACK_H

