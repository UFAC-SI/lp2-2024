class Hotel:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.quartos = []

    def incluir_quarto(self, quarto):
        self.quartos.append(quarto)

    def reservar_quarto(self, numero, cliente):
        for quarto in self.quartos:
            if quarto.numero == numero:
                if quarto.reservar(cliente):
                    print(f'Quarto {quarto.numero} reservado com sucesso pelo {quarto.cliente}!')
                else:
                    print(f'Quarto {quarto.numero} está ocupado!')

    def liberar_quarto(self, numero):
        for quarto in self.quartos:
            if quarto.numero == numero:
                print(f'{quarto.cliente}', end=' ')
                quarto.liberar()
                print(f'liberou o quarto {quarto.numero}.')


    def verificar_disponibilidade(self):
        print('Quartos disponíveis:')
        for quarto in self.quartos:
            if quarto.disponivel:
                print(f'Quarto: {quarto.numero}, '
                      f'Capacidade: {quarto.capacidade}')