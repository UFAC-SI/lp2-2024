from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Fulano', '123')
cliente2 = Cliente('Beltrano', '456')

conta1 = Conta(101, 0, 0)
conta2 = Conta(102, 100, 100)

cliente1.adicionar_conta(conta1, 'Titular')
cliente1.adicionar_conta(conta2, 'Titular')

cliente1.listar_contas()

cliente2.adicionar_conta(conta1, 'Dependente')

conta1.listar_clientes()