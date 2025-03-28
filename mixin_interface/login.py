class Login:
    def logar(self, autenticavel):
        try:
            autenticavel.autenticar()
        except Exception as e:
            print('Objeto não autenticável')