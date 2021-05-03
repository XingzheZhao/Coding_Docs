x = 'hello world this is sam'

s =x.upper().replace(' ', '')
print(s)

new_str = ""
for i in x:
    if i.isspace():
        pass
    else:
        new_str = new_str + i
print(new_str)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.chords = (self.x, self.y)

    def __str__(self):
        return '(' + str(self.x) +', ' + str(self.y) + ')'

    def __add__(self, p):
        return Point(self.x+p.x, self.y+p.y)

    def length(self): # ! or __len__
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, p):
        return self.length() < p.length()

    def __le__(self, p):
        return self.length() <= p.length()

    def __eq__(self, p):
        return self.length() == p.length()

a = Point(1,2)
b = Point(4,6)
print(a < b)

c = a+b
print(c)
print(5>4)