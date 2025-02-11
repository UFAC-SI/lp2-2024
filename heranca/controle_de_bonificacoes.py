from funcionario import Funcionario
class ControleDeBonificacoes:
    def __init__(self, total = 0):
        self._total = total

    def registra(self, funcionario):
        #if hasattr(funcionario, 'get_bonificacao'):
        # if isinstance(funcionario, Funcionario):
        #     self._total += funcionario.get_bonificacao()
        # else:
        #     print('Referência não tem bonificação!')
        try:
            self._total += funcionario.get_bonificacao()
        except AttributeError as e:
            print('Referência não tem bonificação!')

    def get_total(self):
        return self._total