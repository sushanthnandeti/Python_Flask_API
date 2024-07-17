import functools

user = {"username" : "sushanth", "access_level" : "admin"}


def make_secure(func):
    @functools.wraps(func)  #This inbuilt python function keeps the name of the original passing function instead of overwriting it with the decorators name
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            print("User does not have admin access.")

    return secure_function


@make_secure
def get_admin_password():
    return 'lol123'


print(get_admin_password)
print(get_admin_password.__name__)