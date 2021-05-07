from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'major'])

s = Student('Sam', '30', 'CMPE')

print(s.name)

import sys

a = 2
b = '2'
print(sys.getsizeof(a))
print(sys.getsizeof(b))

hashT = {}
hashT[1] = 1
hashT[2] = 1
print(hashT)

ls = [1,2,3,4]
t = [5]
print(ls+t)
print(t+ls)

for i in range(9, -1, -1):
    print(i)

s = 'ABCDEDF'
for index, value in enumerate(s):
    print(index, value)