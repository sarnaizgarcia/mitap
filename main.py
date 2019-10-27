from view.user import UserView
from controller.user import UserController
from model.user import User

import json

user = User(json)
user_controller = UserController(user)
user_view = UserView(user_controller)


def main(user_view):
    user_view.show_welcome()


main(user_view)
