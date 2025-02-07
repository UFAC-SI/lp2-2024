from produto import Produto
p1 = Produto('Carro', -100000)
try:
    if p1.validar_preco(p1.preco):
        print('preco válido')
except ValueError as e:
    print(e)

Produto.atualizar_desconto(10)
print(p1.calcular_preco_com_desconto())
