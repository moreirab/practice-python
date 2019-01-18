# source: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

def divisors(num=None):
    print('Input a number and I\'ll show you all their divisors (if there\'re any)!')
    input_num = 0
    try:
        input_num = int(input(''))
        return [x for x in range(2, input_num) if input_num%x==0]
    except ValueError:
        print('You should input a valid number!')

print(divisors())