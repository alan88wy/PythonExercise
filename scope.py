a = 10

def my_func(n):
    a = 1 # local variable for this function
    print("Inside function1")
    print(a)
    a = a + n
    print(a)
    return a

def my_func2(n):
    global a  # Global variable. My be declare before this function
    print("Inside function2")
    print(a)
    a = a + n
    print(a)
    return a

print("outside function")
print(a)

my_func(3)

print("outside function")
print(a)

my_func2(3)

print("outside function")
print(a)

# Functions defined inside anther function can reference variables 
# from that enclosing scope, just like functions can reference 
# variables from the global scope.

def outer_func():
    x = "Hello"

    def inner_func():
        x = "Hello World!"
        print("Inside function -> ", x)

    inner_func()
    print("Outside Function -> ", x)   # X will not change unless you declare nonlocal x


outer_func()

# You can change x if you declare x as nonlocal

y = "Hello Python"

def outer_func():
    x = "Hello"

    def inner_func():
        global y
        nonlocal x
        x = "Hello World!"
        y = "Hello World!"
        print("Using nonlocal inside function -> ", x)

    inner_func()
    print("Outside Function -> ", x)   # X will not change unless you declare nonlocal x

print("y before calling function -> ", y)
outer_func()
print("y after calling function -> ", y)

