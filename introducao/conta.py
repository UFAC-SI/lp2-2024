class Conta:
    def __init__(self, n, t, s, l): #Metodo de inicialização
        self.numero = n             #Atributos de instância
        self.titular = t
        self.saldo = s
        self.limite = l
    #Métodos da conta
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor):
        self.saldo += valor

    def ver_saldo(self):
        return f'Saldo: {self.saldo:.2f}'

    def transferir(self, valor, destino):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        else:
            return False

    def __str__(self):
        return f'Numero: {self.numero} Saldo: {self.saldo}'