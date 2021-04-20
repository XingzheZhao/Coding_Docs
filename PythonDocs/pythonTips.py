num1 = 1_000_000
num2 = 3_000_000_000

total = num1 + num2

print(f'{total:,}')  # ? seperators


names = ['Sam', 'Tony', 'David']

for index, name in enumerate(names):
    print(index, name, sep='\t')

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman', 'Ironman']

for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')


# ? unpacking values

# a, _ = (1, 2)

a, b, *c = (1, 2, 3, 4, 5)
# a, b, *_ = (1, 2, 3, 4, 5)
# a, b, *c, d = (1,2,3,4,5,6,7)

print(a)
print(b)
print(tuple(c))

# ? set and get attribute

class Person():
    pass

person = Person()
first_key = 'first'
first_val = 'Sam'

setattr(person, first_key, first_val)
print(person.first)

first = getattr(person, first_key)
print(first)

person2 = Person()
person2_info = {'first': 'Sam', 'last': 'Zhao'}

for key, value in person2_info.items():
    setattr(person2, key, value)

for key in person2_info.keys():
    print(getattr(person2, key), end=' ')

# ? hide user infomation while logging in

from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')
print('Logging in...')