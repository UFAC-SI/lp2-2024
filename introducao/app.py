from conta import Conta

c1 = Conta(1, 'Manoel', 1000, 100) #Cria uma instância da classe Conta
print(type(c1))
c1.titular = 'Manoel Limeira'
c1.saldo = 1000

c2 = Conta(2, 'Fulano', 500, 100)
#c2.saldo_extra = 500 #Em tempo de podemos criar
                     #atributos
print(c1)
print(c1.saldo)
#print(c2.saldo_extra)
c1.sacar(2000)
print(c1.saldo)

c3 = c1
print(id(c1))
print(id(c3))
c3.sacar(100)
print(c3.saldo)
c1.transferir(100, c2)
print(c2.saldo)
print(dir(c1))
print(vars(c1))