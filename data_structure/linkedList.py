class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node
    
    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d
    

class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def push(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def insertAfter(self, prev_n, data):
        if prev_n is None:
            print('The target node is not in the linked list')
            return
        new_node = Node(data)
        new_node.set_next(prev_n.get_next())
        prev_n.set_next(new_node)

    def append(self, d):
        new_node = Node(d)
        if self.root is None and self.size == 0:
            self.root = new_node
            self.size += 1
            return
        last_node = self.root
        while last_node.get_next():
            last_node = last_node.get_next()
        last_node.set_next(new_node)


    def push_node(self, n):
        n.set_next(self.root)
        self.root = n
        self.size += 1

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return this_node
            else:
                this_node = this_node.get_next()
        return None

    def print_list(self):
        this_node = self.root
        while this_node:
            print(this_node.get_data())
            this_node = this_node.get_next()


myList = LinkedList()
for i in range(11):
    myList.append(i)
print(myList.remove(8))
# print(myList.find(5))
myList.insertAfter(myList.find(4), 50)
myList.print_list()