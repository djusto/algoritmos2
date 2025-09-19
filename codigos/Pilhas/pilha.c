#include "pilha.h"

// Função para inicializar a pilha (equivalente ao construtor)
void constructor(Stack *s, int max_size) {
    s->n = max_size;
    s->k = 0;
    s->p = (int *)malloc(sizeof(int) * s->n);    // Aloca dinamicamente a memória para o array
    if (s->p == NULL) {
        fprintf(stderr, "Erro na alocação de memória!\n");
        exit(EXIT_FAILURE);
    }
}

void add(Stack *s, int x) {       // Adiciona x na pilha
    if (s->k < s->n) {
        s->p[s->k] = x;
        s->k++;
    } else {
        printf("Erro: a pilha esta cheia!\n");
    }
}

int remove_element(Stack *s) {     // Remove elemento da pilha
    if (s->k > 0) {
        s->k--;
        return s->p[s->k];
    } else {
        printf("         :( a pilha esta vazia\n");
        return -1; // Retorna um valor de erro
    }
}

// Função para liberar a memória alocada dinamicamente
void free_stack(Stack *s) {
    free(s->p);
    s->p = NULL;
}

// Função para encontrar o valor máximo
int get_max(Stack *s) {
    if (s->k == 0) {
        printf("Erro: a pilha esta vazia\n");
        return -1;
    }
    int max_val = s->p[0];
    for (int i = 1; i < s->k; i++) {
        if (s->p[i] > max_val) {
            max_val = s->p[i];
        }
    }
    return max_val;
}

