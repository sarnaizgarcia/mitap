class UserController(object):
    def __init__(self, user):
        self.user = user

    def choose(self, number):
        if number == 1:
            self.user.log_in()
        else:
            self.user.sign_in()
