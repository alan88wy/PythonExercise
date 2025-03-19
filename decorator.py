from functools import wraps # Use this so that we can get the parameter info


def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))
        return fn(*args, **kwargs)

    return inner


@counter
def adder(a: int, b: int=10) -> int:
    """
    returns sum of two integers
    """
    return a + b

help(adder)

print("Add 1+2 -> ", adder(1,2))
print("Add 5+2 -> ", adder(5,2))
