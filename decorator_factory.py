def dec_factory():
    print("Running dec factory")

    def dec(fn):
        print("running dec") 
        def inner(*args, **kwargs): 
            print("Running Inner")
            return fn(*args, **kwargs)

        return inner
    return dec

@dec_factory()
def add(a, b):
    print("{0} + {1} = {2}".format(a, b, a + b))
    return a + b

add(1,3)

from functools import wraps

def timed(num_reps=1):
    def decorator(fn):
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / num_reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                            num_reps))
            return result
        return inner
    return decorator

def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-1) + calc_fib_recurse(n-2)

@timed(5)
def fib(n):
    return calc_fib_recurse(n)

fib(30)

