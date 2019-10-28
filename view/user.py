class UserView(object):
    def __init__(self, user_controller):
        self.user_controller = user_controller

    def show_welcome(self):
        selection = int(input(
            'Bienvenido, presiona 1 para logearte, si no tienes cuenta presiona 2 >  '))
        self.user_controller.choose(selection)
