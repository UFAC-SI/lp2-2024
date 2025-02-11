from funcionario import Funcionario
from gerente import Gerente
from controle_de_bonificacoes import ControleDeBonificacoes

class Cliente:
    pass

f1 = Funcionario('Fulano', 5000, '999999999999')
g1 = Gerente('Ciclano', 9000, '88888888888', '123', 4)

print(f1)
print(g1)
#Bonificações
print(f1.get_bonificacao())
print(g1.get_bonificacao())
#Controle das bonificações
controle = ControleDeBonificacoes()
controle.registra(f1)
controle.registra(g1)
c1  = Cliente()
controle.registra(c1)
print(controle.get_total())
