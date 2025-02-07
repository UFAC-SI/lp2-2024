class Produto:
    _desconto = 0
    def __init__(self, nome, preco):
        if Produto.validar_preco(preco):
            self._nome = nome
            self._preco = preco

    @property
    def preco(self):
        return self._preco

    @classmethod
    def atualizar_desconto(cls, valor):
        Produto._desconto = valor

    @staticmethod
    def validar_preco(preco):
        if preco < 0:
            raise ValueError('Não pode ser negativo.')
        else:
            return True

    def calcular_preco_com_desconto(self):
        return self._preco - (Produto._desconto/100 * self._preco)