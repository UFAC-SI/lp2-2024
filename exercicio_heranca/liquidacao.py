class Liquidacao:
    _historico = []
    def registrar(self, produto):
        produto.vender_produto()
        liquidacao = produto._preco_venda * 0.5
        preco = produto._preco_venda - liquidacao
        Liquidacao._historico.append(
            f'Produto {produto._nome} vendido na liquidação por {preco}: '
        )