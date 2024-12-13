from decimal import Decimal
v1 = 0.1
v2 = 0.2
soma = v1 + v2
print(f'{soma}')
#O que aconteceu aqui?
#Soma com a precisão correta.
#Usa a classe Decimal
v3 = Decimal('0.1')
v4 = Decimal('0.2')
somaDecimal = v3 + v4
print(f'{somaDecimal}')
