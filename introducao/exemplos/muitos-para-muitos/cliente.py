from cliente_conta import ClienteConta
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta, tipo):
        #Ligação entre os objetos Cliente e Conta
        cliente_conta = ClienteConta(self, conta, tipo)
        #Adiciona os objetos nas listas
        self.contas.append(cliente_conta)
        conta.clientes.append(cliente_conta)

    def listar_contas(self):
        print(f'Contas do cliente: {self}')
        for cc in self.contas:
            print(f'{cc.conta}')

    def __str__(self):
        return f'{self.nome}'