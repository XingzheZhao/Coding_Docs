class MinHeap:
    def __init__(self):
        self.heap = []

    def has_parent(self, i):
        if i == 0:
            return False
        else:
            return True
    
    def get_parent(self, i):
        pass

# ? [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ?           1
# ?       2        3
# ?    4    5    6   7
# ?  8   9