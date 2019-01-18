# source: https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
from utils import random_list

def list_ends():
    a = random_list(200, 10000)
    print('List elements')
    print(a)
    print('First and last elements')
    return [a[0], a[-1]]

print(list_ends())
