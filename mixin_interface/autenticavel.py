import abc
class AutenticavelInterface(abc.ABC):
    """
    Esta interface obriga a implementação do método abstrato
    """
    @abc.abstractmethod
    def autenticar(self):
        """Este método define a autenticação
        """
        pass