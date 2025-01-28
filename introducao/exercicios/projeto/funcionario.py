class Funcionario:
    def __init__(self, id, nome, cargo):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.projetos = []

    def __str__(self):
        return f'Nome: {self.nome} ({self.id})'

    def listar_projetos(self):
        print(f'Projetos que {self.nome} participa:')
        for item in self.projetos:
            print(f'{item.projeto.nome}|{item.papel}|{item.data_inicio}')
        print(f'Total de participações em projetos: {len(self.projetos)}')
