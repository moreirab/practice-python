# source: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
from exercise_04 import check_divisors
input_num = 0

print('Input a number and I\'ll show you whether this is a prime number or not!')
try:
    input_num = int(input())
    if input_num == 0 or input_num == 1:
        raise ValueError
    is_prime = len(check_divisors(input_num)) == 0
    if is_prime:
        print('This number is prime!')
    else:
        print('This number is not prime!')

except ValueError:
    print('You should input a valid number!')