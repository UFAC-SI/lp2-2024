class Produto:

    _historico = [] #Atributo de classe

    def __init__(self, nome, preco_compra=0, qtde=0):
        self._nome = nome
        self._preco_compra = preco_compra
        self._qtde = qtde
        self._preco_venda = 0

    def definir_preco_venda(self, lucro=0.4):#0.4
        margem = self._preco_compra * lucro
        self._preco_venda = self.preco_compra + margem

    def vender_produto(self, qtde=1):
        try:
            if self._qtde >= qtde:
                self._qtde -= qtde
                Produto._historico.append(f'{qtde} '
                                          f'unidade(s) do '
                                          f'produto {self._nome}'
                                          f' vendido(s) por '
                                          f'{self._preco_venda}. '
                                          f'Total: '
                                          f'{qtde*self._preco_venda}')
            else:
                raise ValueError('Quantidade não disponível no estoque.')
        except ValueError as e:
            pass


    def comprar_produto(self, qtde, preco):
        self.qtde = self.qtde + qtde #Metodos gettter e setter funcionando na mesma linha
        self.preco_compra = preco #O metodo setter do atributo preco_compra
        self.definir_preco_venda()
        Produto._historico.append(f'{qtde} '
                                  f'unidade(s) do '
                                  f'produto {self._nome}'
                                  f' comprados(s) por '
                                  f'{preco}. '
                                  f'Total: '
                                  f'{qtde * preco}')

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def preco_compra(self):
        return self._preco_compra

    @preco_compra.setter
    def preco_compra(self, valor):
        self._preco_compra = valor

    @property
    def qtde(self):
        return self._qtde

    @qtde.setter
    def qtde(self, valor):
        self._qtde = valor
