from controller.user import UserController

class UserView(object):
    def show_welcome(self):
        selection = int(input('Bienvenido. Presiona 1 para logearte o presiona 2 si no tienes cuenta '))
        if selection == 1:
            self._log_in()
        else:
            self._sign_in()

    def _log_in(self):
        print('estoy en el LOG in')
    

    def _sign_in(self):
        print('estoy en el SIGN in')
