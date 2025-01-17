from historico import Historico

class Conta:
    def __init__(self, n, cliente, s, l): #Metodo de inicialização
        self.numero = n             #Atributos de instância
        self.titular = cliente
        self.saldo = s
        self.limite = l
        self.historico = Historico()

    #Métodos da conta
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.transacoes.append(f'Saque de {valor}')
            return True
        else:
            return False

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Depósido de {valor}')

    def ver_saldo(self):
        return f'Saldo: {self.saldo:.2f}'

    def transferir(self, valor, destino):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.transacoes.append(f'Tansferência de {valor} para '
                                             f'{destino}')
            destino.saldo += valor
            destino.historico.transacoes.append(f'Transferência de {valor} de'
                                                f' {self}')
            return True
        else:
            return False

        # if self.sacar(valor):
        #     destino.depositar(valor)
        #     return True
        # else:
        #     return False

    def __str__(self):
        return (f'Numero: {self.numero}|'
                f'Titular: {self.titular.nome}|'
                f'Saldo: {self.saldo} ')