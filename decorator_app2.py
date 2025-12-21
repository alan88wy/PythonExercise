def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone
    
    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called at {1}'.format(fn.__name__, run_dt))
        return result
        
    return inner

def timed(fn):
    from functools import wraps
    from time import perf_counter
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print('{0} ran for {1:.6f}s'.format(fn.__name__, end-start))
        return result
    
    return inner

@timed
@logged
def func_1():
    pass

@timed
@logged
def factorial(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))

func_1()
factorial(1000)
