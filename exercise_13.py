# source: https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
from utils import input_number

input_num = input_number('How many numbers do you wish to yeild the Fibonacci numbers?')
num0 = 0
num1 = 1
numbers = [num0, num1]

for i in range(1, input_num):
    num = num0 + num1
    numbers.append(num)
    num0 = num1
    num1 = num

print('List of {} Fibonacci numbers!'.format(input_num))
print(numbers)