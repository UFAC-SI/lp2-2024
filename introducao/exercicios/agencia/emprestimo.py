class Emprestimo:
    def __init__(self, conta, valor, parcelas):
        self.valor = valor
        self.parcelas = parcelas
        self.valor_parcela = valor/parcelas
        self.parcelas_restantes = parcelas
        self.conta = conta
        conta.depositar(valor)
        conta.adicionar_emprestimo(self)

    #pagar uma parcela
    def pagar_parcela(self):
        if self.parcelas_restantes > 0:
            if self.conta.saldo >= self.valor_parcela:
                self.conta.sacar(self.valor_parcela)
                self.parcelas_restantes -= 1
                print(f'Pagou a parcela: {self.parcelas-self.parcelas_restantes}, valor: {self.valor_parcela}')
                print(f'Faltam {self.parcelas_restantes} parcelas.')
            else:
                print('Saldo insuficente, parcela não paga.')
        else:
            print('Emprestimo pago.')
