from conta import Conta
c1 = Conta(101,'Fulano', 1000, 200)
for i in range(100):
    Conta(i, 'Fulano'+str(i), 10+i, 1+i)
#Forma de acesso incorreta
#print(c1._total_contas)
#print(Conta._total_contas)
print(c1.get_total_contas()) #Metodo de Instância
print(Conta.get_total_contas(c1)) #Metodo de Instância
c2 = Conta(102,'Fulano', 1000, 200)
print(c2.get_total_contas_estatico()) #Metodo estatico
print(Conta.get_total_contas_estatico()) #Metodo estatico
c3 = Conta(101,'Fulano', 1000, 200)
print(Conta.get_total_contas_classe()) #Metodo de classe
print(c3.get_total_contas_classe()) #Metodo de classe

#slots
#c1.chave_pix = '68999999999'
print(vars(c1))