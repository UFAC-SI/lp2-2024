from funcionario import Funcionario
class Gerente(Funcionario):
    #Funcionario é a superclasse
    #Gerente é subclasse
    def __init__(self, nome, salario, cpf, senha, qtde):
        super().__init__(nome, salario, cpf)
        self._senha = senha
        self._qtde = qtde

    def get_bonificacao(self):
        #print('Chamada da subclasses')
        return super().get_bonificacao() + 1000