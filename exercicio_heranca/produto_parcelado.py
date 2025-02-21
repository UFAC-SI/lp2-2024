from produto import Produto
class ProdutoParcelado(Produto):
    def definir_preco_venda(self, lucro):
        margem = self._preco_compra * lucro * 1.05
        self._preco_venda = self._preco_compra + margem
