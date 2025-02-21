class Sobrecarga:
    def __init__(self):
        print('Um')
    # def __init__(self):
    #     print('Dois')
    # def __init__(self):
    #     print('Três')

Sobrecarga()

class Sobrecarga2:
    def __init__(self, *args):
        self._argumentos = args
        self._tam = len(args)
        self.__str__()

    def __str__(self):
        if self._tam == 0:
            print('Zero')
        if self._tam == 2:
            print("Dois")
        if (self._tam > 0):
            print(*self._argumentos)

Sobrecarga2('Teste', 4)

from functools import reduce
class Calculadora:
    def soma(self, *args):
        soma = 0
        for i in args:
            soma += i
        return soma

    def soma2(self, *args):
        return sum(args)

    def soma3(self, *args):
        return reduce(lambda x, y: x + y, args)


calc = Calculadora()
print(calc.soma3(1,2,3,4,5))
print(calc.soma3('Py','thon', 'é', 'complicado'))

from datetime import date
class Data:
    def __init__(self, data):
        if isinstance(data, str):
            self._d = date.fromisoformat(data)
        if isinstance(data, date):
            self._d = data

    def __str__(self):
        return f'{self._d.day:02d}/{self._d.month:02d}/{self._d.year}'

dia1 = Data('2025-02-09')
dia2 = Data(date.today())
print(dia2)

class Tempo:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self._hora = hora
        self._minuto = minuto
        self._segundo = segundo

    def __str__(self):
        return f'{self._hora}:{self._minuto}:{self._segundo}'

t1 = Tempo(8, 10, 30)
print(t1)

class Pessoa:
    def __init__(self, nome, idade=None):
        self._nome = nome
        self._idade = idade

    @classmethod
    def criar_pessoa(cls):
        return Pessoa('Anônimo')

p1 = Pessoa('Maria', 30)
p2 = Pessoa('Joe')
p3 = Pessoa.criar_pessoa()
print(p1._nome) #Não faça isso na prova
print(p2._nome)
print(p3._nome)