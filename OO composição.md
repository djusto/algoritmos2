Um classe "contém" (has a) outra classe. Por exemplo uma figura composta  por um círculo e um quadrado.

```python
import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def __str__(self):
        return f'Círculo: Raio = {self.raio}, Área = {self.area():.2f}'


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def __str__(self):
        return f'Quadrado: Lado = {self.lado}, Área = {self.area():.2f}'


class FiguraComposta:            # Classe que usa composição
    def __init__(self, circulo, quadrado):
        self.circulo = circulo    # Um circulo e um quadrado
        self.quadrado = quadrado

    def area_total(self):
        return self.circulo.area() + self.quadrado.area()

    def __str__(self):
        return (f'Figura Composta:\n'
                f'{self.circulo}\n'
                f'{self.quadrado}\n'
                f'Área Total = {self.area_total():.2f}')

# Exemplo de uso
C = Circulo(5)
Q = Quadrado(4)
figura = FiguraComposta(C, Q)

print(figura)

```