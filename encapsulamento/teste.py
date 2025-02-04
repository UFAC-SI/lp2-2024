from conta import Conta
c1 = Conta(101, 'Fulano', 1000, 200)
#print(c1._saldo) #Acesso indevido
print(vars(c1))
c1.saldo = 2000
print(c1.saldo)