class DecClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print('DecClass instance called: a= (0), b = {1}'.format(self.a, self.b))
            return fn(*args, **kwargs)

        return inner


@DecClass(10, 20)
def my_func(s):
    print('Hello {0}'.format(s))


my_func('Python')
