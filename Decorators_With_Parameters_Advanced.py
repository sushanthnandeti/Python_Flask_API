import functools

user = {"username" : "sushanth", "access_level" : "admin"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)  #This inbuilt python function keeps the name of the original passing function instead of overwriting it with the decorators name
        def secure_function(*args, ** kwargs):
            if user["access_level"] == access_level:
                return func(*args, ** kwargs)
            else:
                print("User does not have admin access.")

        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return 'admin: admin password'

@make_secure("user")
def get_user_password():
    return 'user : user password'


result = get_admin_password()
print(result)
