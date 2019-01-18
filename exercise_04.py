# source: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

def divisors(num):
    return [x for x in range(2, num) if num%x==0]

print('Input a number and I\'ll show you all their divisors (if there\'re any)!')
num = 0
try:
    num = int(input(''))
    print(divisors(num))
except ValueError:
    print('You should input a valid number!')