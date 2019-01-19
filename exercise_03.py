# source: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
from utils import random_list, input_number
a = random_list(100, 100)
num = input_number('Give me a number and I\'ll print a list of numbers that are smaller than that given number:')
print('Original list:')
print(a)
print('Numbers that are smaller than {}:'.format(num))
print([x for x in a if x < num])