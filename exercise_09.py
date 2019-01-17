# source: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
import random

guesses = []
num = random.randint(1,10)
def guess_num():    
    try:
        print('From 1 to 9, guess and input the generated number (or type \'exit\' to leave):')
        guess = input()
        if guess == 'exit':
            print_inputed_numbers(guesses)
        elif not guess.isnumeric():
            raise ValueError
        else:
            guess = int(guess)
            guesses.append(guess)
            if guess < num:
                print('Too low! Try again!')
                guess_num()
            elif guess > num:
                print('Too high! Try again!')
                guess_num()
            else:
                print('You\'re exatly right! Congratulations! :)')
                print_inputed_numbers(guesses)
    except ValueError:
        print('You should input a valid number (between 1 and 9, inclusive.)')

def print_inputed_numbers(guesses):
    print('# of attempts: {}'.format(len(guesses)))
    print('Inputed numbers')
    print(guesses)
    exit()


print(guess_num())