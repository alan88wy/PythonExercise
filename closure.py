def adder(n):
    def inner(x):
        return x + n;

    return inner

add1 = adder(1)
add2 = adder(2)
add3 = adder(3)

print(add1(10))
print(add2(20))
print(add3(30))
print(add1(10))

# This will not work as n was only created when we first access it
# So, if we call adders[3](10), n will be fix to 3. All element
# in the adders list will have n = 3

def create_adders():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x: x + n)
    return adders

print("Wrong!")
adders = create_adders()
print(adders[3](10))
print(adders[0](10))
print("End Wrong!")

# This will work
def create_adders():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x, step=n: x + step)
    return adders

print("Correct!")
adders = create_adders()
print(adders[3](10))
print(adders[0](10))
print("End Correct!")

# Another example
def incrementer(n):
    def inner(start):
        current = start
        def inc():
            a = 10  # local var
            nonlocal current
            current += n
            return current
        return inc
    return inner

fn = incrementer(2) # n is set to 2. Falling gn will increment by 2

incr_2 = fn(100)    # start is set to 100
print(incr_2())
print(incr_2())

incr_3 = incrementer(3)(200)
print(incr_3())
print(incr_3())
