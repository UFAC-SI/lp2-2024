class Quarto:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade
        self.disponivel = True
        self.cliente = None

    def reservar(self, cliente):
        if self.disponivel:
            self.cliente = cliente
            self.disponivel = False
            return True
        else:
            return False

    def liberar(self):
        self.disponivel = True
        self.cliente = None
        return True

    def __str__(self):
        return f'{self.numero}|{self.capacidade}|{self.disponivel}'