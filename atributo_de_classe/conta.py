class Conta:
    _total_contas = 0   #Atributo de classe
    __slots__ = ['_numero', '_titular', '_saldo', '_limite']
    def __init__(self, n, c, s, l):
        self._numero = n     #Atributos de Instância
        self._titular = c
        self._saldo = s
        self._limite = l
        Conta._total_contas += 1  #Incrementa quando cria uma instâncias

    #Metodo de Instância
    def get_total_contas(self):
        return Conta._total_contas

    # Metodo Estatico
    @staticmethod
    def get_total_contas_estatico():
        return Conta._total_contas

    #Metodo de classe
    @classmethod
    def get_total_contas_classe(cls):
        return Conta._total_contas

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