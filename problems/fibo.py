# stantdard

a = 0
b = 1
for i in range(0, 10):
    print(a)
    a, b = b, a+b
    # temp = a
    # a = b
    # b = temp + b