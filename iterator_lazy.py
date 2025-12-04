def fib(n):
    fib_0 = 1
    fib_1 = 1
    for i in range(n-1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1

class Fib:
    def __init__(self, n):
        self.n = n
        
    def __iter__(self):
        return self.FibIter(self.n)

    class FibIter:
        def __init__(self, n):
            self.n = n
            self.i = 0
         
        def __iter__(self):
            return self
     
        def __next__(self):
            if self.i >= self.n:
                raise StopIteration
            else:
                result = fib(self.i)
                self.i += 1
                return result

fib_iterable = Fib(7)

for num in fib_iterable:
    print(num)
