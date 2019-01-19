import random

def random_list(num_elem=0, random_range=0):
    return [random.randint(0, random_range) for x in range(0, random.randint(0, num_elem))]

def input_number(msg):
    print(msg)
    try:
        return int(input())
    except ValueError:
        print('You should input a valid number!')