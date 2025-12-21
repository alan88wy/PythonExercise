f = lambda x,y=10: (x**2 + y)
a = f(30,2)
print(a)
b=f(10)
print(b)

f2 = lambda x,*args, y, **kwargs: (x, *args, y, {**kwargs})

c = f2(1, 'a','b', y=200, a=20, b=200)
print(c)

def fun(fn, x):
    return fn(x)

f = lambda x: x**2

r = fun(f, 3)
print(r)

def fun2(f,x,*args, y, **kwargs):
    return f(x, *args, y=y, **kwargs)

b = fun2(f2, 1, 'a','b', y=200, a=20, b=200)
print(b)

# Sorted list - as upper
l = ['a', '3', 'z', '10', '2', 'r']
ls = sorted(l, key=str.upper)

print("ls : ", ls)

ls2 = sorted(l, key = lambda s: s.upper())
print("ls2 : ", ls2)

# Sorted list randomly
import random
f3=lambda x: random.random()
ol = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ol3 = sorted(ol, key=f3)
print(ol3)
