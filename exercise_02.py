# source: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
from utils import input_number
num = input_number('Give me a number and I\'ll say whether this is an odd or even number:')
if num%2==0:
    print('This number is even!')
else:
    print('This number is odd!')