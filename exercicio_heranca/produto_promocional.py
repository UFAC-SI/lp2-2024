from produto import Produto
class ProdutoPromocional(Produto):
    def definir_preco_venda(self, lucro):
        margem = self._preco_compra * lucro
        parcial = (margem + self._preco_compra)
        self._preco_venda = parcial - (parcial * 0.2)
