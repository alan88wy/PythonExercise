from functools import reduce

l1 = [1,2,3,4,5,6]


# Get Max number
r = reduce(lambda a, b: a if a > b else b, l1)
print("Max    : ", r)
print("Max(f) : ", max(l1))

# Get Min number
r = reduce(lambda a, b: a if a < b else b, l1)
print("Min    : ", r)
print("Min(f) : ", min(l1))

# Get add all number
r = reduce(lambda a, b: a + b, l1)
print("Sum    : ", r)
print("Sum(f) : ", sum(l1))

# Get product of all number
r = reduce(lambda a, b: a * b, l1)
print("Product: ", r)

n = 5

def fact(n):
    if n < 1:
        return 1 
    else:
        return n * fact(n - 1)

l1 = [fact(i) for i in range(1, n + 1)]

print("Fact : ", l1)

