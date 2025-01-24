from agencia import Agencia
from emprestimo import Emprestimo
ag1 = Agencia('Centro')
#Quem cria as contas é agencia
ag1.adicionar_conta(1, 1000, 100)
ag1.adicionar_conta(2, 2000, 100)
ag1.adicionar_conta(3, 3000, 100)
ag1.listar_contas()
#ag1.fechar_agencia()
ag1.adicionar_conta(4, 3000, 100)

e1 = Emprestimo(ag1.contas[0], 5000, 5)
print(ag1.contas[0].saldo)
e1.pagar_parcela()
e1.pagar_parcela()
e1.pagar_parcela()
e1.pagar_parcela()
ag1.contas[0].sacar(2000)
e1.pagar_parcela()
e1.pagar_parcela()
print(ag1.contas[0].saldo)
