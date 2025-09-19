program teste_tempo
    use mod_pilha
    implicit none

    integer, parameter :: n = 100000
    integer, parameter :: repete = 10
    
    type(pilha) :: p
    integer     :: k, i, x
    real        :: inicio, fim, tt
    real        :: num_aleatorio
    
    call construtor(p, n)

    call random_seed()    ! semente do gerador aleatório

    call cpu_time(inicio)
    !===============================================  <= inicio
    do k = 1, repete
        ! Empilhando
        do i = 1, n
            call random_number(num_aleatorio)
            x = int(num_aleatorio * 1000) + 1 ! Gera um inteiro entre 1 e 1000
            call p%add(x)
        end do
        
        print *, maxval(p%p)
        
        do i = 1, n
            call p%remove(x)
        end do
    end do
    !============================================= <= fim
    call cpu_time(fim)
    tt = fim - inicio

    print *, "Tempo total: ", tt, " Tempo por loop:", tt/repete
    
end program teste_tempo

