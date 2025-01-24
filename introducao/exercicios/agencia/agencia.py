from conta import Conta
class Agencia:
    def __init__(self, nome):
        self.nome = nome
        self.status = True
        self.contas = []

    def adicionar_conta(self, n, s, l):
        if self.status:
            conta = Conta(n, s, l)
            self.contas.append(conta)
        else:
            print(f'Agência {self} foi encerrada.')

    def listar_contas(self):
        print(f'Contas da Agência: {self}')
        for c in self.contas:
            print(c)

    def fechar_agencia(self):
        while len(self.contas) > 0:
            self.contas.pop()
        self.status = False
        print(f'Agência {self} encerrada!')

    def __str__(self):
        return f'{self.nome}'