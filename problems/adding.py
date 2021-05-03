
code1 = '''
def sum1(n=100):
    result = 0

    for i in range(n+1):
        result += i

    return result
'''

code2 = '''
def sum2(n=100):
    result = 0
    
    mul = n // 2
    if n % 2 == 0:
        return mul * (n+1)
    else:
        return mul * (n+1) + (n+1) // 2
'''


def sum1(n):
    result = 0

    for i in range(n+1):
        result += i

    return result

code3 = '''
def sum3(n=100):
    return (n*(n+1)) / 2
'''

def sum2(n):
    result = 0
    
    mul = n // 2
    if n % 2 == 0:
        return mul * (n+1)
    else:
        return mul * (n+1) + (n+1) // 2

print(sum1(5))
print(sum2(5))
# 1, 2, 3
# 1, 2, 3, 4, 5
# 1, 2, 3, 4, 5, 6, 7
# 1, 2, 3, 4, 5, 6, 7, 8, 9
import timeit
print(timeit.timeit(stmt=code1, number=1000))
print(timeit.timeit(stmt=code3, number=1000))