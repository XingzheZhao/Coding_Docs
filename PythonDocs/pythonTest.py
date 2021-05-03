from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'major'])

s = Student('Sam', '30', 'CMPE')

print(s.name)

import sys

a = 2
b = '2'
print(sys.getsizeof(a))
print(sys.getsizeof(b))