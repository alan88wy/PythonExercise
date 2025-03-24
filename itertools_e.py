import itertools
from functools import reduce
from collections import defaultdict
from itertools import (
        accumulate,
        count,
        cycle,
        repeat, 
        islice,
        chain,
        tee,
        starmap,
        product,
        zip_longest
        )

data = (
    (1, 'abc'),
    (1, 'bcd'),
   
    (2, 'pyt'),
    (2, 'yth'),
    (2, 'tho'),
    
    (3, 'hon')
)

groups = list(itertools.groupby(data, key=lambda x: x[0]))

print(groups)

groups = itertools.groupby(data, key=lambda x: x[0])

for group in groups:
    print(group[0], list(group[1]))


# Count([start[, step]])
# itertools.count(start=0, step=1)
#
# Make an iterator that returns evenly spaced values beginning with start.

g = count(10)
print("Itertools count + islice -> ", list(islice(g, 5)))

# itertools.cycle(iterable)
#
# Make an iterator returning elements from the iterable and saving a copy of each. When the iterable is exhausted, return elements from the saved copy. Repeats indefinitely. Roughly equivalent to:


g = cycle(('red', 'green', 'blue'))
print(list(islice(g, 9)))

from collections import namedtuple
Card = namedtuple('Card', 'rank suit')

def card_deck():
    ranks = tuple(str(num) for num in range(2, 11)) + tuple('JQKA')
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    for suit in suits:
        for rank in ranks:
            yield Card(rank, suit)

hands = [list() for _ in range(4)]

hands_cycle = cycle(hands)

for card in card_deck():
    next(hands_cycle).append(card)


for hand in hands:
    [print(card) for card in hand]

# itertools.chain(*iterables)
#
# Make an iterator that returns elements from the first iterable until it is exhausted, then proceeds to the next iterable, until all of the iterables are exhausted. This combines multiple data sources into a single iterator.

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

print("\nchain -> \n")

for item in chain(l1, l2, l3):
    print(item)


# itertools.tee(iterable, n=2tee
#
# Return n independent iterators from a single iterable.

def squares(n):
    for i in range(n):
        yield i**2

gen = squares(10)
iters = tee(squares(10), 3)

print("\ntee -> \n")
print(iters)

# itertools.starmap(function, iterable)
#
# Make an iterator that computes the function using arguments obtained from the iterable. Used instead of map() when argument parameters have already been “pre-zipped” into tuples.
#
# The difference between map() and starmap() parallels the distinction between function(a,b) and function(*c). Roughly equivalent to:

# def starmap(function, iterable):
#     #starmap(pow, [(2,5), (3,2), (10,3)]) → 32 9 1000
#     for args in iterable:
#         yield function(*args)

def add(x, y):
    return x + y

print("\nstarmap -> \n")
[print(n) for n in list(starmap(add, [(0,0), (1,1), (2,2)]))]


# functools.reduce(function, iterable, [initial, ]/)
#
# Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). 

print("\nreduce -> ", reduce(lambda x, y: x*y, [1, 2, 3, 4]))

# itertools.accumulate(iterable[, function, *, initial=None])
#
# Make an iterator that returns accumulated sums or accumulated results from other binary functions.
# 
# The function defaults to addition. The function should accept two arguments, an accumulated total and a value from the iterable.
# 
# If an initial value is provided, the accumulation will start with that value and the output will have one more element than the input iterable.

print("\naccumulate -> ", list(accumulate([10, 20, 30])))

# itertools.zip_longest(*iterables, fillvalue=None)
# Make an iterator that aggregates elements from each of the iterables.
# 
# If the iterables are of uneven length, missing values are filled-in with fillvalue. If not specified, fillvalue defaults to None.
# 
# Iteration continues until the longest iterable is exhausted.

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4]
l3 = [1, 2, 3]

print("\nzip_longest -> ") 
[print(n) for n in list(zip_longest(l1, l2, l3, fillvalue='N/A'))]

# itertools.product(*iterables, repeat=1)
# 
# Cartesian product of the input iterables.
# 
# Roughly equivalent to nested for-loops in a generator expression. For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
# 
# The nested loops cycle like an odometer with the rightmost element advancing on every iteration. This pattern creates a lexicographic ordering so that if the input’s iterables are sorted, the product tuples are emitted in sorted order.
# 
# To compute the product of an iterable with itself, specify the number of repetitions with the optional repeat keyword argument. For example, product(A, repeat=4) means the same as product(A, A, A, A).

l1 = ['x1', 'x2', 'x3', 'x4']
l2 = ['y1', 'y2', 'y3']

print("\nproduct -> ") 
[print(n) for n in list(itertools.product(l1, l2))]

# example
def matrix(n):
    for i, j in product(range(1, n+1), range(1, n+1)):
        yield (i, j, i*j)

print("\nproduct example -> ") 
[print(n) for n in list(matrix(4))]

# itertools.takewhile(predicate, iterable)
#
# Make an iterator that returns elements from the iterable as long as the predicate is true. Roughly equivalent to:
#
# def takewhile(predicate, iterable):
#     # takewhile(lambda x: x<5, [1,4,6,3,8]) → 1 4
#     for x in iterable:
#         if not predicate(x):
#             break
#         yield x

def grid(min_val, max_val, step, *, num_dimensions=2):
    axis = itertools.takewhile(lambda x: x <= max_val,
                               itertools.count(min_val, step))
    
    # to handle multiple dimensions, we just need to repeat the axis that
    # many times - tee is perfect for that
    axes = itertools.tee(axis, num_dimensions)

    # and now we just need the product of all these iterables
    return itertools.product(*axes)

print("\nGrid -> ") 
[print(n) for n in list(grid(-1, 1, 0.5, num_dimensions=3))]




