# source: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

def check_divisors(num):
    return [x for x in range(2, num) if num%x==0]

def divisors():
    print('Input a number and I\'ll show you all their divisors (if there\'re any)!')
    input_num = 0
    try:
        input_num = int(input())
        if input_num == 0 or input_num == 1:
            raise ValueError
        print(divisors(num=input_num))
    except ValueError:
        print('You should input a valid number!')