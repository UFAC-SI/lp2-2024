from projeto_funcionario import ProjetoFuncionario
class Projeto:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.funcionarios = []

    def listar_funcionarios(self):
        print(f'Funcionários do projeto {self}:')
        for item in self.funcionarios:
            print(item.funcionario)
        print(f'Total de funcionários:{len(self.funcionarios)}')

    def adicionar_funcionario(self, func, papel, data):
        associacao = ProjetoFuncionario(self, func, papel, data)
        self.funcionarios.append(associacao)
        func.projetos.append(associacao)

    def remover_funcionario(self, func):
        #encontar o func
        func_remover = None
        for item in self.funcionarios:
            if item.funcionario.id == func.id:
                func_remover = item
                break
        if func_remover:
            self.funcionarios.remove(func_remover)
            func.projetos.remove(func_remover)
            print('Funcionário removido com sucesso!')

    def __str__(self):
        return f'Projeto: {self.nome} ({self.id})'