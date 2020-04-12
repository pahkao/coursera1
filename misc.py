import openpyxl as xl
#import sys
#print(sys.path)

import math

print(math.e)

x = 'Hello world'
#print(dir(x))
y = x.rfind('w')
print(y)

x = 'From marquard@uct.ac.za'
print(x[8])

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

# Traceback error: TypeError: 'str' object does not support item assignment
# fruit = 'Banana'
# fruit[0] = 'b'
# print(fruit)

#list = [0, 1, 2, 3, 4]
y = list(range(5))
print(y)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))


stuff = dict()
print(stuff.get('candy',-1))

x = 194 % 5
print(x)

a = 10
b = 12
a, b = 'lol', 'kek'
print(a, b)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])


# ищет в листе элементы только с буквами
import re
pattern = re.compile(".[0-9].")
A = ['m24534', 'hello', '13000']
B = [a for a in A if not pattern.match(a)]

print(B)


s=["pune", "mumbai", "delhi"]

x = [(w.upper(), len(w)) for w in s]

print(x)

import math
z = [str(round(math.pi)) for i in range (1, 6)]
print(z)
