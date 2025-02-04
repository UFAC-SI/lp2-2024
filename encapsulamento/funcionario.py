class SalarioError(Exception):
    pass

class Funcionario:
    def __init__(self, nome, salario, cargo):
        try:
            if salario < 0:
                raise SalarioError('Salário não pode ser negativo.')
            self._salario = salario
            self._nome = nome
            self._cargo = cargo
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

    def trocar_cargo(self, novo_cargo):
        self._cargo = novo_cargo

    @property
    def cargo(self):
        return self._cargo
