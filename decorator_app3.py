# Decorators Application (Memoization)

from functools import wraps

def memoize_fib(fn):
    cache = dict()
    
    @wraps(fn)
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    
    return inner

@memoize_fib
def fib(n):
    print ('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print("fib(3) :")
print("Result :", fib(3))
print("fib(10) :")
print("Result :", fib(10))
print("fib(6) :")
print("Result :", fib(6))

# Generic Memoization
def memoize(fn):
    cache = dict()
    
    @wraps(fn)
    def inner(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    
    return inner

@memoize
def fib(n):
    print ('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print("fib(3) :")
print("Result :", fib(3))
print("fib(10) :")
print("Result :", fib(10))
print("fib(6) :")
print("Result :", fib(6))

@memoize
def fact(n):
    print('Calculating {0}!'.format(n))
    return 1 if n < 2 else n * fact(n - 1)

print("fact(5) : ")
print("Result :", fact(5))
print("fact(7) : ")
print("Result :", fact(7))
print("fact(3) :")
print("Result :", fact(3))

# Using built-in memoization decorator = lru_cache
from functools import lru_cache

print("Using lru_cache :")

# Default 128 but we can change that @lru_cache(maxsize=8)
@lru_cache()  
def fact(n):
    print('Calculating {0}!'.format(n))
    return 1 if n < 2 else n * fact(n - 1)

print("fact(5) : ")
print("Result :", fact(5))
print("fact(7) : ")
print("Result :", fact(7))
print("fact(3) :")
print("Result :", fact(3))
