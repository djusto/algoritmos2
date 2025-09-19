module mod_pilha
   implicit none
   
   type :: pilha
      integer :: k = 0
      integer :: n
      integer, dimension(:), allocatable :: p
   contains
      procedure :: add
      procedure :: remove
   end type 

contains

   subroutine construtor(self, n_max)
      class(pilha), intent(inout) :: self
      integer, intent(in) :: n_max

      self%n = n_max
      allocate(self%p(self%n))
      self%p = 0
      self%k = 0
   end subroutine construtor

   subroutine add(self, x)
      class(pilha), intent(inout) :: self
      integer,      intent(in)    :: x

      if (self%k < self%n) then
         self%k = self%k + 1
         self%p(self%k) = x
      else
         print *, "erro: a pilha esta cheia!"
      end if
   end subroutine add

   subroutine remove(self, x)
      class(pilha), intent(inout) :: self
      integer, intent(out)        :: x

      if (self%k > 0) then
         x = self%p(self%k)
         self%k = self%k - 1
      else
         print *, "         :( a pilha esta vazia"
         x = 0
      end if
   end subroutine remove

end module mod_pilha

