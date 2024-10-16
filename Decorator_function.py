class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

# Decorator to check authentication before running function
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):    # This is the on way to pass parameter to wraooer function
        if args[0].is_logged_in:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Alan")
new_user.is_logged_in = True    # By setting to True, create_blog_post will be run
create_blog_post(new_user)