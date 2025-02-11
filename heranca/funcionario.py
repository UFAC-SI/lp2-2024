class SalarioError(Exception):
    pass

class Funcionario:
    def __init__(self, nome, salario, cpf):
        try:
            if salario < 0:
                raise SalarioError('Salário não pode ser negativo.')
            self._salario = salario
            self._nome = nome
            self._cpf = cpf
        except SalarioError as se:
            print(se)


    def aumentar_salario(self, percentual):
        self._salario += percentual * self._salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise SalarioError('Salário não pode ser negativo.')
        else:
            self._salario = valor

    @property
    def cpf(self):
        return self._cpf

    def get_bonificacao(self):
        #sprint('Chamada da superclasse')
        return self._salario * 0.1

    def __str__(self):
        return f'{self._nome}|{self._salario}'
