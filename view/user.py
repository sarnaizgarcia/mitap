from controller.user import UserController

user_controller = UserController()
class UserView(object):
    def __init__(self, user_controller):
        self.user_controller = user_controller
        
    def show_welcome(self):
        selection = int(input('Bienvenido. Presiona 1 para logearte o presiona 2 si no tienes cuenta '))
        user_controller.choose(selection)

