import random
from functools import reduce
from collections import Counter

# Random sample

l = range(100)

random.seed(0)
print('random.sample(l, k=10) -> ', random.sample(l, k=10))

print('with random.seed(0) -> ')
random.seed(0)
print('random.sample(l, k=10) -> ', random.sample(l, k=10))

suits = 'C', 'D', 'H', 'A'
ranks = tuple(range(2,11)) + tuple('JQKA')

deck = [str(rank) + suit for suit in suits for rank in ranks]

print('Counter(random.sample(deck, k = 20)) ->',
Counter(random.sample(deck, k = 20)))
