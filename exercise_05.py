# source: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
from utils import random_list

a = random_list(50, 50)
print('List a:')
print(sorted(a))

b = random_list(50, 50)
print('List b:')
print(sorted(b))

c = [x for x in set(a+b) if x in a and x in b]
print('List c:')
print(sorted(c))
