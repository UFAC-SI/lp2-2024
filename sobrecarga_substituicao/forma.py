import math


class Forma:
    def __init__(self, *args):
        self._tam = len(args)
        if self._tam == 1:
            self._tipo = 'Círculo'
        elif self._tam  == 2:
            if args[0] == args[1]:#Losango?
                self._tipo = 'Quadrado'
            else:
                self._tipo = 'Retângulo'
        elif self._tam == 3:
            self._a = args[0]
            self._b = args[1]
            self._c = args[2]
            if (self._a < self._b + self._c) and (self._b < self._a + self._c) and (self._c < self._a + self._b):
                self._tipo = 'Triângulo'
            else:
                self._tipo = 'Forma desconhecida'
                raise ValueError('Os parấmetros não formam um Triângulo.')

        else:
            self._tipo = 'Forma desconhecida'

    def area(self):
        return 0

    def perimetro(self):
        return 0

    def __str__(self):
        if self._tipo == 'Forma desconhecida':
            return f'{self._tipo} Não tem área e perímetro'
        else:
            return (f'{self._tipo}'
                f' - Área: {self.area()}'
                f' Perímetro: {self.perimetro()}')


class Circulo(Forma):
    def __init__(self, raio):
        super().__init__(raio)
        self._raio = raio

    def area(self):
        return math.pi * self._raio * self._raio

    def perimetro(self):
        return 2 * math.pi * self._raio

    # def __str__(self):
    #     return (f'{super().__str__()}'
    #             f' - Área: {self.area()}'
    #             f' Perímetro: {self.perimetro()}')

class Quadrilatero(Forma):
    def __init__(self, lado_a, lado_b):
        super().__init__(lado_a, lado_b)
        self._a = lado_a
        self._b = lado_b

    def area(self):
        return self._a * self._b

    def perimetro(self):
        return 2 * (self._a + self._b)

    # def __str__(self):
    #     return (f'{super().__str__()}'
    #             f' - Área: {self.area()}'
    #             f' Perímetro: {self.perimetro()}')

class Triangulo(Forma):
    def __init__(self, a, b, c):
        try:
            super().__init__(a, b, c)
            self._a = a
            self._b = b
            self._c = c
        except ValueError as error:
            print(error)

    def perimetro(self):
        if self._tipo == 'Triângulo':
            return self._a + self._b +self._c
        # else:
        #     return 0

    def area(self):
        if self._tipo == 'Triângulo':
            m = self.perimetro()/2
            return math.sqrt(m*(m-self._a)*(m-self._b)*(m-self._c))
        # else:
        #     return 0


    # def __str__(self):
    #     return (f'{super().__str__()}'
    #             f' - Área: {self.area()}'
    #             f' Perimetro: {self.perimetro()}')

c1 = Circulo(10)
q1 = Quadrilatero(4, 5)
t1 = Triangulo(1,2,3)
f1 = Forma()

formas = [c1,q1,t1,f1]
for f in formas:
    print(f)
