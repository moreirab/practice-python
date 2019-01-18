# source: https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
import random

a = [random.randint(0, 1000) for x in range(0, random.randint(0, 100))]
b = [random.randint(0, 1000) for x in range(0, random.randint(0, 100))]
c = [list(set(a+b))]

print('Elements in a')
print(a)
print('Elements in b')
print(b)
print('Elements in c')
print(c)