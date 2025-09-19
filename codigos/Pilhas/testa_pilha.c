#include "pilha.h"
#include <time.h>
#include <sys/time.h> // Para gettimeofday
#include <stdlib.h> // Para srand, rand
#include <stdio.h>

int main() {
    const int n = 100000;
    const int repete = 10;
    
    Stack p;
    struct timeval inicio_tv, fim_tv;
    long tempo_microsegundos;
    
    srand(time(NULL));        // seed do gerador de aleatórios

    constructor(&p, n);       // inicia a pilha

    // Início da marcação de tempo
    gettimeofday(&inicio_tv, NULL);

    for (int k = 0; k < repete; k++) {
        // Empilhando
        for (int i = 0; i < n; i++) {
            int x = rand() % 1000 + 1; // Gera um inteiro entre 1 e 1000
            add(&p, x);
        }
        
        // Imprimindo o valor máximo
        printf("Max da pilha: %d\n", get_max(&p));
        
        // Desempilhando
        for (int i = 0; i < n; i++) {
            remove_element(&p);
        }
    }

    // Fim da marcação de tempo
    gettimeofday(&fim_tv, NULL);
    
    tempo_microsegundos = (fim_tv.tv_sec - inicio_tv.tv_sec) * 1000000 + (fim_tv.tv_usec - inicio_tv.tv_usec);
    double tt = (double)tempo_microsegundos / 1000000.0;

    printf("Tempo total: %f segundos\n", tt);
    
    free_stack(&p);

    return 0;
}

