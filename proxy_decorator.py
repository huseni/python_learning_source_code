__author__ = 'kathiria'


class User(object):
    def __init__(self, roles):
        self.roles = roles


class Unauthorized(Exception):
    print("You are unauthorised")


def protect(role):
    def _protect(function):
        def __protect(*args, **kw):
            user = globals().get('user')
            if user is None or role not in user.roles:
                raise Unauthorized("I would not tell you")
            return function(*args, **kw)
        return __protect
    return _protect

#tarek = User(('admin','user'))
bill = User(('user',))


class MySecrets(object):
    @protect(object)
    def waffle_recipe(selfself):
        print ('Use tons of butter!')

#these_are = MySecrets()
#user = tarek
#these_are.waffle_recipe()



