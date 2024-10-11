
Em C:
```c
int square(int a,int b) {
    int s;
    s=a;
    a=b;
    b=s;
    return s;
}
```

``` asm
push    rbp
mov     rbp, rsp
mov     DWORD PTR [rbp-20], edi
mov     DWORD PTR [rbp-24], esi

mov     eax, DWORD PTR [rbp-20]
mov     DWORD PTR [rbp-4], eax   # s=a

mov     eax, DWORD PTR [rbp-24]
mov     DWORD PTR [rbp-20], eax  # a=b
 
mov     eax, DWORD PTR [rbp-4]
mov     DWORD PTR [rbp-24], eax  # b=s

mov     eax, DWORD PTR [rbp-4]
mov     DWORD PTR [rbp-4], eax    # s=a
mov     eax, DWORD PTR [rbp-4]
pop     rbp
ret
```

Em Fortran
```
mov     eax, DWORD PTR [rbp-4]
mov     DWORD PTR [rbp-8], eax
mov     eax, DWORD PTR [rbp-12]
mov     DWORD PTR [rbp-4], eax
mov     eax, DWORD PTR [rbp-8]
mov     DWORD PTR [rbp-12], eax
```
