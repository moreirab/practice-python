#rock, paper, scissors
import random

moves_dict = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}

def rock_paper_scissors():
    print('Choose your move: [r]ock, [p]aper or [s]cissors')
    moves_list = list(moves_dict.keys())
    ai = random.choice(moves_list)
    player = input().lower()

    try:
        if player not in moves_list:
            raise ValueError
        else:
            print('Your move: {}; Opponent\'s move: {}'\
                    .format(moves_dict.get(player), moves_dict.get(ai)))
            if player == ai:
                print('Draw!')
                restart()
            if player == 'r':
                if ai == 's':
                    print('You win!')
                    restart()
                else:
                    print('You lose!')
                    restart()
            elif player == 'p':
                if ai == 'r':
                    print('You win!')
                    restart()
                else:
                    print('You lose!')
                    restart()
            elif player == 's':
                if ai == 'p':
                    print('You win!')
                    restart()
                else:
                    print('You lose!')
                    restart()
            
    except ValueError:
        print('You should input a valid option ([r]ock, [p]aper or [s]cissors)')

def restart():
    try:
        print('Restart? [y]es or [n]o')
        restart = input().lower()

        if restart == 'y':
            return rock_paper_scissors()
        elif restart == 'n':
            exit()
        else:
            raise ValueError
    except ValueError:
        print('You should input a valid option ([y]es or [n]o)')        

rock_paper_scissors()