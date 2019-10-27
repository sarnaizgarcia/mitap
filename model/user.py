from customerrors.user import PasswordsNotEqual


class User(object):
    def __init__(self, json):
        self.json = json

    def log_in(self):
        print('estoy en el log in')

    def sign_in(self):
        print('Has elegido registrarte')
        username = input('Elige un nombre de usuario> ')
        password = input('Elige una contraseña')
        second_pass = input('Repite la contraseña')
        try:
            self._check_pass(password, second_pass)
        except PasswordsNotEqual:
            print('Las contraseñas no coinciden')
            self.sign_in()
        self._register_user(username, password)

    def _check_pass(self, first, second):
        if first != second:
            raise PasswordsNotEqual

    def _register_user(self, username, password):
        with open('./persistence/users.json', 'a+') as file:
            persistence = self.json.load(file)
