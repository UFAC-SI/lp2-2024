#Teste
from projeto import Projeto
from funcionario import Funcionario

p1 = Projeto(1, 'Projeto 1', 'Teste')
p2 = Projeto(2, 'Projeto 2', 'Teste')

f1 = Funcionario(1, 'Fulano', 'Gerente')
f2 = Funcionario(2, 'Ciclano', 'Diretor')
f3 = Funcionario(3, 'Beltrano', 'Estagiário')

p1.adicionar_funcionario(f1, 'Scrum Master', '01/01/2025')
p1.adicionar_funcionario(f2, 'PO', '15/01/2025')
p2.adicionar_funcionario(f1, 'Scrum Master', '01/01/2025')
p1.adicionar_funcionario(f3, 'Frontend', '01/01/2025')

p1.listar_funcionarios()
p1.remover_funcionario(f1)
p1.listar_funcionarios()

f1.listar_projetos()

