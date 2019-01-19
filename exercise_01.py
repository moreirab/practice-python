# source: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
from utils import input_number
from datetime import date

print('Give me your name:')
name = input()
age = input_number('Give me your age:')
print(date.today().year - age)
year = (date.today().year - age) + 100
print('{}, you\'ll turn 100 years old in {}.'.format(name, year))