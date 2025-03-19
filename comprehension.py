# map
# Syntax: map(func, list)

def fact(n):
    return 1 if n < 2 else n * fact(n- 1)

print(fact(3))

# Example 1 : create a map from a list using fact

mf = map(fact, [1,2,3,4,5,6])

print(list(mf))

# Example 2 : Adding two list
l1 = [1,2,3,4,5,6]
l2 = [10, 20, 30, 40, 50, 60, 70]

f = lambda x, y : x + y

ma = map(f, l1, l2)
print(list(ma))

# Filter
#
# The filter function is a function that filters an iterable based 
# on the truthyness of the elements, or the truthyness of the 
# elements after applying a function to them. Like the map function,
# the filter function returns an iterable that we can view by 
# generating a list from it, or simply enumerating in a for loop.


# Example 1: Note that since 0 is falsy, it will not be display

l1 = [0, 1,2,3,4,5,6]

print("List of truthyness : \n")

for e in filter(None, l1):
    print(e)
    
# Example 2: Even no

def is_even(n):
    return n % 2 == 0

l1 = [1,2,3,4,5,6,7,8,9]

r = filter(is_even, l1)
print("Even no : ", list(r))

# List Comprehension

l1 = [1,2,3,4,5,6,7,8,9]
r = [i for i in l1 if i % 2 ==0]

print("Even No : ", r)

r = [i**2 for i in l1]

print("Expo no : ", list(r))

# ZIP
#
# The zip built-in function will take one or more iterables, 
# and generate an iterable of tuples where each tuple contains 
# one element from each iterable:

l1 = 1,2, 3
l2 = 'a', 'b', 'c'

print("Zip : ", list(zip(l1, l2)))


