class Conta:
    def __init__(self, n, c, s, l):
        self._numero = n
        self._titular = c
        self._saldo = s
        self._limite = l

    #Forma Pytonica
    @property
    def saldo(self):
        return self._saldo


    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor
        
    #Conveção padrão para getters e setters
    def get_saldo(self):
        return self._saldo

    #Esse método não faz sentido pois temos sacar e depositar
    def set_saldo(self, valor):
        self._saldo = valor

    #sacar
    #depositar