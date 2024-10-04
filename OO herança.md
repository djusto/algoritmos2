A herança entre classes é do tipo "é um(a)" (is a).   
O círculo é uma forma geométrica e o quadrado é uma forma geométrica.

### Classe Base `FormaGeometrica`:   
A classe `FormaGeometrica` é a classe base que define a estrutura comum para todas as formas geométricas, como o nome da forma. O método `area()` é abstrato, ou seja, precisa ser implementado pelas subclasses (`Circulo` e `Quadrado`), já que a área depende da forma.


### Subclasse `Circulo`:
A classe `Circulo` herda de `FormaGeometrica` e implementa o método `area()`, com a fórmula  $πr^2$ .

### Subclasse `Quadrado`:
A classe `Quadrado` também herda de `FormaGeometrica` e implementa sua própria versão do método `area()`, usando $lado^2$

### Uso do `super()`:
Em cada subclasse, o método `__str__()` utiliza o `super().__str__()` para herdar o comportamento da classe base, adicionando informações específicas da subclasse (raio ou lado e área).

### Polimorfismo:
Tanto `Circulo` quanto `Quadrado` têm o mesmo método `area()`, mas com implementações diferentes, permitindo que você trabalhe com objetos de forma geométrica de maneira uniforme, independentemente da forma exata.


```python
import math


class FormaGeometrica:         # Classe base
    def __init__(self, nome):
        self.nome = nome

    def area(self):
        raise NotImplementedError("Deve ser implementado pelas subclasses")

    def __str__(self):
        return f'Forma: {self.nome}'


class Circulo(FormaGeometrica):     # Subclasse Circulo
    def __init__(self, raio):
        super().__init__("Círculo")
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def __str__(self):
        return f'{super().__str__()}, Raio: {self.raio}, Área: {self.area():.2f}'


class Quadrado(FormaGeometrica):   # Subclasse Quadrado
    def __init__(self, lado):
        super().__init__("Quadrado")
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def __str__(self):
        return f'{super().__str__()}, Lado: {self.lado}, Área: {self.area():.2f}'

# Exemplo de uso
C = Circulo(5)
Q = Quadrado(4)

print(C)  # Saída: Forma: Círculo, Raio: 5, Área: 78.54
print(Q)  # Saída: Forma: Quadrado, Lado: 4, Área: 16.00

```