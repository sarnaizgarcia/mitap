from model.user import User

class UserController(object):
    pass
    def choose(self, number):
        if number == 1:
            self._log_in()
        else:
            self._sign_in()

    def _log_in(self):
        print('estoy en el LOG in')
    
    def _sign_in(self):
        print('estoy en el SIGN in')