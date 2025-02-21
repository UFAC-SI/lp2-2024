from produto import Produto
from produto_parcelado import ProdutoParcelado
from produto_promocional import ProdutoPromocional
from liquidacao import Liquidacao
parcelado = ProdutoParcelado('Café', 100, 10)
promocional = ProdutoPromocional('Morango', 10, 10)
parcelado.definir_preco_venda(0.5)
promocional.definir_preco_venda(0.5)
parcelado.vender_produto()
promocional.vender_produto()


for p in Produto._historico:
    print(p)

liqui = Liquidacao()
liqui.registrar(promocional)

for l in liqui._historico:
    print(l)