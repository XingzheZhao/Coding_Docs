
myList = [1,2,3,4,5]

myList.pop(0)
print(myList)

from collections import deque

myList2 = deque()

myList2.append(1)
myList2.append(2)
myList2.append(3)
myList2.popleft()
print(myList2)


from queue import Queue

myList3 = Queue(maxsize=5)

print(myList3.qsize())

myList3.put('a')
myList3.put('b')
myList3.put('c')

print(f'Is myList3 full or not: {myList3.full()}')

myList3.get()
print(myList3)
print(myList3)