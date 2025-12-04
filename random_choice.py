import random
from functools import reduce

# Random choices
l = [10, 20, 30, 40, 50, 60]
random_index = random.randrange(len(l))
print("Random Index {0}: {1}".format(random_index, l[random_index]))

print("Random Choice : {0}".format(random.choice(l)))

print("Using range in ramdom.choices ->")

l2 = list(range(1000))

print("random.choices(l2, k = 5) -> ", random.choices(l2, k = 5))

# Random.choices with weight
#
# random.choices(population, weights=None, cum_weights=None, k=1)
#
# Parameters
#
# population: It is is sequence or data structure from which you want to choose data.
# weights or cum_weights: Define the selection probability for each element.
# weights: If a weights sequence is specified, random selections are made according to the relative weights.
# cum_weights: Alternatively, if a cum_weights sequence is given, the random selections are made according to the cumulative weights.
# k: The number of samples you want from a population.
#
# Note: You cannot specify both weights and cum_weights at the same time.

l = ['a', 'b', 'c', 'd', 'e']
weights=[5, 15, 25, 35, 50]

# Example, I will give weight to this
#
# a = 10
# b = 40
# c = 5
# d = 35
# e = 25
# 
# Which give b higher changes being selected, follow by d
#

for i in range(5):
    print('iter {0} of random.choices(l, weights=(10, 40, 5, 35, 25), k=3) -> {1}'.format(i, random.choices(l, weights=weights, k=5)))

weight = reduce(lambda a,b: a + b, weights) 
for i in weights:
    prob = i/weight
    print('{0} has probability of {1}'.format(i, prob))

for i in range(5):
    print('iter {0} of random.choices(l, cum_weights=(10, 40, 5, 35, 25), k=3) -> {1}'.format(i, random.choices(l, cum_weights=weights, k=5)))



