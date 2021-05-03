class ComplexNumber:
    def __init__(self, real, imagine):
        self.real= real
        self.imagine = imagine

    def __str__(self):
        if self.imagine < 0:
            if self.real == 0:
                return '-' + str(abs(self.imagine)) + 'i'
            else:
                return str(self.real) + '-' + str(abs(self.imagine)) + 'i'
        elif self.imagine == 0:
            if self.real == 0:
                return str(0)
            else:
                return str(self.real)
        else:
            if self.real == 0:
                return str(self.imagine)
            else:
                return str(self.real) + '+' + str(self.imagine) + 'i'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imagine + other.imagine)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imagine - other.imagine)

    # ? (a + bi) * (c + di)
    # ? ac + adi + bci + bdi^2
    # ? ac - bd + (ad + bc) i
    def __mul__(self, other):
        real_num = self.real * other.real - self.imagine * other.imagine
        imagine_num = self.real * other.imagine + self.imagine * other.real
        return ComplexNumber(real_num, imagine_num)

a = ComplexNumber(4,6)
b = ComplexNumber(4,-6)
c = ComplexNumber(0,-8)
d = ComplexNumber(0,0)
e = ComplexNumber(-9,0)

print(a, b, c, d, e, sep='\n')

print('Operations')
print(a+b)
print(c+e)
print(a-b)

f = ComplexNumber(2, -3)
g = ComplexNumber(-3, -5)
print(f*g)