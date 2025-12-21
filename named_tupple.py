from collections import namedtuple

Point2D = namedtuple('Point2D', ('x','y'))

pt = Point2D(20, 30)

print(pt)

data_dict = dict(key1=100, key2=200, key3=300)
Data = namedtuple('Data', data_dict.keys())

print(Data._fields)

d1 = Data(**data_dict)
print(d1)
