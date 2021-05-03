class Customer:
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership

    def __str__(self):
        return self.name + ' ' + self.membership
    
    __repr__ = __str__


customers = [Customer('Sam', 'Gold'),
            Customer('Johnny', 'Premium')]

print(customers)