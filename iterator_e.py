# In order to be able to use this class as an iterator
# object, you user __iter__ to return itself and
# use __next__ to iterate over the object

class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result


sq = Squares(10)

print("Using next(sq) -> ")
print(next(sq))
print(next(sq))
print(next(sq))

print("Using for loop : ")

sq = Squares(10)

for item in sq:
    print(item)

sq = Squares(10)
print("List : -> ", [item for item in sq if item %2 ==0])


sq = Squares(10)
print("Enumerator : -> ", list(enumerate(sq)))


# How the above still needs you to recreate the object 
# when it reached the end
#
# Let's try another way

class Cities:
    def __init__(self, cities):
        self._cities = cities

    def __getitem__(self, s):
        return self._cities[s]

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        return self.CityIterator(self)


    class CityIterator:
        def __init__(self, city_obj):
            self._city_obj = city_obj
            self.index = 0
    
        def __iter__(self):
            return self
    
        def __next__(self):
            if self.index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self.index]
                self.index += 1
                return item
    

cities = Cities(['New York', 'Newark', 'New Delhi', 'Newcastle'])

for city in cities:
    print(city)

print("\nAgain ...\n")

for city in cities:
    print(city)

print("\nList ....\n")
print(list(enumerate(cities)))

print('\nSorted in reverse ...\n')
cities = sorted(cities, reverse=True)
print(cities)

print('\nPrint first item ...\n')
print(cities[0])
