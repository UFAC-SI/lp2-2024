from mixin_interface.autenticavel import AutenticavelInterface
from mixin_interface.cliente import Cliente
from mixin_interface.diretor import Diretor
from mixin_interface.login import Login
from mixin_interface.presidente import Presidente

d1 = Diretor()
c1 = Cliente()
p1 = Presidente()

AutenticavelInterface.register(Presidente)

login = Login()
login.logar(d1)
login.logar(c1)
login.logar(p1)
