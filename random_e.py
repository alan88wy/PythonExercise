import random
from functools import reduce

# Random.seed is use to reset the seed
# This can help use to reproduce the same repeatable numbers

random.seed(0)
for _ in range(10):
    print(random.randint(10,20), random.random())

print ("******************")

random.seed(0)
for _ in range(10):
    print(random.randint(10,20), random.random())

# Random choices
l = [10, 20, 30, 40, 50, 60]
random_index = random.randrange(len(l))
print("Random Index {0}: {1}".format(random_index, l[random_index]))

print("Random Choice : {0}".format(random.choice(l)))

print("Using range in ramdom.choices ->")

l2 = list(range(1000))

print("random.choices(l2, k = 5) -> ", random.choices(l2, k = 5))

