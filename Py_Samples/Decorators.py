import functools

user = {"username" : "sushanth", "access_level" : "admin"}


def make_secure(func):
    @functools.wraps(func)  #This inbuilt python function keeps the name of the original passing function instead of overwriting it with the decorators name
    def secure_function(*args, ** kwargs):
        if user["access_level"] == "admin":
            return func(*args, ** kwargs)
        else:
            print("User does not have admin access.")

    return secure_function


@make_secure
def get_admin_password(panel):
    if panel == 'admin':
        return 'lol123'
    elif panel == 'billing':
        return 'Secure Password'


print(get_admin_password)
print(get_admin_password.__name__)